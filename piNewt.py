from datetime import datetime
startTime = datetime.now()

n = 0
p = float(0)
s = -1

while n < 100000000:
    m = s**n
    f = float(1/(2*n + 1))
    p = p + m*f

    n = n + 1

i = float(p*4)

print(datetime.now() - startTime)
#print(i)
