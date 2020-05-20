n = int(input("How many terms?"))
f1 = 0
f2 = 1
count = 0

if n == 1:
   print(f1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(f1)
       t = f1 + f2
       # update values
       f1 = f2
       f2 = t
       count += 1
