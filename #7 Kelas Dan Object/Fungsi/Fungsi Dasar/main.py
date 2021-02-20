'''
dengan fungsi memungkinkan membuat sebuah fungsi tertentu yang akan memudahkan dalam pekerjaan.
misalnya: fungsi dari hitung(10 + 10) akan menghasilkan 20.
hasil akan ditampilkan apabila sebuah fungsi sudah dijabarkan.

inti dari sebuah fungsi adalah membuat sebuah blok kode yang ketika di panggil akan berjalan.

sumber referensi: https://www.w3schools.com/python/python_functions.asp
ditulis pada: 20-02-2021
'''

# membuat fungsi dengan isi
def callFunc():
    print('hello world')

#membuat fungsi dengan code tertentu
def countFunc(a, b):
    hasil = int(a + b)

    # return digunakan untuk mengembalikan hasil atau output
    # jika return tidak di buat kode akan berjalan sebagai mestinya akan tetapi hasil yang akan di panggil none(tidak ada)
    return hasil


# memanggil fungsi
callFunc()

print(countFunc(10, 10))