4. 
a)
recursion definition:
base cases - (j = 0) or (i =  j)
C(i,j) = C(i-1,j-1) + C(i-1,j) for  i>j>0

B)


define pascal(row,col):
    if (col is 0 or row = col):
        return 1
    else:
        return pascal(row - 1, col)+ pascal(row - 1, col - 1)

C)

for row in range(1, n + 1):
    value = 1
    for col in range(1, row + 1):
        print value # do not create new line, this should all be on same row
        value = (value*((row-i)/i))
    print("") #create new line


