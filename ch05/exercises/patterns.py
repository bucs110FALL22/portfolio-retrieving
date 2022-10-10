y = int(input("Enter the number of rows: "))  



def star_pyramid(y):
     
    
    for i in range(0, y):
     
        
        for i in range(0, i+1):
                                 
          print("* ", end="")
      
        
        print("\r")
 


star_pyramid(y)


for i in range(y+1, 0, -1):
   
    for i in range(0, i-1):
        
      print("*", end=' ')
    print(" ")