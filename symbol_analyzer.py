from typing import List
import string


def is_identifier(token: str) -> bool:
    return token.isalpha() or token.isdigit() or token == '_'


def tokenize(src: str) -> List[str]:
    tokens = []
    while src:
        ch = src[0]
        next = src[1] if len(src) > 1 else None

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

        tokens.append(token)

    return tokens


if __name__ == "__main__":
    tokenize("hello1<in_t> std::exception::~exception(hello<int, void<t>>)")
