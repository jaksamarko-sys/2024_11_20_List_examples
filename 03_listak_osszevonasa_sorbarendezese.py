"""
Hozz létre két listát: [3, 1, 4] és [9, 7, 2]. 
Egyesítsd a két listát, és rendezd a lista elemeit növekvő sorrendbe!
"""
lista1 = [3, 1, 4]
lista2 = [9, 7, 2]

lista1.extend(lista2)
lista1.sort()
# lista1.sort(reverse=False)
# lista1.sort(reverse=True)
print(lista1)

# írasd ki az első és az utolsó elemet!

print(lista1[0])
print(lista1[-1])