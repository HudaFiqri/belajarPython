from datetime import *

while True:
    data = input('>>> ')

    if (data == 'jam?' or data == 'jam'):

        if (datetime.now().hour < 12):
            print(
                'sekarang jam {jam}:{menit} pagi'.format(jam=datetime.now().hour, menit=datetime.now().minute))

        elif (datetime.now().hour < 15):
            print(
                'sekarang jam {jam}:{menit} siang'.format(jam=datetime.now().hour, menit=datetime.now().minute))

        elif (datetime.now().hour < 18):
            print(
                'sekarang jam {jam}:{menit} sore'.format(jam=datetime.now().hour, menit=datetime.now().minute))

        elif (datetime.now().hour < 24):
            print(
                'sekarang jam {jam}:{menit} malam'.format(jam=datetime.now().hour, menit=datetime.now().minute))

    elif (data == 'exit'):
        break

    else:
        print('input masukkan salah')