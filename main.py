# main.py

import sys
from lexer import tokenize
from parser import Parser
from interpreter import evaluate
from environment import Environment
from error import UslError

def main():
    if len(sys.argv) < 2:
        print('Usage: python main.py <script.usl>')
        return
    script_path = sys.argv[1]
    try:
        with open(script_path, 'r') as f:
            code = f.read()
        tokens = tokenize(code)
        parser = Parser(tokens)
        ast = parser.parse()
        env = Environment()
        evaluate(ast, env)
    except UslError as e:
        print(f'Error: {e}')
    except FileNotFoundError:
        print(f'File not found: {script_path}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

if __name__ == '__main__':
    main()
