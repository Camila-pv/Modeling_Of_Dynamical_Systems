import pandas as pd
import datatable as dt
import time

def primeNumber(number):
    count =0;
    for i in range(2,number):
        if (number%i) == 0:
            count = count +1
        
    if(count == 1):
        print("El numero es primo")
    else:
        print("El numero no es primo")
    

def compareTime():
    inicio = time.time()
    time.sleep(1)
    df = pd.read_csv("archivo.txt")
    print(df.to_string()) 
    
    fin = time.time()
    print(fin-inicio)
    
    inicio = time.time()
    time.sleep(1)
    df= dt.fread("archivo.txt")
    print(df.to_string()) 
    
    fin = time.time()
    print(fin-inicio)
    
    

    
    
number = 8
primeNumber(number)
compareTime()
