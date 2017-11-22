data = [3,1,4,2,5]


for j in range(1,len(data)):
    key = data[j]
    i = j-1
    while i >= 0 and data[i] > key:
        data[i+1] = data[i]
        i = i - 1
    data[i+1] = key
print("insertion sort")
print(data)

# invert insertion sort
for j in range(1, len(data)):
    key = data[j]
    i = j-1
    while i >=0 and data[i] < key:
        data[i+1] = data[i]
        i = i-1
    data[i+1] = key
print("invert insertion sort")
print(data)