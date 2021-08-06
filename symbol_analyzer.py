from typing import List
import string

print("hello")


def tokenize(src: str) -> List[str]:
    while src:
        ch = src[0]
        next = src[1] if len(src) > 1 else None

        token = ""
        if ch in string.ascii_letters:
            while src[0] in string.ascii_letters:
                token += src[0]
                src = src[1:]
        elif ch == ':' and next == ':':
            token = '::'
            src = src[2:]
        else:
            token = src[0]
            src = src[1:]

        print(token)


if __name__ == "__main__":
    tokenize("hello<int> std::exception::~exception(hello<int, void<t>>)")
