# for x in range(1,5) :
#     for y in range(1,6) :
#         print("*", end="")
#     print()
    
    
# for a in range(1,21) :
#     for b in range(1,21) :
#         print(a*b, end=" ")
#     print("\n")
        
# for x in range(1,6) :
#     for y in range(1,x+1) :
#         print("*", end=" ")
#     print('')  


# for x in "banana":
#   print(x)

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y) 

# txt = f"The price is 49 dollars"
# print(txt)

# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# txt = f"The price is {95:.2f} dollars"
# print(txt)

# username = input("Enter username:")
# print("Username is: " + username)

#What a lambda returns


# price = 59
# tax = 0.25
# txt = f"The price is {price+(price * tax)}"
# print(txt)

# z1 = int(2.15)
# z2 = str(price)
# print(z1)
# print(z2)
# print(type(z2))

# my_List1 = ["BMW","Ford","Peugeot"]
# my_List2 = [1,10,125]
# my_List3 = ['a','v','x']
# my_List4 = [True,True,False,False,False,True]

# print(len(my_List1))
# print(len(my_List2))
# print(len(my_List3))
# print(len(my_List4))

# my_NestedList = [1,2,["abc","cba"]]
# print(my_NestedList)


# My_New_List = [[10,2008,1998],["Frank","Julia"],[True,False,False,True]]

# print(My_New_List)
# print(My_New_List[0][2])
# print(My_New_List[1][1])
# print(My_New_List[2][3])



# def my_Function_Sum(a,b):
#     wynik = a + b
#     return wynik

# wynik = my_Function_Sum(10,20)
# print(wynik)

# def ulamek(licznik,mianownik):
#     if mianownik == 0: return "Przez 0 nie dzielimy"
#     else: return float(licznik/mianownik)

# print(ulamek(1,100))

# def silniaa(n):
#     if n == 0: return 1
#     else: return n*silniaa(n-1)

# print(silniaa(10))

# def silniarekurencyjnie(n):
#     if n == 0:
#         return 1
#     else:
#         return n * silniarekurencyjnie(n-1)

# # Przykład użycia
# print(silniarekurencyjnie(5))  # Wyświetli 120



# def silnia_rekur(n):
#     if n == 0: return 1
#     else: return n*silnia_rekur(n-1)
    
# print(silnia_rekur(12))    

# def poww(liczba):
#     return liczba ** 2

# print(poww(30))

# def potegowanie(podstawa,potega):
#     if potega == 0:
#         return 1
#     elif potega < 0:
#         return 1/potegowanie(podstawa,-potega)
#     else: 
#         return podstawa*potegowanie(podstawa,potega-1)
    
# print(potegowanie(3,4))


# def pierwiastkowanie(podstawa,stopien):
#     if podstawa == 1:
#         return 1
#     elif podstawa < 0:
#         return 0
#     else: return podstawa ** (1/stopien)
    
# print(pierwiastkowanie(9,2)) 

for x in range (1,5):
    for y in range (1,5):
        print(y,end="")
        
    print()      

       
       
       