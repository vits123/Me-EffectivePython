"""
 function takes a bytes or str instance and always returns a str:

"""


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str


print(to_str(b'hello'))  # prints hello
