'''
dengan python bisa melakukan manipulasi sebuah file

sumber referensi: https://www.petanikode.com/python-file/
ditulis pada: 14-02-2021
'''

#membaca file yang akan di tulis
#w = write, ini digunakan untuk mengubah isi dari sebuah file
file = open('file.txt', 'w')

#membuat sebuah user inputan
text = input('masukkan kata >>> ')

#apply atau commit ke file yang dituju untuk mengubah file tersebut
file.write(text)

#menampilkan output dari file user inputan
print('menulis isi file dengan output = {isi}'.format(isi=text))