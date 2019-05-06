#test ping

import os
import socket

akses = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#buat protokol tcp

ipadd = input("masukkan ip address = ")

net = os.system('ping ' + ipadd)

if net == 0:
    print('berhasil menghubungkan server')

else:
    print('gagal menghubungkan server')
