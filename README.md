# stack_parts_for_3DPrints
Este programa permite ingresar un códigoG de una pieza para ser impresa 3D apilada una sobre otra y de este modo aumentar la productividad. Fue desarrollado por TRIMAKER a fin de poder imprimir máscaras para el COVID de forma rápida.


This program allows you to enter a G-code of a part to be 3D printed stacked on top of each other and thus increase productivity. It was developed by TRIMAKER to be able to print COVID skins quickly.

The problem is that CURA does not allow layers of 0.3mm and when it reaches the next piece that is stacked, leave a different distance, for example 0.15mm layer so that the two do not stick.

*************
Configuration:

OFFSET = 0.05	  								          Separation between pieces - FOR 0.4mm nozzle OFFSET = 0.26 GOES VERY WELL
ALTURA_PIEZA = 6								          It is the height of the individual piece to be stacked
QUANTITY = 2									            TOTAL amount to put in stack
NOMBRE_ARCHIVO_ENTRADA = 'CII_V8_06mm'		Input file name WITHOUT .gcode, WITHOUT StartCode & EndCode
*************
Usage:

From console, in the same folder were are the GCode and the "start.gcode" and end "end.gcode" files
"python offset4.py"
*************


*************
ESPAÑOL:

Este programa permite ingresar un códigoG de una pieza para ser impresa 3D apilada una sobre otra y de este modo aumentar la productividad. Fue desarrollado por TRIMAKER a fin de poder imprimir máscaras para el COVID de forma rápida.

El problema es que CURA no permite hacer capas de a 0.3mm y cuando llega a la siguiente pieza que está apilada, dejar una capa de otra medida, por ejemplo 0.15mm, para que las dos no se peguen.

*************
Configuración:

OFFSET = 0.05	  								          Separación entre piezas - PARA boquilla de 0.4mm OFFSET = 0.26 ANDA MUY BIEN
ALTURA_PIEZA = 6								          Es la altura de la pieza individual a apilar
QUANTITY = 2								            	Cantidad TOTAL a poner en pila
NOMBRE_ARCHIVO_ENTRADA = 'CII_V8_06mm'		Nombre del archivo de entrada SIN .gcode
*************

Este programa te permite que le ingreses un códigoG SIN StartGcode NI EndGcode - Que van en dos archivos aparte en la misma carpeta y la altura de capa, el offset entre piezas y la cantidad. Con todos estos datos la salida es: La pieza ingresada apilada por la cantidad de veces ingresada con la separación puesta.

El archivo de salida tiene el mismo nombre que el de entrada, pero se le agrega_MODIF y se guarda en la misma carpeta.

***********************************************************************************************************************************
Se llama desde la consola, en la carpeta donde está el programa y los codigosG de start, end y de la pieza con:  python offset4.py
***********************************************************************************************************************************
