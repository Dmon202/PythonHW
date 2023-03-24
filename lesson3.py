#6.4.1
def FindandIndexTask():
    text='<a href="https://developer.mozilla.org">MDN</a>'
    print( text[ text.index('href=')+6 : text.index('>')-1 ] )

#FindandIndexTask() #https://developer.mozilla.org

#6.4.2
def ReplaceTask():
    text = 'Лнепбблнепб гтьзу в ннепчнепле мнепя, кёгднеп весеннвый'
    text =text.replace('неп', 'а')
    text =text.replace('аб', 'ю')
    text =text.replace('ть', 'рё')
    text =text.replace('ё', 'о')
    text =text.replace('вы', 'и')
    print(text)

#ReplaceTask()  #Люблю грозу в начале мая, когда весенний

#6.4.3
def SplitTask():
    text="арбузы, черешня, яжевика, бананы, морковь, сыр"
    text = text.split(', ')
    for word in range(0,len(text)):
        if word != len(text):
            print(str(word+1)+'. '+text[word]+';')
        else:
            print(str(word+1)+'. '+text[word]+'.')

#SplitTask()
"""
1. арбузы;
2. черешня;
3. яжевика;
4. бананы;
5. морковь;
6. сыр;
"""

#6.4.4
def CountTask():
    text='халапеньо, длинношеее, хворост, змееед, Ыгыатта, воспользовавшемуся, апельсин'
    text= text.split(', ')
    i=0
    maxEEE=0
    while i<len(text):
        if text[i].count('е')>text[maxEEE].count('е'):
            maxEEE=i
        i+=1
    print(maxEEE+1)

#CountTask() #2

#6.4.5
def SaladCode(): # sorry for naming)
    print('Введите строчку: ')
    text=input()
    print('Введите число: ')
    n=int(input())
    ABC="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    ZYX=''
    i=0
    while i<len(text):
        if ABC.find(text[i])+n<len(ABC):
            ZYX+=ABC[ABC.find(text[i])+n]
        else:
            ZYX+=ABC[ABC.find(text[i])+n-len(ABC)]
        i+=1
    print(ZYX)

#SaladCode() #try yourself