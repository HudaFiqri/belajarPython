###import semua module yang akan digunakan
from datetime import *

###panggil module now untuk memanggil fungsi wakti
waktu = datetime.now()

###menampilkan output dari [nama hari:tahun:bulan:tanggal]
print(f'{waktu.strftime("%A")}, {waktu.day}-{waktu.month}-{waktu.year}')

###menampilkan output dari [jam:menit:detik]
print(f'{waktu.hour}:{waktu.minute}:{waktu.second}')
