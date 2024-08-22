"""""       TYPE DEF of VARIABLES
x = 5         #int
y = 2.5       #float
z = 'rakam'   #str
w = True      #bool

print(type(x))
print(type(y))
print(type(z))
print(type(w))

"""
""""        CONVERTING TYPE of VARIABLES
x = 5         #int
y = 2.5       #float
z = 'rakam'   #str
w = True      #bool

print(float(x))       #convert int to float
print(int(y))         #convert float to int

"""
#örnek: terminalden bir yarıçap değeri al ve dairenin alanı ve çevresini hesapla.(alan:pi*r^2  ,  çevre:2*pi*r  , pi=3.14)

pi = 3.14
print("please enter a value")
r = float(input())
alan = pi*r**2
cevre= 2*pi*r

print("alan=" , alan)
print("çevre="  ,cevre)
