import Books
import Publishers

BooksTemp = []
Publishers = []

def addBook (ISBN,BookName,Authors,Publisher,Subjects,PublishYear,PageNO):
    if len(str(ISBN) <= 20) and len(BookName) <= 200 and len(Authors) <= 200 and len(Publisher) <= 200 and len(Subjects) <=200 and len(str(PublishYear)) == 4 and PageNO < 10000:
         newBook = Books.Book(ISBN,BookName,Authors,Publisher,Subjects,PublishYear,PageNO)
         for Book in BooksTemp:
            if Books.ISBN == ISBN:
                return
    BooksTemp.append(newBook)
    counter = len(BooksTemp)
    info += str(counter) + "-"
    attsName = ["ISBN","BookName","Authors","Publisher","Subjects","PublishYear","PageNO"]
    attsValues = [ISBN,BookName,Authors,Publisher,Subjects,PublishYear,PageNO]
    info = ''
    for i in range(7):
         if i !=6:
                info += attsName[i]+':'+str(attsValues[i]) + '/'
         else:
                info += attsName[i]+':'+str(attsValues[i])
         with open('books.txt','a') as Writer:
            Writer.write(info + '\n')

def readBooks ():
    with open('books.txt','r') as RW:
       lines = RW.readlines()
    for attribute in lines:
        atts1 = []
        atts2 = []
        for item in attribute:
            count = item.index('-')
            info = item[count+1:]
            info = info.split('/')
        for item in info:
            att1,att2 = item.split(':')
        atts1.append(att1)
        atts2.append(att2)

        dictionary = dict(zip(atts1,atts2))
        createBooks(dictionary)

def createBooks (dictionary):
    ISBN = int(dictionary['ISBN'])
    BookName = dictionary['BookName']
    Authors = dictionary['Authors']
    Publisher = dictionary['Publisher'] 
    Subjects = dictionary['Publisher'] 
    PublishYear = int(dictionary['PublishYear'])
    PageNO = int(dictionary['PageNO'])

    newBook = Books.Book(ISBN,BookName,Authors,Publisher,Subjects,PublishYear,PageNO)
    BooksTemp.append(newBook)

def updateBook(ISBN,SearchSpace,ValueToSpace):
    for i in range(len(BooksTemp)):
        if (BooksTemp[i].ISBN == int(ISBN)):
            if SearchSpace == "BookName" and len(ValueToSpace) <=200:
                BooksTemp[i].BookName = ValueToSpace
            elif SearchSpace == "Authors" and len(ValueToSpace) <=200:
                BooksTemp[i].Authors = ValueToSpace    
            elif SearchSpace == "Publisher" and len(ValueToSpace) <=200:
                BooksTemp[i].Publisher = ValueToSpace
            elif SearchSpace == "Subjects" and len(ValueToSpace) <=200:
                BooksTemp[i].Subjects = ValueToSpace
            elif SearchSpace == "PublishYear" and len(ValueToSpace) <=200:
                BooksTemp[i].PublishYear = ValueToSpace
            elif SearchSpace == "PageNO" and len(ValueToSpace) <=200:
                BooksTemp[i].PageNO = ValueToSpace
             

            with open('books.txt','r+') as Writer:
                lines = Writer.readlines()
                changedValue =  lines[i]
                dash_index = changedValue.index('-')
                TrueValue = changedValue[dash_index+1:]
                TrueValue = TrueValue.split('/')
                for i in range(len(TrueValue)):
                    TrueValue[i] = TrueValue[i].split(':')
                for Item in TrueValue:
                    if SearchSpace in Item :
                        Item[1] == ValueToSpace
                        break
                Update = ''
                Update += str(i) + '-'
                for j in range(7):
                    if j != 6 :
                        Update += TrueValue[i][0] +":" + TrueValue[i][1]+ '/'
                    else:
                        Update += TrueValue[i][0] +":" + TrueValue[i][1]
                
                lines[i] = Update

                for String in lines:
                    Writer.write(String)
        
        

