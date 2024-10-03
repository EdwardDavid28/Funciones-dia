import math
#Ejemplo para calcular el area del triangulo
from array import array

#Variables de entrada
base =int(input("ingrese la base: "))
altura =int(input("ingrees la altura: "))

#Proceso
def calcularAreatriangulo(b,a):
    area=(b*a)/2
    return area

#invocar la funcion
resultado=calcularAreatriangulo(base,altura)

#salida
print(f"El area del triangulo cuya base {base} y altura {altura} es: {resultado}")

#Funcion con argumentos predeterminado
def myfunction(country ="Colombia"):
    print("Yo soy de "+country)

#Invocar la funcion
myfunction()
myfunction("Suiza")
myfunction("Polonia")
myfunction("EEUU")
myfunction("Brazil")

#Argumentos arbitrarios
def mostrarEstudiantes(*args):
    print("El estudiante: "+args[2])

#Invocamos la funcion
mostrarEstudiantes("emil","tobias","linus")

#
def mostrarCarros(carro1,carro2,carro3):
    print("El carro es: "+carro2)

mostrarCarros(carro1="bmw",carro3="Ferrari",carro2="Ford")

def mostrarCliente(**kwargs):
    print("Su apellido es: "+kwargs["apellido"])

mostrarCliente(nombre="tobias",apellido="Refsnes")

def miFuncion():
    pass


x=min(5,10,25)
y=max(5,10,25)
print(x)
print(y)

num1=pow(7,4)

print(num1)

num2=math.sqrt(34)
print(num2)

#redondea hacia arriba
num3=math.ceil(7.8)
#redondea hacia abajo
num4=math.floor(7.8)

print(num3)
print(num4)