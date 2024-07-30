"""  METHODS OF STRING    """
message = 'Hello There. My name is Fatih Topal.'

#message = message.upper()            #Tüm harfleri büyük harfe dönüştürür.
#message = message.lower()            #Tüm harfleri küçük harfe dönüştürür.
#message = message.title()            #Kelimelerin baş harflerini büyük yazar.
#message = message.capitalize()       #Sadece baştaki harfi büyütür.
#message = message.strip()            #String'in başına boşluk getirir.

#message = message.split()            #String'deki her bir kelimeyi ayırarak diziye dönüştürür.
#message = message.split('.')         #String'deki noktaya kadar olan her bir cümleyi ayırarak diziye dönüştürür.
#message = '*'.join(message)          #Dizideki her bir elemanı birleştirerek aralarına "*" koyar.

#index = message.find('Fatih')        #String içerisindeki "Fatih" in kaçıncı indexte başladığını söyler.Eğer kelime yoksa "-1" döndürür.
#isFound = message.startswith('H')    #String "H" ile mi başladığını söyler.
#isFound = message.endswith('.')      #String "." ile mi bittiğini söyler.

#message = message.replace('Fatih','Hasan')     #"Fatih" yerine "Hasan" yazdırır.
#message = message.center(50,'*')               #50 karakterlik boşluğun merkezine String'i yazdırır, boşlukları'*' ile doldurur.

print(message)