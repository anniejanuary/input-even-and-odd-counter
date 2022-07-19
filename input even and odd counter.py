list=[] #lista niezdefiniowana
i=0 #początkowy indeks licznika od którego będzie liczyć

while i<5:
    entered_number=int(input("Podaj liczbę "))
    list.append(entered_number)
    i+=1
    
print(list)

#resetuje licznik, bo wyżej się powiększał:
i=0 
even_counter=0
odd_counter=0

while i<5:
    if list[i]%2==0:
        even_counter+=1
    else:
        odd_counter+=1
    i+=1
        
print(f"There are {even_counter} even numbers")
print(f"There are {odd_counter} odd numbers")
