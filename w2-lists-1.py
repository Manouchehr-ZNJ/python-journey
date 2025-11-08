fruits=['apple','orange']
quiz=True
while (quiz):
    question=input('add remove exit show : ')
    if(question=='exit'):
        quiz=False
    if(question=='remove'):
        print(fruits)
        removeFruit=input('which fruit: ')
        fruits.remove(removeFruit)
        print(fruits)
        removeFruit=''
    if(question=='add'):
        newFruit=input('new fruit : ')
        if(len(newFruit)>1):
            fruits.append(newFruit);
            newFruit=''
            print(fruits)
    if(question=='show'):
        print(fruits)



                