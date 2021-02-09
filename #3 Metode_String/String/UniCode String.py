###encode string
string_byte_prefix = u'您好'

###menampilkan string
print(type(string_byte_prefix))

###encode string ke byte
to_byte_String = bytes(string_byte_prefix, 'UTF-8')

###decode string
print(bytes.decode(to_byte_String))
