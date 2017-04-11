f = open("temp")
file1 = f.readlines()

for i in range(len(file1)):
    for j in range(len(file1[i])):
        if file1[i][j] == '(':
            s1 = file1[i][0:j+1]
            s2 = "3"
            s3 = file1[i][j+1:len(file1[i])]
            file1[i] = s1 + s2 + s3
            break

fl = open('temp2', 'w')
for i in file1:
    fl.write(i)
fl.close()
