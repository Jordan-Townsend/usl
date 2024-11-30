# interpreter.py

from ast_nodes import *
from environment import Environment
from usl_builtins import built_in_functions
from error import UslError, UslReturn, UslBreak, UslContinue

def evaluate(node, env):
    if isinstance(node, Number):
        return node.value
    elif isinstance(node, String):
        return node.value
    elif isinstance(node, Boolean):
        return node.value
    elif isinstance(node, NoneType):
        return None
    elif isinstance(node, Identifier):
        return env.get_variable(node.name)
    elif isinstance(node, BinaryOp):
        left = evaluate(node.left, env)
        right = evaluate(node.right, env)
        return eval_binary_op(node.op, left, right)
    elif isinstance(node, UnaryOp):
        expr = evaluate(node.expr, env)
        return eval_unary_op(node.op, expr)
    elif isinstance(node, Assignment):
        value = evaluate(node.expression, env)
        for target in node.targets:
            if isinstance(target, Identifier):
                env.set_variable(target.name, value)
            elif isinstance(target, Attribute):
                obj = evaluate(target.obj, env)
                setattr(obj, target.attr, value)
            else:
                raise UslError('Invalid assignment target')
        return value
    elif isinstance(node, ExpressionStatement):
        return evaluate(node.expression, env)
    elif isinstance(node, FunctionCall):
        func = evaluate(node.func, env)
        args = [evaluate(arg, env) for arg in node.arguments]
        if callable(func):
            return func(*args)
        elif isinstance(func, FunctionDef):
            func_env = Environment(func.env)
            if len(args) != len(func.params):
                raise UslError(f'Function "{func.name}" expected {len(func.params)} arguments, got {len(args)}')
            for param, arg in zip(func.params, args):
                func_env.set_variable(param, arg)
            try:
                evaluate(func.body, func_env)
            except UslReturn as ret:
                return ret.value
            return None
        else:
            raise UslError(f'"{func}" is not a function')
    elif isinstance(node, FunctionDef):
        node.env = env
        env.define_function(node.name, node)
    elif isinstance(node, ClassDef):
        cls = UslClass(node.name, node, env)
        env.define_variable(node.name, cls)
    elif isinstance(node, ReturnStatement):
        value = evaluate(node.expression, env) if node.expression else None
        raise UslReturn(value)
    elif isinstance(node, IfStatement):
        condition = evaluate(node.condition, env)
        if condition:
            return evaluate(node.then_branch, env)
        elif node.else_branch:
            return evaluate(node.else_branch, env)
    elif isinstance(node, WhileLoop):
        while evaluate(node.condition, env):
            try:
                evaluate(node.body, env)
            except UslBreak:
                break
            except UslContinue:
                continue
            except UslReturn as ret:
                raise ret
    elif isinstance(node, ForLoop):
        evaluate(node.init, env)
        while evaluate(node.condition, env):
            try:
                evaluate(node.body, env)
                evaluate(node.update, env)
            except UslBreak:
                break
            except UslContinue:
                evaluate(node.update, env)
                continue
            except UslReturn as ret:
                raise ret
    elif isinstance(node, BreakStatement):
        raise UslBreak()
    elif isinstance(node, ContinueStatement):
        raise UslContinue()
    elif isinstance(node, Block):
        for stmt in node.statements:
            result = evaluate(stmt, env)
            if isinstance(stmt, ReturnStatement):
                return result
        return None
    elif isinstance(node, StatementList):
        for stmt in node.statements:
            result = evaluate(stmt, env)
        return result
    elif isinstance(node, Attribute):
        obj = evaluate(node.obj, env)
        if hasattr(obj, node.attr):
            return getattr(obj, node.attr)
        elif isinstance(obj, UslInstance):
            return getattr(obj, node.attr)
        else:
            raise UslError(f'Attribute "{node.attr}" not found')
    else:
        raise UslError('Unknown AST node')

def eval_binary_op(op, left, right):
    if op == 'ADD':
        return left + right
    elif op == 'SUB':
        return left - right
    elif op == 'MUL':
        return left * right
    elif op == 'DIV':
        return left / right
    elif op == 'MOD':
        return left % right
    elif op == 'EQ':
        return left == right
    elif op == 'NEQ':
        return left != right
    elif op == 'LT':
        return left < right
    elif op == 'GT':
        return left > right
    elif op == 'LE':
        return left <= right
    elif op == 'GE':
        return left >= right
    elif op == 'AND':
        return left and right
    elif op == 'OR':
        return left or right
    else:
        raise UslError(f'Unknown operator {op}')

def eval_unary_op(op, expr):
    if op == 'ADD':
        return +expr
    elif op == 'SUB':
        return -expr
    elif op == 'NOT':
        return not expr
    else:
        raise UslError(f'Unknown operator {op}')

class UslClass:
    def __init__(self, name, class_def, env):
        self.name = name
        self.class_def = class_def
        self.env = env
        self.methods = {}
        self.bases = []
        for base_name in class_def.bases:
            base = env.get_variable(base_name)
            self.bases.append(base)
        self.initialize_class()

    def initialize_class(self):
        class_env = Environment(self.env)
        evaluate(self.class_def.body, class_env)
        self.methods = class_env.variables

    def __call__(self, *args, **kwargs):
        instance = UslInstance(self)
        init_method = self.methods.get('__init__')
        if not init_method:
            # Check base classes for __init__
            for base in self.bases:
                init_method = base.methods.get('__init__')
                if init_method:
                    break
        if init_method:
            func_env = Environment(init_method.env)
            func_env.set_variable('self', instance)
            if isinstance(init_method, FunctionDef):
                expected_args = len(init_method.params) - 1  # Exclude 'self'
                if len(args) != expected_args:
                    raise UslError(f'__init__ expected {expected_args} arguments, got {len(args)}')
                for param, arg in zip(init_method.params[1:], args):  # Skip 'self'
                    func_env.set_variable(param, arg)
                try:
                    evaluate(init_method.body, func_env)
                except UslReturn:
                    pass
            else:
                raise UslError('__init__ is not a function')
        return instance



class UslInstance:
    def __init__(self, cls):
        self.cls = cls
        self.attributes = {}

    def __getattr__(self, name):
        if name in self.attributes:
            return self.attributes[name]
        if name in self.cls.methods:
            method = self.cls.methods[name]
            if isinstance(method, FunctionDef):
                return self.bind_method(method)
            else:
                return method
        # Search in base classes
        for base in self.cls.bases:
            if isinstance(base, UslClass):
                if name in base.methods:
                    method = base.methods[name]
                    if isinstance(method, FunctionDef):
                        return self.bind_method(method)
                    else:
                        return method
        raise AttributeError(f"'{self.cls.name}' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        if name in ('cls', 'attributes'):
            super().__setattr__(name, value)
        else:
            self.attributes[name] = value

    def bind_method(self, method):
        def bound_method(*args):
            func_env = Environment(self.cls.env)
            func_env.set_variable('self', self)
            expected_args = len(method.params) - 1  # Exclude 'self'
            if len(args) != expected_args:
                raise UslError(f'Method "{method.name}" expected {expected_args} arguments, got {len(args)}')
            for param, arg in zip(method.params[1:], args):  # Skip 'self' in params
                func_env.set_variable(param, arg)
            try:
                evaluate(method.body, func_env)
            except UslReturn as ret:
                return ret.value
        return bound_method
