'''
mengambil data pada Dictionary.

sumber referensi: https://realpython.com/iterate-through-dictionary-python
ditulis pada: 23-02-2021
'''

# ada data sekian dan ingin mengambil data dari dalam
data = {'username':'user1', 'password':'user123'}

# gunakan looping agar data bisa diambil semua
for x in data:
    print(x, '=', data[x])