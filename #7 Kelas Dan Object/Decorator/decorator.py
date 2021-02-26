'''
decorator
jadi agar memudahkan dalam pembungkusan fungsi maka python menyediakan yang namanya decorator.

sumber referensi: https://www.youtube.com/watch?v=r7Dtus7N4pI
direvisi pada: 26-02-2021
'''

'''
membuat fungsi yang akan dipanggil.

jadi di decorator pada python harus fungsi rekursif untuk mengembalikan value jika tidak ada rekursif maka python akan menunjukan error
TypeError: 'NoneType' object is not callable | ini dikarenakan tidak adanya rekursif pada fungsi.
'''
def f1(func):

    # jika ada variabel yang di keluarkan maka akan menghasilkan output
    function_data = 'function data'
    print(function_data)
    return func

# nah ini lah yang unik dari python decorator dilambangkan dengan @ dan ini bertujuan untuk memanggil fungsi
@f1
def func_data():
    print('hello')

# lalu coba panggil fungsi yang baru dan coba output seperti apakah yang akan keluar
func_data()
