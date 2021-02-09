###encode string
string_byte = bytes('hello world', 'UTF-8')
string_byte_prefix = b'hello world'

###menampilkan string
print(type(string_byte))
print(type(string_byte_prefix))

###decode string
print(bytes.decode(string_byte))
print(bytes.decode(string_byte_prefix))
