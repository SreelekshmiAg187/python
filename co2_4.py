import math
for i in range(1000, 10000):
     squreroot=int(math.sqrt(i))
     if (squreroot * squreroot==i):
         if all (int (digit)%2==0  for digit in str(i)):
                 print(i)
          
