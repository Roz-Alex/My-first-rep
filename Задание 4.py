def linesearch(arr, element):
    index = []
    for i in range (len(arr)):
        if arr[i] == element:
            index.append(i)
    if not index : 
        index.append (-1)
    return index

a = open ('input.txt')
lines = a.readlines()
number = int(lines[3])
a.close
arr = list(map(int, lines [4].split()))

if len(arr) <= 1000:
    ind = (linesearch (arr, number))
else:
    print ('Error')
out = ' '.join(str(e) for e in ind)
with open ('output.txt', 'wt') as f:
    f.write(out)