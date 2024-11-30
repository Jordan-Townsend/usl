# ast_nodes.py

class ASTNode:
    pass

class Number(ASTNode):
    def __init__(self, value):
        self.value = float(value)

class String(ASTNode):
    def __init__(self, value):
        self.value = bytes(value[1:-1], "utf-8").decode("unicode_escape")

class Boolean(ASTNode):
    def __init__(self, value):
        self.value = value

class NoneType(ASTNode):
    def __init__(self):
        self.value = None

class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name

class BinaryOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class UnaryOp(ASTNode):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

class Assignment(ASTNode):
    def __init__(self, targets, expression):
        self.targets = targets
        self.expression = expression

class ExpressionStatement(ASTNode):
    def __init__(self, expression):
        self.expression = expression

class FunctionCall(ASTNode):
    def __init__(self, func, arguments):
        self.func = func
        self.arguments = arguments

class FunctionDef(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class ClassDef(ASTNode):
    def __init__(self, name, bases, body):
        self.name = name
        self.bases = bases
        self.body = body

class ReturnStatement(ASTNode):
    def __init__(self, expression):
        self.expression = expression

class IfStatement(ASTNode):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

class WhileLoop(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class ForLoop(ASTNode):
    def __init__(self, init, condition, update, body):
        self.init = init
        self.condition = condition
        self.update = update
        self.body = body

class BreakStatement(ASTNode):
    pass

class ContinueStatement(ASTNode):
    pass

class Block(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class StatementList(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class Attribute(ASTNode):
    def __init__(self, obj, attr):
        self.obj = obj
        self.attr = attr
