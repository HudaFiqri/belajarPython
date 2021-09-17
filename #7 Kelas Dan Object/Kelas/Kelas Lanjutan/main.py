class counting:
    
    def tambah(self, value1, value2 ):

        self.value1 = value1
        self.value2 = value2
        
        output = ( self.value1 + self.value2 )
        
        return output
    
    def kurang( self, value1, value2 ):

        self.value1 = value1
        self.value2 = value2

        output = ( value1 - value2 )

        print(output)

    def kali( self, value1, value2 ):

        self.value1 = value1
        self.value2 = value2

        output = ( self.value1 * self.value2 )

        return output

    def bagi( self, value1, value2 ):

        self.value1 = value1
        self.value2 = value2

        output = ( self.value1, self.value2 )

        return output

ct = counting()
print(ct.tambah(5, 5))
