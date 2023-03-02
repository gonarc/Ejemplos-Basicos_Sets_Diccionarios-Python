"""
Sets: Son una colección unica y desordenada de datos, en la cual solo se puede hacer una sola representación del mismo elemento.
Se utilizan las {} para declararlas.
"""

equipos_de_futbol={'Boca','River','Independiente','Racing'}

print(equipos_de_futbol)#{'River', 'Independiente', 'Boca', 'Patronato'}

#Añadir elementos al set con .add("elemento")
equipos_de_futbol.add("Patronato")
print(equipos_de_futbol)#{'River', 'Independiente', 'Boca', 'Patronato'}

#Eliminar elementos al set con .remuve("elemento")
equipos_de_futbol.remove("Racing")
print(equipos_de_futbol) #{'River', 'Independiente', 'Boca', 'Patronato'}

