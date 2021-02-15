'''
sumber referensi: - https://amiradata.com/python-get-file-size-in-kb-mb-or-gb
                  - kumpulan solusi pemprogramman python(penulis: Budi Raharjo)
ditulis pada: 15-02-2021
'''

#module yang digunakan menggunakan os
import os

#tentukan dimana filenya berada
file = 'Pic.png'

#panggil modul os dan gunakan module getsize() untuk mendapatkan ukuran file
#ukuran file yang akan ditampilkan adalah dalam bentuk bytes
file_size = os.path.getsize(file)

#convert ukuran file yang asalnya dari bytes ke kilobytes
convert = (float(file_size) / int(1000))

#menampilkan output dari file
print(convert)