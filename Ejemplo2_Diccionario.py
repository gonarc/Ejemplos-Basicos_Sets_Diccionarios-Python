"""
Los Diccionarios son mapeos desordenados que guardan objetos.
Utilizan un orden en par Clave/Valor:
diccionario= {
    'manzanas':'300',
    'banana':'350',
    'anana':'500'
}

Es obligatorio que la clave y el valor esten entre comillas.
*Se utilizan los diccionarios cuando sabemos la clave pero no el orden o la ubicacion de cada uno.

"""

frutas = {
    'manzanas': '300',
    'banana': '350',
    'anana': '500'
}

print(frutas)
print(type(frutas))

# Diccionarios Multidimensionales con [{'',''},{'',''}]
personas = [
    {
        'Nombre': 'Gonzalo',
        'Apellido': 'Arce'
    },
    {
        'Nombre': 'Maxi',
        'Apellido': 'Rodriguez'
    },
    {
        'Nombre': 'Sol',
        'Apellido': 'Luna'
    },
    {
        'Nombre': 'Camila',
        'Apellido': 'Quipildor'
    },
    {
        'Nombre': 'Maria',
        'Apellido': 'Pavon'
    }
]

print(personas)
print(type(personas))

# Encontrar clave y sacar su valor:
# print(persona[index]["clave"])
# importante: la clave o el valor deben estar escritos igual que en el diccionario.
print(personas[0]["Apellido"])
print(personas[3]["Nombre"])

print("\n Listado de Personas")

for contador in personas:
    print(contador)

print("\n Listado de Personas[Apellidos]")

for claves in personas:
    print(claves['Apellido'])

print("\n Listado de Personas [Nombres] y [Apellidos]")
for contador2 in personas:
    print(f"Su nombre es: {contador2['Nombre']}")
    print(f"Su apellido es: {contador2['Apellido']}")
    print("\n")
