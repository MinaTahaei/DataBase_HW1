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
     with open ('books.txt', 'a+') as RM:
         line = RM.readlines()
         for lines in line:         
             if(Tmp3[0] ==  )

        

# def updateBook (userInput):
# def addPublisher(userInput):
# def findPublisher(userInput):
# def removePublisher (userInput):
# def updatePublisher (userInput):


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
    






