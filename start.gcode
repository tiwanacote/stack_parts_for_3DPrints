M82 ;absolute extrusion mode
;Start GCode - Cosmos II - 1.0_SEGTK

M104 S120				;Comienzo a calentar extrusor				;Unidades en mm
G90        			;absolute positioning
M82        			;set extruder to absolute mode
M107      				;Apagar FAN
G28 X Y Z  			;Home

M190 S60

G29			;Senso la cama
G1 F5000 X0.5 Y0.5

M109 S210

G0 Z10
G92 E0               		;Defino cero en la posición del actual del extrusor
G1 F900 X0.5 Y0.5 Z0.300	;Posiciono antes de hacer una línea
G1 F900 X0.5 Y51.5 E2.56436	;Hago una línea

M117 Printing...
M141 S28
G92 E0
G92 E0
