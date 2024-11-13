object_list=[]
matched_words=[]
display_word=0

while display_word<10:
    word=input("Enter a word: ")
    object_list.append(word)
    display_word+=1
num=int(input("Enter a number: "))
for i in object_list:
    if len(i)>=num:
        matched_words.append(i)
print(matched_words)