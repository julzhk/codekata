def encode_caesar(s: str, offset=1):
    ''' encode a string using a caesar cipher '''
    return ''.join([chr(encode_letter_code(c, offset)) for c in s.lower()])


def encode_letter_code(s: str, offset: int) -> int:
    if not s.isalpha():
        return ord(s)
    return (ord(s) + offset - ord('a')) % 26 + ord('a')


print(encode_caesar('a what is for lunch!', 13))


def decode_caesar(s: str, offset=1):
    ''' decode a string using a caesar cipher '''
    return ''.join([chr(decode_letter_code(c, offset)) for c in s.lower()])


def decode_letter_code(s: str, offset: int) -> int:
    if not s.isalpha():
        return ord(s)
    return (ord(s) - offset - ord('a')) % 26 + ord('a')


print(decode_caesar('n jung vf sbe yhapu!', 13))
