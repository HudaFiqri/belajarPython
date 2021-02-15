'''
sumber referensi: https://www.petanikode.com/python-file
ditulis pada: 14-02-2021
'''

#a = append, dengan append bisa menambahkan data ke dalam file tanpa perlu mengubah isi dari keseluruhan file
data_file = open('file.txt', 'a')

#membuat input user
data_id = input('masukkan id >>> ')
data_user = input('masukkan username >>> ')
data_password = input('masukkan password >>> ')

#membuat output yang akan dikeluarkan
data = ('\n\nID: {id}\nUser Name: {user}\nUser Password: {passw}'.format(id=data_id, user=data_user, passw=data_password))

#melakukan penulisan atau commit ke dalam file
data_file.write(data)