a = open ('input.txt')
lines = a.readlines()
check = int(lines[0])
a.close
if check<1000:
    arr = lines[1]
    arr = list(map(int, arr.split()))
    for i in range (0, check-1):
        smallest = i
        for j in range (i+1, check):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    out = ' '.join(str(e) for e in arr)
    with open ('output.txt', 'wt') as b:
        b.write (out)
else:
    print ('Mistake')