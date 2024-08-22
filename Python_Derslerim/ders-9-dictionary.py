plakalar = {'kocaeli' : 41 , 'istanbul' : 34}

print(plakalar['istanbul'])
print(plakalar['kocaeli'])

plakalar['ankara'] = 6

print(plakalar)

users = {  'hasan' : { 'age' : 20, 'region' : 'Istanbul', 'email' : 'hasan@gmail.com', 'number' : 123  },
           'necmi' : { 'age' : 30, 'region' : 'Kocaeli', 'email' : 'necmi@gmail.com', 'number' : 456  },
           'selami' : { 'age' : 40, 'region' : ['Ankara', 'Muş'], 'email' : 'selami@gmail.com', 'number' : 789  }
        }
print(users['hasan'])
print(users['necmi']['age'])
print(users['selami']['region'][0])