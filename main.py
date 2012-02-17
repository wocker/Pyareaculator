import math
print "Pyareacalculator: Calcula el area de una figura geometrica\n"
print "Que area deseas calcular \n"
#Defino la variable opcion con el valor de string z
opcion = "z"
#Inicio un while para que el usuario ingrese la opcion
while opcion != "a"  and opcion != "b":
		print "a) El area de un triangulo"
		print "b) El area de un circulo"
		print "c) El area de un rectangulo"
		print "d) El area de un Paralelogramo"
		opcion = raw_input("Elige la figura geometrica:\n")
        
		if opcion == "a":
			base_triangulo = float(raw_input("Introduzca la base:"))
			altura_triangulo = float(raw_input("Introduzca la altura:"))
			area_triangulo = base_triangulo * altura_triangulo / 2.0
			print "El area del triangulo es:", +area_triangulo
			
		elif opcion == "b":
			radio_circulo = float(raw_input("Introduzca el radio:"))
			area_circulo = radio_circulo * 3.1415926535897932384626433832795
			print "El area del circulo es:", +area_circulo
			
		elif opcion == "c":
			base_rectangulo = float(raw_input("Introduzca la base:"))
			altura_rectangulo = float(raw_input("Introduzca la altura:"))
			area_rectangulo = base_rectangulo * altura_rectangulo
			print "El area del rectangulo es:", +area_rectangulo
			
		elif opcion == "d":
			base_paralelogramo = float(raw_input("Introduzca la base:"))
			altura_paralelogramo = float(raw_input("Introduzca la altura:"))
			area_paralelogramo = base_paralelogramo * altura_paralelogramo
			print "El area del paralelogramo es:", +area_paralelogramo
