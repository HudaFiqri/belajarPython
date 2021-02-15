#modul

import os
import time

#mesin kalkulator

def tam(a, b):
    return (a + b)
def kur(a, b):
    return a - b
def kal(a, b):
    return a * b
def bag(a, b):
    return a / b

#menu
if __name__ == '__main__':
    while True:
        os.system('cls')
        os.system('color 0b')
        print('Selamat Datang Di Program Kasir McDonald')
        print('')
        print('Silahkan Pilih Menu:')
        print('1. Teh\t\t\t Rp.8000')
        print('2. McSpicy\t\t Rp.39000')
        print('3. Nasi Medium\t\t Rp.5000')
        print('4. Nasi Large\t\t Rp.7000')
        print('5. Hash Brown\t\t Rp.7000')
        print('0. keluar')
        print('')

        inp = input('pilih>>> ')

        #masukkan input
        if('0' == inp):
            break
        
        elif('1' == inp):
            inp1 = int(input('masukkan jumlah>>> '))
            inp2 = int(input('masukkan Rp>>> '))
            harga_teh = 8000
            harga1 = kal(harga_teh, inp1)

            kembali = inp2 - harga1

            print('')

            print('uang yang terima =', inp2)
            print('uang yang kembalikan =', kembali)
            print('harga keseluruhan =', harga1)

        elif('2' == inp):
            inp1 = int(input('masukkan jumlah>>> '))
            inp2 = int(input('masukkan Rp>>> '))
            harga_mc = 39000
            harga1 = kal(harga_mc, inp1)

            kembali = inp2 - harga1

            print('')

            print('uang yang terima =', inp2)
            print('uang yang kembalikan =', kembali)
            print('harga keseluruhan =', harga1)

        elif('3' == inp):
            inp1 = int(input('masukkan jumlah>>> '))
            inp2 = int(input('masukkan Rp>>> '))
            harga_med = 5000
            harga1 = kal(harga_med, inp1)

            kembali = inp2 - harga1

            print('')

            print('uang yang terima =', inp2)
            print('uang yang kembalikan =', kembali)
            print('harga keseluruhan =', harga1)

        elif('4' == inp):
            inp1 = int(input('masukkan jumlah>>> '))
            inp2 = int(input('masukkan Rp>>> '))
            harga_lar = 7000
            harga1 = kal(harga_lar, inp1)

            kembali = inp2 - harga1

        elif('5' == inp):
            inp1 = int(input('masukkan jumlah>>> '))
            inp2 = int(input('masukkan Rp>>> '))
            harga_has = 7000
            harga1 = kal(harga_has, inp1)

            kembali = inp2 - harga1

            print('')

            print('uang yang terima =', inp2)
            print('uang yang kembalikan =', kembali)
            print('harga keseluruhan =', harga1)


        else:
            print('pengetikan salah')

        print('')

        awal = input('kembali (y/n)>>> ')

        if('n' == awal):
            break
