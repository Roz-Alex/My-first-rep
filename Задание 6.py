a = open ('input.txt')
lines = a.readlines()
check = int(lines[0])
a.close

for i in range(N):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)