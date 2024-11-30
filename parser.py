# parser.py

from lexer import Token
from ast_nodes import *
from error import UslError

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current_token(self):
        return self.tokens[self.position] if self.position < len(self.tokens) else None

    def expect(self, *expected_types):
        token = self.current_token()
        if token and token.type in expected_types:
            self.position += 1
            return token
        else:
            expected = ', '.join(expected_types)
            actual = token.type if token else 'EOF'
            raise UslError(f'Expected {expected}, got {actual}', token.line if token else None)

    def match(self, *expected_types):
        token = self.current_token()
        return token and token.type in expected_types

    def parse(self):
        statements = []
        while self.current_token():
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            else:
                break
        return StatementList(statements)

    def parse_statement(self):
        if self.match('SEMICOLON'):
            self.expect('SEMICOLON')
            return None
        elif self.match('DEF'):
            return self.parse_function_def()
        elif self.match('CLASS'):
            return self.parse_class_def()
        elif self.match('IF'):
            return self.parse_if_statement()
        elif self.match('WHILE'):
            return self.parse_while_loop()
        elif self.match('FOR'):
            return self.parse_for_loop()
        elif self.match('RETURN'):
            return self.parse_return_statement()
        elif self.match('BREAK'):
            self.expect('BREAK')
            self.expect('SEMICOLON')
            return BreakStatement()
        elif self.match('CONTINUE'):
            self.expect('CONTINUE')
            self.expect('SEMICOLON')
            return ContinueStatement()
        else:
            expr = self.parse_expression()
            if self.match('ASSIGN'):
                self.expect('ASSIGN')
                value = self.parse_expression()
                self.expect('SEMICOLON')
                return Assignment([expr], value)
            elif self.match('SEMICOLON'):
                self.expect('SEMICOLON')
                return ExpressionStatement(expr)
            else:
                raise UslError(f'Expected ASSIGN or SEMICOLON', self.current_token().line)

    def parse_expression(self):
        return self.parse_or_expression()

    def parse_or_expression(self):
        left = self.parse_and_expression()
        while self.match('OR'):
            op = self.expect('OR').type
            right = self.parse_and_expression()
            left = BinaryOp(left, op, right)
        return left

    def parse_and_expression(self):
        left = self.parse_equality_expression()
        while self.match('AND'):
            op = self.expect('AND').type
            right = self.parse_equality_expression()
            left = BinaryOp(left, op, right)
        return left

    def parse_equality_expression(self):
        left = self.parse_relational_expression()
        while self.match('EQ', 'NEQ'):
            op = self.expect('EQ', 'NEQ').type
            right = self.parse_relational_expression()
            left = BinaryOp(left, op, right)
        return left

    def parse_relational_expression(self):
        left = self.parse_additive_expression()
        while self.match('LT', 'GT', 'LE', 'GE'):
            op = self.expect('LT', 'GT', 'LE', 'GE').type
            right = self.parse_additive_expression()
            left = BinaryOp(left, op, right)
        return left

    def parse_additive_expression(self):
        left = self.parse_multiplicative_expression()
        while self.match('ADD', 'SUB'):
            op = self.expect('ADD', 'SUB').type
            right = self.parse_multiplicative_expression()
            left = BinaryOp(left, op, right)
        return left

    def parse_multiplicative_expression(self):
        left = self.parse_unary_expression()
        while self.match('MUL', 'DIV', 'MOD'):
            op = self.expect('MUL', 'DIV', 'MOD').type
            right = self.parse_unary_expression()
            left = BinaryOp(left, op, right)
        return left

    def parse_unary_expression(self):
        if self.match('NOT', 'ADD', 'SUB'):
            op = self.expect('NOT', 'ADD', 'SUB').type
            expr = self.parse_unary_expression()
            return UnaryOp(op, expr)
        else:
            return self.parse_primary_expression()

    def parse_primary_expression(self):
        token = self.current_token()
        if self.match('NUMBER'):
            self.expect('NUMBER')
            return Number(token.value)
        elif self.match('STRING'):
            self.expect('STRING')
            return String(token.value)
        elif self.match('TRUE'):
            self.expect('TRUE')
            return Boolean(True)
        elif self.match('FALSE'):
            self.expect('FALSE')
            return Boolean(False)
        elif self.match('IDENT'):
            return self.parse_identifier()
        elif self.match('LPAREN'):
            self.expect('LPAREN')
            expr = self.parse_expression()
            self.expect('RPAREN')
            return expr
        else:
            raise UslError(f'Unexpected token {token.type}', token.line)

    def parse_identifier(self):
        token = self.expect('IDENT')
        expr = Identifier(token.value)
        while self.match('LPAREN', 'DOT'):
            if self.match('LPAREN'):
                expr = self.parse_function_call(expr)
            elif self.match('DOT'):
                self.expect('DOT')
                attr_name = self.expect('IDENT').value
                expr = Attribute(expr, attr_name)
        return expr

    def parse_function_call(self, func):
        self.expect('LPAREN')
        arguments = []
        if not self.match('RPAREN'):
            arguments.append(self.parse_expression())
            while self.match('COMMA'):
                self.expect('COMMA')
                arguments.append(self.parse_expression())
        self.expect('RPAREN')
        return FunctionCall(func, arguments)

    def parse_function_def(self):
        self.expect('DEF')
        name = self.expect('IDENT').value
        self.expect('LPAREN')
        params = []
        if not self.match('RPAREN'):
            params.append(self.expect('IDENT').value)
            while self.match('COMMA'):
                self.expect('COMMA')
                params.append(self.expect('IDENT').value)
        self.expect('RPAREN')
        body = self.parse_block()
        return FunctionDef(name, params, body)

    def parse_class_def(self):
        self.expect('CLASS')
        name = self.expect('IDENT').value
        bases = []
        if self.match('EXTENDS'):
            self.expect('EXTENDS')
            bases.append(self.expect('IDENT').value)
        body = self.parse_block()
        return ClassDef(name, bases, body)

    def parse_if_statement(self):
        self.expect('IF')
        self.expect('LPAREN')
        condition = self.parse_expression()
        self.expect('RPAREN')
        then_branch = self.parse_block()
        else_branch = None
        if self.match('ELSE'):
            self.expect('ELSE')
            else_branch = self.parse_block()
        return IfStatement(condition, then_branch, else_branch)

    def parse_while_loop(self):
        self.expect('WHILE')
        self.expect('LPAREN')
        condition = self.parse_expression()
        self.expect('RPAREN')
        body = self.parse_block()
        return WhileLoop(condition, body)

    def parse_for_loop(self):
        self.expect('FOR')
        self.expect('LPAREN')
        init = self.parse_statement()
        condition = self.parse_expression()
        self.expect('SEMICOLON')
        update = self.parse_expression()
        self.expect('RPAREN')
        body = self.parse_block()
        return ForLoop(init, condition, update, body)

    def parse_return_statement(self):
        self.expect('RETURN')
        expression = self.parse_expression()
        self.expect('SEMICOLON')
        return ReturnStatement(expression)

    def parse_block(self):
        self.expect('LBRACE')
        statements = []
        while not self.match('RBRACE'):
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        self.expect('RBRACE')
        return Block(statements)
