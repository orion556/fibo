"""hi there this is simple project of mine    this print first 10000 fibonacci numbers"""
fibo = [0,1,1]
n = raw_input("write number of numbers u want to get to")
print (0)
print (1)
print (1)


n = int(n)
for i in range (n):
    next_fibo = fibo[i+1]+fibo[i+2]
    print next_fibo
    fibo.append(next_fibo)

    

