# usl_builtins.py

def built_in_print(*args):
    print(*args)

def built_in_input(prompt=''):
    return input(prompt)

def built_in_len(obj):
    return len(obj)

def built_in_type(obj):
    return type(obj).__name__

def built_in_int(obj):
    return int(obj)

def built_in_float(obj):
    return float(obj)

def built_in_str(obj):
    return str(obj)

def built_in_bool(obj):
    return bool(obj)

def built_in_list(obj):
    return list(obj)

def built_in_dict(obj):
    return dict(obj)

def built_in_set(obj):
    return set(obj)

def built_in_range(*args):
    return list(range(*args))  # Converted to list for compatibility

def built_in_abs(x):
    return abs(x)

def built_in_round(x, ndigits=None):
    return round(x, ndigits)

built_in_functions = {
    'print': built_in_print,
    'input': built_in_input,
    'len': built_in_len,
    'type': built_in_type,
    'int': built_in_int,
    'float': built_in_float,
    'str': built_in_str,
    'bool': built_in_bool,
    'list': built_in_list,
    'dict': built_in_dict,
    'set': built_in_set,
    'range': built_in_range,
    'abs': built_in_abs,
    'round': built_in_round,
}
