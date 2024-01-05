# panggil nama modulenya
import Class_App
# karena folder Class_App ada file __init__.py maka folder tersebut sudah menjadi module

# tinggal panggil nama class didalam folder tersebut
caller_1 = Class_App.main_1()
caller_2 = Class_App.main_2()

# coba panggil function didalam class tersebut
print(caller_1.main_func())
print(caller_2.main_func())