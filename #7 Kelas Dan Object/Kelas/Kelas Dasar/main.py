'''
class merupakan kumpulan dari beberapa fungsi yang sudah siap untuk di panggil atau akan dijalankan.
class sendiri ibarat blueprint atau rancangan dari sebuah code yang akan di eksekusi, class sendiri bisa
di ibaratkan sebagai blueprint dalam suatu pengerjaan, ketika dipanggil maka code akan mengeksekusi blueprint tersebut.

sumber referensi: - https://www.geeksforgeeks.org/self-in-python-class/
                  - http://mn-belajarpython.blogspot.com/2016/11/penjelasan-kata-self-pada-class-python.html
                  - https://www.w3schools.com/python/python_classes.asp
                  - https://www.w3schools.com/python/gloss_python_class.asp
ditulis pada: 20-02-2021
'''

# buat terlebih dahulu class yang akan dipanggil nantinya
class MainClass:

    # self adalah sebuah variabel yang dimana untuk menyatakan classnya.
    # jika menggunakan IDE seperti PyCharm seperti yang digunakan oleh penulis maka self sendiri akan otomatis digenerate
    # oleh IDE PyCharm.
    def func1(self):
        print('hello world 1')

    def func2(self):
        print('hello world 2')

# memanggil class
callClass = MainClass()

# memanggil fungsi dalam class
callClass.func1()
callClass.func2()