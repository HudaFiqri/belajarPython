#dictionary isi data

data = {
    'nama' : 'M Huda Fiqri',
    'kelas' : 'x tkj a',
    'umur' : 16,
    'jenis kelamin' : 'laki',
    'hobi' : ['ngonfig', 'ngoding'],
    'skill' : ['networking', 'programming', 'desain']
    }

#pemanggilan basic

print('#pemanggilan basic')

print('nama saya = %s' % data['nama'])
print('kelas = %s' % data['kelas'])
print('umur =', data['umur'])
print('jenis kelamin = %s' % data['jenis kelamin'])
print('hobi = %s' % data['hobi'])
print('skill = %s' % data['skill'])

print('')

#pemanggilan dengan metode get()

data2 = {
    'nama' : 'M Huda Fiqri',
    'kelas' : 'x tkj a',
    'umur' : 16,
    'jenis kelamin' : 'laki',
    'hobi' : ['ngonfig', 'ngoding'],
    'skill' : ['networking', 'programming', 'desain']
    }

print('#pemanggilan dengan metode get()')

print('nama = ', data.get('nama'))
print('kelas = ', data.get('kelas'))
print('umur =', data.get('umur'))
print('jenis kelamin = ', data.get('jenis kelamin'))
print('hobi = ', data.get('hobi'))
print('skill = ', data.get('skill'))
