#modul
import os
import time

#mesin
def tambah(a, b):
    return a + b

def kurang(c, d):
    return c - d

def kali(e, f):
    return e * f

def bagi(x, y):
    return round(x / y)

#menu
if __name__ == '__main__':

    while True:

        print('1. tambah')
        print('2. kurang')
        print('3. kali')
        print('4. bagi')
        print('0. keluar')

        pilih = input('pilih >>> ')

        #pilihan
        if(pilih == '1'):
            in1 = int(input('masukkan angka >>> '))
            in2 = int(input('masukkan angka >>> '))

            print('hasil >>> ', tambah(in1, in2))

        elif(pilih == '2'):
            in1 = int(input('masukkan angka >>> '))
            in2 = int(input('masukkan angka >>> '))
            
            print('hasil >>> ', kurang(in1, in2))

        elif(pilih == '3'):
            in1 = int(input('masukkan angka >>> '))
            in2 = int(input('masukkan angka >>> '))
            
            print('hasil >>> ', kali(in1, in2))

        elif(pilih == '4'):
            in1 = int(input('masukkan angka >>> '))
            in2 = int(input('masukkan angka >>> '))
            
            print('hasil >>> ', bagi(in1, in2))

        elif(pilih == '0'):
            break

        else:
            print('salah tulis master')

        time.sleep(2)
        os.system('cls')
