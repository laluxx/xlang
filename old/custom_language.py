import re
import sys

def tokenize(text):
    tokens = re.findall(r'\S+|\n', text)
    return tokens

def parse(tokens):
    parsed = []
    while tokens:
        token = tokens.pop(0)
        if token == "FOR":
            n = tokens.pop(0)
            command = tokens.pop(0)
            parsed.append(f'for {n} "{command}"')
        elif token == "WHILE":
            i = tokens.pop(0)
            max_value = tokens.pop(0)
            command = tokens.pop(0)
            parsed.append(f'while {i} {max_value} "{command}"')
    return parsed

def main():
    input_code = sys.stdin.read()
    tokens = tokenize(input_code)
    parsed = parse(tokens)
    for command in parsed:
        print(command)

if __name__ == "__main__":
    main()
