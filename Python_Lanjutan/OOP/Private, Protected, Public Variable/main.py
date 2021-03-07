'''
dengan menggunakan metode ini kita bisa menentukan jenis variable yang akan digunakan

sumber referensi: pintaar module
ditulis pada: 06-03-2021
'''
class Variable:

    def __init__(self):
        '''
        Public Variable

        Merupakan Variable yang dapat diakses semua orang dan dapat dipanggil dengan mudah seperti biasanya
        '''
        self.Var = 'Ini Public Variable'

        '''
        Protected Variable

        Merupakan variable yang dapat diakses semua orang dan mirip seperti public variable yang membedakannya adalah pada underscore _
        '''
        self._Var = 'Ini Protected Variable'

        '''
        Private Variable

        Merupakan Variable yang tidak dapat diakses. Variable jenis ini dapat diakses melalui panggilan difunction atau method
        '''
        self.__Var = 'Ini Private Variable'

    def Pri_Var(self):
        self.__Var = 'Ini Private Variable Yang Terpanggil'
        return self.__Var


Variable_Class = Variable()

# Contoh untuk pemanggilan untuk public variable
print(Variable_Class.Var)

# Contoh untuk pemanggilan untuk protected variable
print(Variable_Class._Var)

# Dan ini contoh untuk private variable
# karena namanya private jadi tidak bisa dipanggil
# print(Variable_Class.__Var)
# untuk memanggil private variable yang dapat terpanggil bisa dilakukan apabila private variablenya berada pada function atau method
print(Variable_Class.Pri_Var())
