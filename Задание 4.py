import time
t_start = time.perf_counter()

def linesearch(arr, element):
    index = []
    for i in range (len(arr)):
        if arr[i] == element:
            index.append(i)
    if not index : 
        index.append (-1)
    return index

arr = [1, 2, 3, 4, 5, 2, 1]
a = open ('input4.txt')
arr = a.readline()
a.close
arr = list(map(int, arr.split()))

with open('input4.txt') as rd:
    for i in range(1):
        next(rd)
    number = int(next(rd))
if len(arr) <= 1000:
    ind = (linesearch (arr, number))
else:
    print ('Error')
out = ' '.join(str(e) for e in ind)
with open ('output4.txt', 'wt') as f:
    f.write(out)

print("Время работы: %s секунд " % (time.perf_counter() - t_start))