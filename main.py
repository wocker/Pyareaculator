import math
print "Pyareacalculator: Calcula el area de una figura geometrica\n"
print "Que area deseas calcular \n"
 
opcion = "z"
while opcion != "a"  and opcion != "b":
        print "a) El area de un triangulo"
        print "b) El area de un circulo"
       
        opcion = raw_input("Elige la figura geometrica:\n")
        if opcion == "a":
			base_triangulo = float(raw_input("Introduzca la base:"))
			altura_triangulo = float(raw_input("Introduzca la altura:"))
			area_triangulo = base_triangulo * altura_triangulo / 2.0
			print area_triangulo
        elif opcion == "b":
			radio_circulo = float(raw_input("Introduzca el radio:"))
			area_circulo = radio_circulo * 3.1416
			print area_circulo
        else:
			print "Por favor elige una figura geometrica"
 #Comentario
 
