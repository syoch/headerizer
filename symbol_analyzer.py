from typing import List, Tuple
import string


def is_identifier(token: str) -> bool:
    return token.isalpha() or token.isdigit() or token == '_'


class Tokenizer():
    def __init__(self, src: str):
        self.tokens = []
        self.index = 0
        self.tokenize(src)

    def peek(self) -> str:
        return self.tokens[self.index]

    def next(self) -> str:
        self.index += 1
        return self.tokens[self.index - 1]

    def has_more(self) -> bool:
        return self.index < len(self.tokens)

    def expect(self, tok: str) -> str:
        if self.peek() == tok:
            self.next()
            return True
        else:
            raise Exception(f'Expected {tok}, got {self.peek()}')

    def consume(self, tok: str) -> str:
        if self.peek() == tok:
            self.next()
            return True
        else:
            return False

    def tokenize(self, src: str) -> None:
        while src:
            ch = src[0]
            next = src[1] if len(src) > 1 else None

            if ch in string.whitespace:
                src = src[1:]
                continue

            token = ""
            if is_identifier(ch):
                while is_identifier(src[0]):
                    token += src[0]
                    src = src[1:]
            elif ch == ':' and next == ':':
                token = '::'
                src = src[2:]
            else:
                token = src[0]
                src = src[1:]

            self.tokens.append(token)


class FuncName():
    def __init__(self) -> None:
        self.is_static = False
        self.namespaces = []
        self.name = ""
        self.args = []
        self.return_type = ""


class Type():
    def __init__(self) -> None:
        self.length = 0
        self.name = ""
        self.args = []
        self.return_type = ""


def read_type(tokens: List[str]) -> Tuple[str, List[str]]:
    pass


def read_func(tokens: List[str]) -> Tuple[str, List[str]]:
    is_static = False
    if tokens[0:1] == ["static"]:
        tokens = tokens[1:]
        is_static = True
    pass


if __name__ == "__main__":
    tokenizer = Tokenizer(
        "hello1<in_t> std::exception::operator +(hello<int, void<t>>)")
    print(tokenizer.tokens)
