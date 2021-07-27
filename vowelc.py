#vowel count in the word and sentences after i got to know.....
l=['a','e','i','o','u']
w=len(l)
a=str(input("enter the string ")).lower()
count = 0
for i in range(0,len(a)):
    for j in range(0,w): 
        if (a[i] == l[j]):
            count=count+1
print("total count in the sentence in the word is ",count)