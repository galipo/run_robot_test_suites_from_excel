names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998,2000,1998,1997]

names.apend('Cenk')      #"Cenk" ismini listenin sonuna ekler.
names.insert(0,'Sena')   #"Sena" ismini 0. indexten önce ekler.
names.remove('Deniz')    #"Deniz" elemanını kaldırır.
names.pop(1)             #Listenin 2. elemanını kaldırır.
names.index('Deniz')     #"Deniz" elemanının index numarasını verir.
result = 'Ali' in names  #"Ali" listede bulunuyorsa, result'a True değerini atar.
names.reverse()          #Liste elemanlarını ters çevirir.
names.sort()             #Liste elemanlarını alfabetik bir şekilde sıralar.
years.sort()             #Liste elemanlarını küçükten büyüğe şeklinde sıralar.
min(years)               #Listenin en küçük sayısını verir.
max(years)               #Listenin en büyük sayısını verir.
years.count(1998)        #Listede kaç adet "1998" elemanı sayısını verir.
years.clear()            #Listeyi temizler.