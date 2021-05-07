while True:
    data = input("Input data Trunk interfaces baru (yes/no)? : ")
    if data == "no":
        file=open("db-interfaces.txt","r")
        for item in file:
            print(item)
        file.close()
        break
    
    if data == "yes":
        file=open("db-interfaces.txt","a")
        switch = input("Masukkan Hostname Switch : ")
        interfaces = input("Masukkan Nama Interfaces : ")
    file.write("Hostname Switch :" + switch + ", Nama Interfaces :" + interfaces +"\n")
file.close()