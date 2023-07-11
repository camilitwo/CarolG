class Rectangulo:
    rectangulos = 0
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def area(self):
        return self.largo * self.ancho

    def perimetro(self):
        return 2 * (self.largo + self.ancho)
    
rectangulo = Rectangulo(10, 20)

#print("El área del rectangulo corresponde a:", rectangulo.area())
#print(rectangulo.perimetro())

# ejercicio genera la clase circulo que reciba radio, y quiero saber el diametro de la circuferencia
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def diametro(self):
        return self.radio * 2

circulo = Circulo(3)

#print(circulo.diametro())
#print("El diámetro del circulo dado es", circulo.diametro())

#ejercicio 3
# crear clase calculadora y que haga las 4 operaciones fundamentales"

class Calculadora:
    def suma(n1, n2):
        return n1 + n2
    def resta(n1, n2):
        return n1 - n2
    def multiplicacion(n1, n2):
        return n1 * n2
    def division(n1, n2):
        if n2 != 0:
            return n1/n2  
        return "indeterminada"
    def sumaLista(n):
        #return n[0]+n[1]+n[2]+n[3]+n[4]
        sum =0
        for num in n:
           sum += num
        return sum

    
calculadora = Calculadora

#print("la suma de estos números es", calculadora.suma(7,90))
#print("la diferencia de estos números es", calculadora.resta(10,40))
#print("la multiplicación de estos números es", calculadora.multiplicacion(3,5))
#print("la división de estos números es", calculadora.division(4,0))

#ejercicio 4
# crear una lista de n numeros, utilizando la misma clase calculadora para hacer la suma
listaNum = [78,9,7,-45,60,999]

#print ("la suma de los números dados en la lista es", calculadora.sumaLista(listaNum))

#crea la clase mascota que va a tener como atributo nombre, especie, dueño, edad. y que al registrar la mascota me retorne una lista de todas las mascotas que registre
import os
class Mascotas:
    def __init__(self, nombre, especie, dueño, edad):
        self.nombre = nombre
        self.especie = especie
        self.dueño = dueño
        self.edad = edad
        self.lista = []
    def registro(self, lista):
        self.lista = lista

    def imprimir(self, lista):
        for mascota in self.lista:
            print("\n\nMascotas registradas")
            print("Nombre:", mascota.nombre, "\nEspecie:", mascota.especie, "\nDueño:", mascota.dueño, "\nEdad:", mascota.edad)

#solicitar datos de la mascota
agr = True
lista = []
while agr:
    os.system("cls")
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    dueño = input("Ingrese el nombre del dueño de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ")
    #crear objeto mascota
    mascota = Mascotas(nombre, especie, dueño, edad)
    
    lista.append(mascota)
    mascota.registro(lista)
    print("¿Desea agregar otra mascota?")
    print("1. Si")
    print("2. No")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        agr = True
    else:
        #imprimir mascota
        mascota.imprimir(lista)
        agr = False
        break







     
    


    
