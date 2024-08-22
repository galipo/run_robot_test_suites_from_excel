#map metodu#
"""def square(num):
    return num**2

numbers = [1,3,5,9]
                                  #map() metodu ya list ile beraber ya da bir for döngüsünde kullanılabilir.    
                                
result = list(map(square,numbers))   #list() ile kullanımı.
print(result)

for item in map(square,numbers):     #for loop ile kullanımı.
    print(item)

res = list(map(lambda num:num**2, numbers))   #lambda ile square kllanmadan aynı sonuç.
print(res)"""

def check_even(num): return num%2==0

numbers= [1,3,5,9,10,4]
result = list(filter(check_even,numbers))

print(result)

numbers= [1,3,5,9,10,4]
