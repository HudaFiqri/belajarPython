#sama dengan append(), insert() juga memakai metode yang sama
#tapi bedanya adalah insert bisa menambahkan secara
#detail dimana data yang ingin di tambahkan

#data array
#array variable

a = ['mangga', 'durian', 'rambutan', 'pepaya']

#disini saya memiliki data a
#data a sama dengan

#mangga = 0
#durian = 1
#rambutan = 2
#pepaya = 3

#dan saya ingin menambahkan data manggis di urutan 1
#maka data durian akan tergantikan dan tergeser

a.insert(1, 'manggis')

#1 itu urutan arraynya
#manggis itu data arraynya

print('#array variable')
print(a)

print('')

#nah bagaimana jika kita ingin menambahkan array
#numerik ke dalam data

#data array
#array numerik

b = [1, 2, 3, 4]

#saya mempunyai data angka 10 dan saya ingin menaruhnya
#di urutan 2 di data array

b.insert(2, 10)


print('#array numerik')
print(b)
