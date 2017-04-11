import os

f = open("layout.html")
file1 = f.readlines()

def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        return files

files = file_name("/home/mihawk/Desktop/wav/test_eval92/1")
files.sort()
print files
k = 0
for i in range(len(file1)):
    for j in range(len(file1[i])-3):
        if file1[i][j] == 'w' and file1[i][j+1] == 'a' and file1[i][j+2] == 'v':
            s1 = file1[i][0:j-10]
            s2 = files[k]
            k = k + 1
            s3 = file1[i][j+3:len(file1[i])]
            file1[i] = s1 + s2 + s3
            break

f.close()
fl = open('layout.html', 'w')
for i in file1:
    fl.write(i)
fl.close()
