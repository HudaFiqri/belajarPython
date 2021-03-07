'''
method static dan dynamic

sumber referensi: - pintaar module
                  - https://medium.com/ngulicode/method-class-method-dan-static-method-pada-python-1fa5feae4333
ditulis pada: 07-03-2021
'''
class Variable:

    __Data_Variable = 'hello world'

    # di static method jika nama class berubah maka harus mengganti secara manual
    @staticmethod
    def Data1():
        return Variable.__Data_Variable

    # sedangkan untuk dynamic method jika nama class berubah maka tidak akan mempengaruhi code
    @classmethod
    def Data2(cls):
        return cls.__Data_Variable

print(Variable.Data1())
print(Variable.Data2())