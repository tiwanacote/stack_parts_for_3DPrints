#!/usr/bin/env python
# -*- coding: utf-8 -*-


# This program allows you to enter a G-code of a part to be 3D printed stacked on top of each other and thus 
# increase productivity. It was developed by TRIMAKER to be able to print COVID skins quickly.

# The problem is that CURA does not allow layers of 0.3mm and when it reaches the next piece
# that is stacked, leave a different distance, for example 0.15mm layer so that the two do not stick.

# Configuration:
# *************
# OFFSET = 0.05	  								Separation between pieces - FOR 0.4mm nozzle OFFSET = 0.26 GOES VERY WELL
# ALTURA_PIEZA = 6								It is the height of the individual piece to be stacked
# QUANTITY = 2									TOTAL amount to put in stack
# NOMBRE_ARCHIVO_ENTRADA = 'CII_V8_06mm'		Input file name WITHOUT .gcode, WITHOUT StartCode & EndCode
# 																				***************************
# Usage:
# *****
# From console, in the same folder were are the GCode and the "start.gcode" and end "end.gcode" files
# "python offset4.py"





# Este programa permite ingresar un códigoG de una pieza para ser impresa 3D apilada una sobre otra y de este
# modo aumentar la productividad. Fue desarrollado por TRIMAKER a fin de poder imprimir máscaras para el COVID de forma rápida.

# El problema es que CURA no permite hacer capas de a 0.3mm y cuando llega a la siguiente pieza
# que está apilada, dejar una capa de otra medida, por ejemplo 0.15mm, para que las dos no se peguen.

# OFFSET = 0.05	  								Separación entre piezas - PARA boquilla de 0.4mm OFFSET = 0.26 ANDA MUY BIEN
# ALTURA_PIEZA = 6								Es la altura de la pieza individual a apilar
# QUANTITY = 2									Cantidad TOTAL a poner en pila
# NOMBRE_ARCHIVO_ENTRADA = 'CII_V8_06mm'		Nombre del archivo de entrada SIN .gcode

# Este programa te permite que le ingreses un códigoG SIN StartGcode NI EndGcode - Que van en dos archivos aparte en la misma carpeta
# y la altura de capa, el offset entre piezas y la cantidad.
# Con todos estos datos la salida es: La pieza ingresada apilada por la cantidad de veces ingresada con la separación puesta.

# El archivo de salida tiene el mismo nombre que el de entrada, pero se le agrega_MODIF y se guarda en la misma carpeta.

# ***********************************************************************************************************************************
# Se llama desde la consola, en la carpeta donde está el programa y los codigosG de start, end y de la pieza con:  python offset4.py
# ***********************************************************************************************************************************

def main(args):
	
	
	import re
	
	# --------------------------------------------------------------------------------------------
	# Ingresar los siguientes datos:
	# --------------------------------------------------------------------------------------------
	
	OFFSET = 0.05									#Separación entre piezas - PARA boquilla de 0.4mm OFFSET = 0.26 ANDA MUY BIEN
	ALTURA_PIEZA = 6
	QUANTITY = 2									#Cantidad TOTAL a poner en pila
	
	NOMBRE_ARCHIVO_ENTRADA = 'CII_V8_06mm'			#Nombre del archivo de entrada SIN .gcode
	
	
	# --------------------------------------------------------------------------------------------
	
	
	
	
	NOMBRE_ARCHIVO_SALIDA  = NOMBRE_ARCHIVO_ENTRADA + "_0" + str(int(OFFSET*100)) + "mm" "_X" + str(QUANTITY) + "_MODIF.gcode"
	
	output_file = open(NOMBRE_ARCHIVO_SALIDA, "w")

	
	with open('start.gcode') as start_gcode:
		for line_sgcode in start_gcode:
			line_sgcode = line_sgcode.strip()
			output_file.write(line_sgcode + '\n')
		
		output_file.write(";----------------------------------------------------------" + '\n')

			
	for counter in xrange(0,QUANTITY):
		
		output_file.write("G92 E0" + '\n')
		
		#with open('gcode_example.gcode') as gcode:
		with open(NOMBRE_ARCHIVO_ENTRADA + ".gcode") as gcode:
	
		
			for line in gcode:
				
				#output_file.write('\n')
				line = line.strip()
				
				if line[:1]!=';':
					
					output_file.write('\n')
					print("-----------------------------------")
					print(line)
					words = str.split(line)
					
					for word in words:
						
					
						if word[:1]=='Z':
							number_string = word[1:]					    			#Le saco el "Z"
							z_value = float(number_string)								#Convierto el numero en string a numero float
							
							z_new_value = z_value + (OFFSET + ALTURA_PIEZA) * counter
								
							output_file.write("Z{}".format(z_new_value))
							output_file.write(" ")
							print("Z{}".format(z_new_value))
						
						else:
							print(word)
							output_file.write(word)
							output_file.write(" ")
						
							
				else:
					print(line)
					#output_file.write(line)
					output_file.write('\n')
					output_file.write(line + '\n')
					
				
				
				
				
				
				
 
	with open('end.gcode') as end_gcode:
		
		output_file.write(";----------------------------------------------------------" + '\n')
		
		for line_egcode in end_gcode:
			line_egcode = line_egcode.strip()
			output_file.write(line_egcode + '\n')
 
 
	output_file.close()
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
