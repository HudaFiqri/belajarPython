'''
dengan metode ini bisa dilakukan pengecekan apakah file ada atau tidak

sumber refensi: kumpulan solusi pemprogramman python(penulis: budi raharjo)
ditulis pada: 14-02-2021
'''

#untuk module yang digunakan adalah os
import os

#mengecek apakah file tersedia atau tidak
#untuk code yang dibawah ini sudah bersifat bool yang keluarannya adalah True or False
file = os.path.exists('file.txt')

#mengecek keberadaan file dengan output yang dimanipulasi
if(file == True):
    print('file ditemukan')

elif(file == False):
    print('file tidak ditemukan')