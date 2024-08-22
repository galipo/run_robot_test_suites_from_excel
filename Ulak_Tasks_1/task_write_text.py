f = open("ArgumentFile.txt","w")     #opening for writing the file
f.write("deneme 1")                  #writing into the file
f.close()                            #closing to the file

f = open("ArgumentFile.txt", "r")    #After opening for reading
print(f.read())                      #Reading to the file

