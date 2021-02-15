'''
dengan membaca file kita bisa menampilkan isi dari sebuah file

sumber referensi: https://www.petanikode.com/python-file/
ditulis pada padal: 14-02-2021
'''

#membuka isi dari sebuah file
#r = read, memungkinkan untuk membaca isi dari sebuah file
file = open('file.txt', 'r')

#membaca hanya 1 baris
isi_file = file.readline()
#membaca semua baris pada file
isi_file2 = file.readlines()

#output 1 baris
print(isi_file)

#menampilkan semua isi dari file
for x in isi_file2:
    print(x, end='')

#menutup isi dari file
file.close()