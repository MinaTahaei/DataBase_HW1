def addBook (userInput):
    Tmp = userInput.split(' , ')
    Tmp[0] = Tmp[0][10:]
    with open('books.txt', 'a+') as RW:
        # for i in range (1, len(Tmp)):
        #     for item in Tmp:
        #      RW.write(str(i) + '-')
        #      RW.write(item + '/ ') 
        #      RW.write('\n')
     numLines = RW.readlines()
     count = len(numLines + 1)
    #  numLines = sum(1 for line in open('books.txt'))
     RW.write(str(count) + '-')
    for item in Tmp:
        RW.write(item + '/ ')
    RW.write('\n')

def findBook (userInput):
    Tmp = userInput.split(' by ')
    Tmp[0] = Tmp[0][10:]
    # print(Tmp[0]):the real search part
    # print(Tmp[1]):the general search part

def removeBook (userInput):
def updateBook (userInput):
def addPublisher(userInput):
def findPublisher(userInput):
def removePublisher (userInput):
def updatePublisher (userInput):


print('for adding books please press A and for Finding boks please press F')
Input = input()
if (Input == 'A'):
    print('Enter the info of the book you want to add')
    userInput = input()
    addBook(userInput)
if (Input == 'F'):
    print('Enter the info of the book you want to find')
    userInput = input()
    findBook(userInput)
    






