"""                        STRINGS   
name = 'Fatih'
surname = 'Topal'
age = 23
cumle = 'My name is ' + name + ' ' + surname + ' and\nI am ' + str(age) + ' years old.'
length = len(cumle)

print(cumle)
print(cumle[0])           #String'in 1. karakterinin bastırır.
print(cumle[4])           #String'in 5. karakterinin bastırır.
print(len(cumle))         #String'in uzunluğunu verir.
print(cumle[length-1])    #String'in son karakterini bastırır.
print(cumle[-1])          #String'in son karakterini bastırır.
print(cumle[3:8])         #String'in 3. karakterinden itibaren 8. karaktere kadar bastırır.
print(cumle[:8])          #String'in başından itibaren 8. karaktere kadar bastırır.
print(cumle[27:])         #String'in 27. karakterinden itibaren son karaktere kadar bastırır.
print(cumle[2:40:3])      #String'in 2. karakterinden 40. karaktere kadar iki karakter atlayarak bastırır.
"""

"""                        FORMAT 
name = 'Fatih'
surname = 'Topal'

print('My name is {} {}'.format(name,surname))
print('My name is {1} {0}'.format(name,surname))
print('My name is {n} {s}'.format(n=name,s=surname))
print('My name is {} {} and I am {} years old.'.format(name,surname,'23'))

result = 200/700
print('the result is {r:1.0}'.format(r=result))
"""

"""                        F FORMAT
name = 'Fatih'
surname = 'Topal'
age = 23

print(f"My name is {name} {surname} and I'm {age} years old.")
"""