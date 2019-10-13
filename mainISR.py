import Books
import Publishers

BooksTemp = []
Publishers = []

def addBook (ISBN,BookName,Authors,Publisher,Subjects,PublishYear,PageNO):
    if len(str(ISBN) )<= 20 and len(BookName) <= 200 and len(Authors) <= 200 and len(Publisher) <= 200 and len(Subjects) <=200 and len(str(PublishYear)) == 4 and len(str(PageNO)) < 5:
         newBook = Books.Book(ISBN,BookName,Authors,Publisher,Subjects,PublishYear,PageNO)
         for Book in BooksTemp:
            if Book.ISBN == ISBN:
                return
    BooksTemp.append(newBook)
    counter = len(BooksTemp)
    info = ''
    info += str(counter) + '-'
    attsName = ['ISBN','BookName','Authors','Publisher','Subjects','PublishYear','PageNO']
    attsValues = [ISBN,BookName,Authors,Publisher,Subjects,PublishYear,PageNO]

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
        for data in attribute:
            count = data.index('-')
            info = data[count + 1:]
            info = info.split('/')
        for data in info:
            att1,att2 = data.split(':')
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
            if SearchSpace == 'BookName' and len(ValueToSpace) <=200:
                BooksTemp[i].BookName = ValueToSpace
            elif SearchSpace == 'Authors' and len(ValueToSpace) <=200:
                BooksTemp[i].Authors = ValueToSpace
            elif SearchSpace == 'Publisher' and len(ValueToSpace) <=200:
                BooksTemp[i].Publisher = ValueToSpace
            elif SearchSpace == 'Subjects' and len(ValueToSpace) <=200:
                BooksTemp[i].Subjects = ValueToSpace
            elif SearchSpace == 'PublishYear' and len(ValueToSpace) <=200:
                BooksTemp[i].PublishYear = ValueToSpace
            elif SearchSpace == 'PageNO' and len(ValueToSpace) <=200:
                BooksTemp[i].PageNO = ValueToSpace


            with open('books.txt','r+') as Writer:
                lines = Writer.readlines()
                changedValue =  lines[i]
                dash_index = changedValue.index('-')
                TrueValue = changedValue[dash_index+1:]
                TrueValue = TrueValue.split('/')
                for i in range(len(TrueValue)):
                    TrueValue[i] = TrueValue[i].split(':')
                for data in TrueValue:
                    if SearchSpace in data :
                        data[1] == ValueToSpace
                        break
                Update = ''
                Update += str(i) + '-'
                for j in range(7):
                    if j != 6 :
                        Update += TrueValue[i][0] +':' + TrueValue[i][1]+ '/'
                    else:
                        Update += TrueValue[i][0] +':' + TrueValue[i][1]

                lines[i] = Update

                for String in lines:
                    Writer.write(String)

def Display(Book):
    Att1 = [ISBN,BookName,Authors,Publisher,Subjects,PublishYear,PageNO]
    Att2 = ['ISBN','BookName','Authors','Publisher','Subjects','PublishYear','PageNO']
    info = ''
    for i in range(7):
        info += Att2[i] +':' + str(Att1[i]) + '/'
    print(info)

def findBook(SearchSpace,ValueToSpace):
    if (SearchSpace == 'ISBN'):
        for book in BooksTemp:
            if book.ISBN == int(ValueToSpace):
                Display(Book)
    elif SearchSpace =='BookName':
        for book in BooksTemp:
            if book.BookName == ValueToSpace:
                Display(Book)
    elif SearchSpace =='Authors':
        for book in BooksTemp:
            if book.Authors == ValueToSpace:
                Display(Book)
    elif SearchSpace =='Subjects':
        for book in BooksTemp:
            if book.Subjects == ValueToSpace:
                Display(Book)

def removeBook(ISBN):
    for book in BooksTemp:
        if book in BooksTemp:
            if book.ISBN == int(ISBN):
                bookIndex =BooksTemp.index(book)
                BooksTemp.remove(book)
                changedValue =[]
                with open('book.txt','r') as reader:
                    Bookinfo = reader.readlines()
                for String in Bookinfo[bookIndex+1:]:
                    for j in range(len(String)):
                        if String[j] == '-':
                            number = int(String[:j])-1
                            UpdateString = str(number) + String[j:]
                            changedValue.append(UpdateString)
                            break
                Bookinfo = Bookinfo[:bookIndex] + changedValue
                with open('books.txt','w') as Writer:
                    for i in Bookinfo:
                        Writer.write(i)

def readPublishers():
     with open('Publisher.txt','r') as RW:
       lines = RW.readlines()
     for attribute in lines:
        atts1 = []
        atts2 = []
        for data in attribute:
            count = data.index('-')
            info = data[count+1:]
            info = info.split('/')
        for data in info:
            att1,att2 = data.split(':')
        atts1.append(att1)
        atts2.append(att2)
        dictionary = dict(zip(atts1,atts2))
        createPublishers(dictionary)

def createPublishers(dictionary):
        PubID = int(dictionary['PubID'])
        PubName = dictionary['PubName']
        SubjectInterest = dictionary['SubjectInterest']
        HeadName  = dictionary['HeadName']
        PubAddress = dictionary['PubAddress']
        newPublisher = Publishers.Publisher(PubID,PubName,SubjectInterest,HeadName,PubAddress)
        Publishers.append(newPublisher)

def addPublisher(PubID,PubName,SubjectInterest,HeadName,PubAddress):
        if len(str(PubID) ) == 6 and len(PubName) <= 200 and len(SubjectInterest) <= 200 and len(HeadName) <= 200 and len(PubAddress) <=200:
            newPublisher = Publishers.Publisher(PubID,PubName,SubjectInterest,HeadName,PubAddress)
        for Publisher in Publishers:
            if Publisher.PubID == PubID:
                return
        Publishers.append(newPublisher)
        counter = len(Publishers)
        info = ''
        info += str(counter) + '-'
        attsName = ['PubID','PubName','SubjectInterest','HeadName','PubAddress']
        attsValues = [PubID,PubName,SubjectInterest,HeadName,PubAddress]

        for i in range(7):
          if i !=6:
            info += attsName[i]+':'+str(attsValues[i]) + '/'
          else:
            info += attsName[i]+':'+str(attsValues[i])
        with open('Publisher.txt','a') as Writer:
            Writer.write(info + '\n')

def updatePublisher(PubID,SearchSpace,ValueToSpace):
     for i in range(len(Publishers)):
        if (Publishers[i].ISBN == int(ISBN)):
            if SearchSpace == 'BookName' and len(ValueToSpace) <=200:
                Publishers[i].BookName = ValueToSpace
            elif SearchSpace == 'Authors' and len(ValueToSpace) <=200:
                Publishers[i].Authors = ValueToSpace
            elif SearchSpace == 'Publisher' and len(ValueToSpace) <=200:
                Publishers[i].Publisher = ValueToSpace
            elif SearchSpace == 'Subjects' and len(ValueToSpace) <=200:
                Publishers[i].Subjects = ValueToSpace
            elif SearchSpace == 'PublishYear' and len(ValueToSpace) <=200:
                Publishers[i].PublishYear = ValueToSpace
            elif SearchSpace == 'PageNO' and len(ValueToSpace) <=200:
                Publishers[i].PageNO = ValueToSpace


            with open('Publisher.txt','r+') as Writer:
                lines = Writer.readlines()
                changedValue =  lines[i]
                dash_index = changedValue.index('-')
                TrueValue = changedValue[dash_index+1:]
                TrueValue = TrueValue.split('/')
                for i in range(len(TrueValue)):
                    TrueValue[i] = TrueValue[i].split(':')
                for data in TrueValue:
                    if SearchSpace in data :
                        data[1] == ValueToSpace
                        break
                Update = ''
                Update += str(i) + '-'
                for j in range(7):
                    if j != 6 :
                        Update += TrueValue[i][0] +':' + TrueValue[i][1]+ '/'
                    else:
                        Update += TrueValue[i][0] +':' + TrueValue[i][1]

                lines[i] = Update

                for String in lines:
                    Writer.write(String)

def Display(Publisher):
    Att1 = [PubID,PubName,SubjectInterest,HeadName,PubAddress]
    Att2 = ['PubID','PubName','SubjectInterest','HeadName','PubAddress']
    info = ''
    for i in range(7):
        info += Att2[i] +':' + str(Att1[i]) + '/'
    print(info)

def findPublisher(SearchSpace,ValueToSpace):
    if SearchSpace == 'PubName':
        for book in BooksTemp:
            if publisher.PubName == ValueToSpace:
                Display(Publisher)

def removePublisher(PubId):
      for publisher in Publishers:
         if publisher in Publishers:
            if publisher.PubID == int(PubID):
                PubIndex =Publishers.index(publisher)
                Publishers.remove(publisher)
                changedValue =[]
                with open('Publisher.txt','r') as reader:
                    Publisherinfo = reader.readlines()
                for String in Publisherinfo [PubIndex + 1:]:
                    for j in range(len(String)):
                        if String[j] == '-':
                            number = int(String[:j])-1
                            Update = str(number) + String[j:]
                            changedValue.append(Update)
                            break
                Pubinfo = Publisherinfo[:PubIndex] + changedValue
                with open('Publishers.txt','w') as Writer:
                    for i in Pubinfo:
                        Writer.write(i)

def Main():
    readBooks ()
    readPublishers()
    while True :
        userInput = input()
        if userInput[0:9] == '-add book' :
            userInputInfo == userInput [9:]
            userInputInfo = userInputInfo.split(',')
            for i in Range(len(userInputInfo)):
                userInputInfo[i] == userInputInfo[i].split(':')

            for data in userInputInfo :
                if data[0] == 'ISBN':
                    ISBN = int(data[1][1:len(data[1])-1])

                elif data[0] == 'BookName' :
                    BookName = data[1][1:len(data[1])-1]

                elif data[0] == 'Authors' :
                    Authors = data[1][1:len(data[1])-1]

                elif data[0] == 'Publisher' :
                    Publisher = data[1][1:len(data[1])-1]

                elif data[0] == 'Subjects' :
                    Subjects = data[1][1:len(data[1])-1]

                elif data[0] == 'PublishYear':
                    PublishYear = int(data[1][1:len(data[1])-1])

                elif data[0] == 'PageNO':
                    PageNO = int(data[1][1:len(data[1])-1])

            addBook(ISBN,BookName,Authors,Publisher,Subjects,PublishYear,PageNO)

        elif userInput[0:9] == 'find book':
            userInput = userInput.split(' ')
            SearchSpace = userInput[-1]
            Title = userInput[2]
            findBook(SearchSpace,ValueToSpace)

        elif userInput[0:11] == 'update book':
            userInput = userInput.split(' ')
            ISBN =userInput[2]
            Title = userInput[4]
            Value = userInput[6]
            updateBook(ISBN,SearchSpace,ValueToSpace)

        elif userInput[0:11] == 'remove book':
            ISBN = userInput.split(' ')[-1]
            removeBook(ISBN)

        elif userInput[0:13]:
            userInputInfo = userInput[13:]
            userInputInfo = userInputInfo.split(',')
            for data in userInputInfo:
                if data[0] == 'PubId':
                    PubId = int(data[1][1:len(data[1])-1])

                elif data[0] == 'PubName' :
                    PubName = data[1][1:len(data[1])-1]

                elif data[0] == 'SubjectInterest' :
                    SubjectInterest = data[1][1:len(data[1])-1]

                elif data[0] == 'HeadName' :
                    HeadName = data[1][1:len(data[1])-1]

                elif data[0] == 'PubAddress' :
                    PubAddress = data[1][1:len(data[1])-1]

            addPublisher(PubId,PubName,SubjectInterest,HeadName,PubAddress)

        elif userInput[0:16] == 'update Publisher':
                userInput = userInput.split(' ')
                PubId =userInput[2]
                Title = userInput[4]
                Value = userInput[6]
                updatePublisher(PubId,Title,Value)

        elif userInput[0:14] == 'find publisher':
                userInput = userInput.split(' ')
                Value = userInput[2]
                findPublisher(Value)

        elif userInput[0:16] == 'remove publisher':
            PubId = userInput.split(' ')[-1]
            removePublisher(PubId)


        Main()
Main()
