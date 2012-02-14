#Importa el modulo math de Python
import math
#Imprimo el titulo de la aplicacion
print "Pyareacalculator: Calcula el area de una figura geometrica\n"
#Imprimo el subtitulo de la pregunta
print "Que area deseas calcular \n"
#Defino la variable opcion con el valor de string z
opcion = "z"
#Inicio un while para que el usuario ingrese la opcion
while opcion != "a"  and opcion != "b":
		#Imprimo la opcion del area de un triangulo
        print "a) El area de un triangulo"
        #Imprimo la opcion del area de un triangulo
        print "b) El area de un circulo"
        #Formulario para que los usuarios ingresen la figura geometria de la que desean sacar el area
        opcion = raw_input("Elige la figura geometrica:\n")
        #Hago la comprobacion si el usuario ingreso la opcion a
        if opcion == "a":
			#Formuario para que los usuarios ingresen la base del triangulo
			base_triangulo = float(raw_input("Introduzca la base:"))
			#Formulario para que los usuarios ingresen la altura del triangulo
			altura_triangulo = float(raw_input("Introduzca la altura:"))
			#Defino la variable area_triangulo que es la base_triangulo por la altura_triangulo entre dos
			area_triangulo = base_triangulo * altura_triangulo / 2.0
			#Imprimo la variable area_triangulo
			print area_triangulo
		#Hago la comprobacion si el usuario ingreso la opcion b
        elif opcion == "b":
			#Formulario para que los usuarios ingresen el radio del circulo
			radio_circulo = float(raw_input("Introduzca el radio:"))
			#Defino la variable area_circulo que calcula el area del circulo basado en el radio_circulo por la constante pi
			area_circulo = radio_circulo * 3.1416
			#Imprimo la variable area_circulo
			print area_circulo
		#Si la opcion ingresada por el usuario no es ni a ni b, hacemos dicha comprobacion
        else:
			#Imprimo un mensaje para los usuarios que no ingresaron ninguna opcion valida
			print "Por favor elige una figura geometrica"
#Fin del programa
 
