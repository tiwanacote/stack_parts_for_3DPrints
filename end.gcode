M140 S0
M141 S0
M107
M107                             ; Fan off
G90 			; Set to absolute positioning
G1 X0 Y0 Z201		; Get extruder out of way
G92 E0			; Reset extruder position
G1 E-1 			; Reduce filament pressure
G92 E0 			; Reset extruder position again
M140 S0 			; Disable heated bed
M104 S0 			; Disable extruder
M84 			; Turn steppers off

M117 Impresion finalizada
M82 ;absolute extrusion mode
M104 S0
;End of Gcode

