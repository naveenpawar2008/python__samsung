import sys

input_number=int(sys.argv[1])

for i in range(1,input_number+1):
    for j in range(1,input_number+1):
        if i==1 or j==input_number-1+1:
           print ('*',end =' ')
        else:
           print (' ',end =' ')