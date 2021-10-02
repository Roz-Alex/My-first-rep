a = open ('input.txt')
lines = a.readlines()
check = int(lines[0])
a.close
arr = list(map(int, lines [1].split()))

for i in range(check):
    for j in range(check-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
out = ' '.join(str(e) for e in arr)
with open ('output.txt', 'wt') as b:
    b.write (out)