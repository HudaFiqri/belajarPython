###membungkus fungsi yang akan dipanggil
def my_decorator(func):
    def bungkus():
        print('baris dieksekusi.')
        func()
    return bungkus

###memanggil fungsi yang telah di bungkus dengan decorator @
@my_decorator
def katakan():
    print('hello 1')

###eksekusi kode
katakan()
