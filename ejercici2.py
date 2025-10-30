#ejercicio 2 
def invertir_array(lista):
    return lista[::-1]

cantidad = int(input("cuantos elementos tendra array? "))
     
array = []

for i in range (cantidad):
   valor= input(f"escribe el valor {i + 1}: ")
   array.append(valor)

print("Array original:", array)

array_invertido = invertir_array(array)
print("Array invertido:", array_invertido)

