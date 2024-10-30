
x = int(input("Enter a number: ")) 
 
for i in range(1, x + 1):  
    if i % 3 == 0 and i % 5 == 0:
        print(i) 
        break  
else:
    
    print("There are no numbers divisible by both 3 and 5")

