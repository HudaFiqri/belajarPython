#memotong array bisa dengan menggunakan fungsi del
#dengan cara memasukkan angka dari urutan array

#array variable
#data array
a = ['medan', 'banjarmasin', 'jakarta', 'pekanbaru']

#saya ingin memotong array dengan menyisakan medan dan pekanbaru

del a[1:3]

print(a)

#hmm sepertinya jika menggunakan fungsi del akan dihitung dari 1
#bukan dari 0
