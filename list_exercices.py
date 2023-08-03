import numpy as np
import random

# 1. Create a list of your favorite fruits.
frutas = ['fresa', 'banano', 'arandanos', 'durazno'];
# 2. Append a new fruit to the list.

nueva_fruta = 'manzana'
frutas.append(nueva_fruta)

# 3. Remove the second fruit from the list.
frutas.remove('banano')

# 4. Check if "banana" is in the list.
if 'banano' in frutas:
    print("Banano esta en la lista")
else:
    print("Banano no esta en la lista")

# 5. Loop through the list and print each fruit.
for i in frutas:
    print(i)

# 6. Create a list of numbers and find the average.
numeros = [2,6,8,4,1]
sum = 0 

for j in numeros:
    sum = sum + j
    
promedio = sum / len(numeros)

print(promedio)


# 7. Remove all duplicates from a list.
t = [3,6,7,6,8]
print(set(t))


# 8. Create a list of names and sort them alphabetically.
nombres = ['Camila', 'Juan', 'Ana', 'David','Maria']
nombres.sort()
print(nombres)

# 9. Find the second-largest number in a list.
nombre_largo = ''
for n in nombres:
    if( len(nombre_largo) < len(n)):
        nombre_largo = n
        
print(nombre_largo)

# 10. Create a list of words and capitalize the first letter of each.
palabras = ['carro', 'moto', 'helicoptero', 'avion', 'bicicleta']
cap = []
for c in palabras:
    cap.append(c.capitalize())
    
print(cap)
    
# 11. Create a list of numbers and find the median.
numeros.sort()
mediana  = np.median(numeros)

print(mediana)

# 12. Shuffle the elements of a list randomly.
random.shuffle(numeros)

print(numeros)

# 13. Create a list of strings and sort them based on their lengths.

        

# 14. Create a list of sentences and sort them based on the number of words.
# 15. Create a list of dates and sort them chronologically.
# 16. Implement a custom sorting algorithm to sort a list of numbers.
# 17. Implement matrix multiplication using nested lists (2D arrays).
# 18. Create a list of mathematical expressions and evaluate them using a custom function.
# 19. Create a list of words and generate an anagram for each word.






