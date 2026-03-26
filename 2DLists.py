rows = 3
cols = 3

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        if i == j:
            row.append(1)
        else:            
            row.append(0)
    matrix.append(row)
print(matrix)


rows = 4
cols = 4

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        if (i+j) % 2 == 0:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)
print(matrix)

rows = 5
cols = 5
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        if i == 0 or i == 4 or j == 0 or j == 4:
            row.append(1)
        else:
            row.append(0)
        matrix.append(row)
print(matrix)


rows = 3
cols = 3

matrix = []

for i in range(rows):
    row = []

    for j in range(cols):
        value = (i+j)*10
        row.append(value)

    matrix.append(row)

print(matrix)


row = []

for i in range(5):
    value = (5 - i)

    row.append(value)
print(row) 

rows = 3 
cols = 3
matrix = []

for i in range(rows):
    row = []

    for j in range(cols):
        value = 3 - j
        row.append(value)

    matrix.append(row)
print(matrix)


rows = 4
cols = 4

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        if (i+j) % 2 == 0:
            value = i+j
        else:
            value = 'Odd'
        row.append(value)

    matrix.append(row)

print(matrix)

rows = 4
cols = 4

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        if i == 0 or i == 3:
            value = 'Blank'
        else:
            value = j
        row.append(value)

    matrix.append(row)

print(matrix)


rows = 4
cols = 4

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        if j <= i:
            value = 1
        else:
            value = 0
        row.append(value)

    matrix.append(row)

print(matrix)


rows = 3
cols = 3

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        if (i+j) % 2 == 0:
            value = 'Black'
        else:
            value = 'White'
        row.append(value)
    
    matrix.append(row)

print(matrix)

#Lists comprehension

rows = 3
cols = 3
matrix = []
row = [['Black' if (i+j) % 2 == 0 else 'White' for j in range(cols)] for i in range(rows)]
matrix.append(row)
print(matrix)


rows = 4
cols = 4

matrix = []

row = [[1 if j<=i else 0 for j in range(cols)] for i in range(rows)]
matrix.append(row)
print(matrix) 

rows = 5

matrix = []

for i in range(rows):
    row = []
    for j in range(i+1):
        
        row.append(j)
    
    matrix.append(row)
print(matrix)

matrix = [[i for j in range(i + 1)] for i in range(5)]

print(matrix)


#Exercise 15
rows = 3
cols = 3
matrix =  [[j ** i for j in range(cols)] for i in range(rows)]

print(matrix)

#exercise 16
relist = [x if x%2 == 0 else 0 for x in range(10)]
print(relist)


#Exercise 17
list = [x**2 for x in range(11) if x % 2 == 0]
print(list)

#Exerxise 18
Identity = [[1 if j == i else 0 for j in range(4)] for i in range(4)]
print(Identity)


#Exercise 19
matrix = [[(i+j) if (i+j) != 4 else 'skip'for j in range(4)]for i in range(4) if i!=1]

flattened = [val for row in matrix for val in row]

print(flattened) 

matrix = [[i*j for j in range(3)] for i in range(3) if i> 0]
flattened = [val for row in matrix for val in row]
print(flattened)