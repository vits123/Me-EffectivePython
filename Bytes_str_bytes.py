"""
  This function takes bytes or str instance and always returns a bytes:
"""


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of bytes


print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))