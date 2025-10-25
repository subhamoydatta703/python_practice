word=input("Enter the word: ")
s=len(word)
word=word.lower()
name=[]
while(s-1)>=0:
    name.append(word[s-1])
    s=s-1
name=''.join(name)
if(word==name):
    print("palindromic word")
else:
    print("not palindromic word")