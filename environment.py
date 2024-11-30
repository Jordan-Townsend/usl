# environment.py

class Environment:
    def __init__(self, parent=None):
        self.variables = {}
        self.parent = parent
        if parent is None:
            # Initialize built-in variables and functions
            self.variables.update({
                'None': None,
                'True': True,
                'False': False,
            })
            from usl_builtins import built_in_functions
            self.variables.update(built_in_functions)

    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        elif self.parent:
            return self.parent.get_variable(name)
        else:
            raise NameError(f'Undefined variable "{name}"')

    def set_variable(self, name, value):
        self.variables[name] = value

    def define_function(self, name, func_def):
        self.variables[name] = func_def

    def define_variable(self, name, value):
        self.variables[name] = value
