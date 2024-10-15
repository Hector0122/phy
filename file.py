# instalar Pandas 
# instalar NumPy 
# instalar matplotlib 


PI = 3.1416

arr = [1, 2, 3, 4, 5]
tu = (1, 2, 3, 4, 5)

print("El valor de PI es: " + str(PI))

print('Dame tu nombre:')
nombre = input()

print(f"Tu nombre es: {nombre}")


def suma(a, b):
    return a + b

class Suma:    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def operation(self, a, b):
        return a + b
    

sumann = lambda a, b: a + b

print(suma(1, 2))
print(sumann(1, 2))
print(Suma.operation(2, 4))

