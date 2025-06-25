#Printing each character of the word "Factory" incrementally repeated on each line:
# F AA CCC TTTT OOOOO RRRRRR YYYYYYY

name = "Factory"
for i in range(len(name)):
    print (name[i] * (i+ 1))