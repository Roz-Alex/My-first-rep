a = open ('input.txt')
lines = a.readlines()
check = int(lines[0])
a.close
if check < 1000:
    arr = lines [1]
    arr = list(map(int, arr.split()))
    for i in range(1, check):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key 
    for j in range (check//2):
        arr[j], arr[-j-1] = arr[-j-1], arr[j]
    out = ' '.join(str(e) for e in arr)
    with open ('output.txt', 'wt') as b:
        b.write (out)
else:
    print ('Mistake')