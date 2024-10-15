# instalar Pandas (pip3 install pandas)
# instalar NumPy  (pip3 install NumPy)
# instalar matplotlib  (pip3 install matplotlib)
# instalar IPython (pip3 install IPython)
# instalar scikit-learn (pip3 install scikit-learn)

'''
    Etapas de Data Science 

    1. Definir el problema ( que queremos estimar o predecir)
    2. Adquirir y preparar los datos (que recursos tenemos para obtener los datos)
    3. Explorar los datos (visualizar los datos, Localizar posibles tendencias)
    4. Modelar los datos (crear un modelo que se ajuste a los datos y evaluarlo)
    5. Resultados ( que resultados hemos obtenido y que podemos hacer con ellos)
    
'''

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

