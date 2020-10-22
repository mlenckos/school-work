def pascal_triangle(n):  
    for row in range(1, n+1):  
        C = 1; # used to represent C(line, i)  
        for i in range(1, row+1):  
              
            # The first value in a  
            # line is always 1  
            print(C, end = " ");  
            C = int(C * (row - i) / i);  
        print(" ");  

n=5 
pascal_triangle(n)


for row in range(1, n + 1):
    value = 1
    for col in range(1, row+1):
        print value # do not create new line, this should all be on same row
        value = (value*((row-i)/i))
    print("") #create new line
