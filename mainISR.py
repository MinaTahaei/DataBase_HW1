def addBook (userInput):
    Tmp = userInput.split(' , ')
    Tmp[0] = Tmp[0][10:]
    with open('books.txt', 'a+') as RW:
      numLines = sum(1 for line in open('books.txt')) 
      count = numLines - 1
      RW.write(str(count) + '-')
      for item in Tmp:
         RW.write(item + '/ ')
      RW.write('\n')

def findBook (userInput):
    Tmp = userInput.split(' by ')
    Tmp[0] = Tmp[0][10:]
    # print(Tmp[0]):the real search part
    # print(Tmp[1]):the general search part
    with open ('books.txt', 'a+') as RF:
        line = RF.readlines()   
        for lines in line:
            Tmp2 = line.split('/')
            Tmp2[0] = Tmp2[0][2:]
            for i in range(0, 6):   
                bmp[i] = Tmp2[i].split(':')
                
             

def removeBook (userInput):
         Tmp3 = userInput.split(' ')
         Tmp3[0] = Tmp3[0][12:]
         with open ('books.txt', 'r') as RM:
             lines = RM.readlines()
             for line in lines:         
                 if(Tmp3[0] == line[0]):
                     RM.close()
                     with open ('books.txt', 'w') as RM:
                         for line in lines:
                             if(line[0] != Tmp3[0]):
                                 RW.write(line)

              
# def updateBook (userInput):


def addPublisher(userInput):
    Tmp = userInput.split(' , ')
    Tmp[0] = Tmp[0][14:]
    with open('Publisher.txt', 'a+') as RW:
      numLines = sum(1 for line in open('Publisher.txt')) 
      count = numLines - 1
      RW.write(str(count) + '-')
      for item in Tmp:
         RW.write(item + '/ ')
      RW.write('\n')

# def findPublisher(userInput):
# def removePublisher (userInput):
# def updatePublisher (userInput):

print('Press the required keys to use different parts of the program')
print('(A)ddBook,(F)indBook,(R)emoveBook,(U)pdateBook,(A)dd(P)ublisher,(F)ind(P)ublisher,(R)emove(P)ublisher,(U)pdate(P)ublisher')
Input = input()
if (Input == 'A'):
    print('Enter the info of the book you want to add')
    userInput = input()
    addBook(userInput)

if (Input == 'F'):
    print('Enter the info of the book you want to find')
    userInput = input()
    findBook(userInput)

if (Input == 'R'):
    print('Enter the info of the book you want to remove')
    userInput = input()
    removeBook(userInput)

if (Input == 'U'):
    print('Enter the info of the book you want to update')
    userInput = input()
    updateBook(userInput)

if (Input == 'AP'):
    print('Enter the info of the publisher you want to add')
    userInput = input()
    addPublisher(userInput)

if (Input == 'FP'):
    print('Enter the info of the publisher you want to find')
    userInput = input()
    findPublisher(userInput)

if (Input == 'RP'):
    print('Enter the info of the publisher you want to Remove')
    userInput = input()
    removePublisher(userInput)

if (Input == 'UP'):
    print('Enter the info of the publisher you want to Update')
    userInput = input()
    updatePublisher(userInput)
