import time
import random
import os 
secret_number=random.randint(1,9)
i=0
while i<3:
    Your_gues=int(input("Enter a number betwine 1 and 10 : "))
    
    if Your_gues==secret_number:
        print("good my man ")
        break
    else:
        i+=1
        if i<3:
            print("try Angin")
            print("1")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("3")
            A=3
            A-=i
            print("you have "+ str(A) + "Try Left ")

        elif i==3:
            print("Your pc will be destroid in ")
            print("1")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("3")
            time.sleep(1)
            os.system('Tree')
            time.sleep(1)
            os.system('Tree')
            os.system('cls')
            print(secret_number)


    

       
       