class main_class():
    
    def class_function(self):
        
        # buat nama variable yang akan dibuat public variable
        global var_class_function

        # variable yang nantinya akan dipanggil ke public
        var_class_function = "hello world"

def main_function():
    
    # coba hal yang sama tapi ini tanpa class
    global public_function_variable

    public_function_variable = "variable on function"

    return public_function_variable


# coba panggil dengan menggunakan class
call_class = main_class()
function_on_class = call_class.class_function()

# coba panggil dengan menggunakan fungsi
call_function = main_function()

# memanggil variable yang berada didalam class
print(public_function_variable)

# memanggil variable yang berada didalam funsi
print(var_class_function)