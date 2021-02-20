'''
membuat fungsi di dalam fungsi

sumber referensi: https://realpython.com/inner-functions-what-are-they-good-for/
ditulis pada: 20-02-2021
'''

# buat terlebih dahulu fungsi yang akan di panggil
def func1():

    # baru buat lagi fungsinya
    def func2():
        print('hello world')

    def func3():
        print('guten tag comrade')

    # baru panggil fungsinya
    func2()
    func3()

func1()