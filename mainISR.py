import Books
import Publishers

BooksTemp = []
PublishersTemp = []

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
        count = attribute.index('-')
        info = attribute[count + 1:]
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
    Subjects = dictionary['Subjects']
    PublishYear = int(dictionary['PublishYear'])
    PageNO = int(dictionary['PageNO'])
    newBook = Books.Book(ISBN,BookName,Authors,Publisher,Subjects,PublishYear,PageNO)
    BooksTemp.append(newBook)


def updateBook(ISBN,SearchSpace,ValueToSpace):
    notfind = 1
    for index in range(len(BooksTemp)):
        if BooksTemp[index].ISBN == int(ISBN) :
            notfind = 0
            if SearchSpace == "BookName" and len(ValueToSpace) <= 200:
                BooksTemp[index].BookName = ValueToSpace
            elif SearchSpace == "Authors" and len(ValueToSpace) <= 200:
                BooksTemp[index].Authors = ValueToSpace
            elif SearchSpace == "Publisher" and len(ValueToSpace) <= 200:
                BooksTemp[index].Publisher = Value
            elif SearchSpace == "Subjects" and len(ValueToSpace) <= 100:
                BooksTemp[index].Subjects = ValueToSpace
            elif SearchSpace == "PublishYear" and len(ValueToSpace) == 4:
                BooksTemp[index].PublishYear = int(ValueToSpace)
            elif SearchSpace == "PageNO" and len(ValueToSpace) <= 4:
                BooksTemp[index].PageNO = int(ValueToSpace)
            changebookindex =  index
            break

    if not notfind:
        with open('books.txt','r') as reader:
            lines = reader.readlines()
            update = lines[changebookindex]
        for index1 in range(len(update)):
            if update[index1] == '-':
                trueUp = update[index1+1:]
                break
        turep = trueUp.split("/")
        for index1 in range(len(turep)) :

            key,value = turep[index1].split(':')
            if key == SearchSpace :
                value = ValueToSpace
                turep[index1] = key + ':' + value
                break
        newupdate = ''
        newupdate += str(changebookindex+1)
        newupdate += "-"
        for i in range(7):
            if i != 6 :
                newupdate += turep[i] +"/"
            else:
                newupdate += turep[i]
        lines[changebookindex] = newupdate
        with open('books.txt','w') as writer:
            for String in lines:
                writer.write(String)

def DisplayBook(Book):
    Att1 = [Book.ISBN,Book.BookName,Book.Authors,Book.Publisher,Book.Subjects,Book.PublishYear,Book.PageNo]
    Att2 = ['ISBN','BookName','Authors','Publisher','Subjects','PublishYear','PageNO']
    info = ''
    for i in range(7):
        info += Att2[i] +':' + str(Att1[i]) + '/'
    print(info)

def findBook(SearchSpace,ValueToSpace):
    if (SearchSpace == 'ISBN'):
        for book in BooksTemp:
            if book.ISBN == int(ValueToSpace):
                DisplayBook(book)
    elif SearchSpace =='BookName':
        for book in BooksTemp:
            if ValueToSpace in book.BookName:
                DisplayBook(book)
    elif SearchSpace =='Authors':
        for book in BooksTemp:
            if ValueToSpace in book.Authors:
                DisplayBook(book)
    elif SearchSpace =='Subjects':
        for book in BooksTemp:
            if ValueToSpace in book.Subjects:
                DisplayBook(book)

def removeBook(ISBN):
    for book in BooksTemp:
        if book in BooksTemp:
            if book.ISBN == int(ISBN):
                bookIndex =BooksTemp.index(book)
                BooksTemp.remove(book)
                changedValue =[]
                with open('books.txt','r') as reader:
                    Bookinfo = reader.readlines()
                for String in Bookinfo[bookIndex + 1:]:
                    for j in range(len(String)):
                        if String[j] == '-':
                            number = int(String[:j]) - 1
                            UpdateString = str(number) + String[j:]
                            changedValue.append(UpdateString)
                            break
                Bookinfo = Bookinfo[:bookIndex] + changedValue
                with open('books.txt','w') as Writer:
                    for i in Bookinfo:
                        Writer.write(i)

def readPublishers ():
    with open('Publisher.txt','r') as RW:
       lines = RW.readlines()
    for attribute in lines:
        atts1 = []
        atts2 = []
        for data in lines:
            count = data.index('-')
            info = data[count + 1:]
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
    SubjectsInterest = dictionary['SubjectsInterest']
    HeadName  = dictionary['HeadName']
    PubAddress = dictionary['PubAddress']
    newPublisher = Publishers.Publisher(PubID,PubName,SubjectsInterest,HeadName,PubAddress)
    PublishersTemp.append(newPublisher)

def addPublisher(PubID,PubName,SubjectsInterest,HeadName,PubAddress):
    if len(str(PubID) ) == 6 and len(PubName) <= 200 and len(SubjectsInterest) <= 200 and len(HeadName) <= 200 and len(PubAddress) <=200:
        newPublisher = Publishers.Publisher(PubID,PubName,SubjectsInterest,HeadName,PubAddress)
        for Publisher in PublishersTemp:
            if Publisher.PubID == PubID:
                return
        PublishersTemp.append(newPublisher)
        counter = len(PublishersTemp)
        info = ''
        info += str(counter) + '-'
        attsName = ['PubID','PubName','SubjectsInterest','HeadName','PubAddress']
        attsValues = [PubID,PubName,SubjectsInterest,HeadName,PubAddress]

        for i in range(5):
          if i != 4:
            info += attsName[i]+':'+str(attsValues[i]) + '/'
          else:
            info += attsName[i]+':'+str(attsValues[i])
        print(info)
        with open('Publisher.txt','a') as Writer:
            Writer.write(info + '\n')

def updatePublisher(PubID,SearchSpace,ValueToSpace):
    notfind = 1
    for i in range(len(PublishersTemp)):
        if (PublishersTemp[i].PubID == int(PubID)):
            notfind = 0
            if SearchSpace == 'PubName' and len(ValueToSpace) <=200:
                PublishersTemp[i].PubName = ValueToSpace
            elif SearchSpace == 'SubjectsInterest' and len(ValueToSpace) <=200:
                PublishersTemp[i].SubjectsInterest = ValueToSpace
            elif SearchSpace == 'HeadName' and len(ValueToSpace) <=200:
                PublishersTemp[i].HeadName = ValueToSpace
            elif SearchSpace == 'PubAddress' and len(ValueToSpace) <=200:
                PublishersTemp[i].PubAddress = ValueToSpace
            changepubindex =  i
            break
    if not notfind:
        with open('Publisher.txt','r') as reader:
            lines = reader.readlines()
            update = lines[changepubindex]
        for index1 in range(len(update)):
            if update[index1] == '-':
                trueUp = update[index1+1:]
                break
        turep = trueUp.split("/")
        for index1 in range(len(turep)) :

            key,value = turep[index1].split(':')
            if key == SearchSpace :
                value = ValueToSpace
                turep[index1] = key + ':' + value
                break
        newupdate = ''
        newupdate += str(changepubindex+1)
        newupdate += "-"
        for i in range(5):
            if i != 4 :
                newupdate += turep[i] +"/"
            else:
                newupdate += turep[i]
        lines[changepubindex] = newupdate
        with open('Publisher.txt','w') as writer:
            for String in lines:
                writer.write(String)


def DisplayPublisher(Publisher):
    Att1 = [Publisher.PubID,Publisher.PubName,Publisher.SubjectsInterest,Publisher.HeadName,Publisher.PubAddress]
    Att2 = ['PubID','PubName','SubjectsInterest','HeadName','PubAddress']
    info = ''
    for i in range(5):
        info += Att2[i] +':' + str(Att1[i]) + '/'
    print(info)

def findPublisher(SearchSpace,ValueToSpace):
    if SearchSpace == 'PubName':
        for publisher in PublishersTemp:
            if ValueToSpace in publisher.PubName:
                DisplayPublisher(publisher)

def removePublisher(PubID):
    for publisher in PublishersTemp:
        if publisher in PublishersTemp:
            if publisher.PubID == int(PubID):
                pubIndex =PublishersTemp.index(publisher)
                PublishersTemp.remove(publisher)
                changedValue =[]
                with open('Publisher.txt','r') as reader:
                    Pubinfo = reader.readlines()
                for String in Pubinfo[pubIndex + 1:]:
                    for j in range(len(String)):
                        if String[j] == '-':
                            number = int(String[:j]) - 1
                            UpdateString = str(number) + String[j:]
                            changedValue.append(UpdateString)
                            break
                Pubinfo = Pubinfo[:pubIndex] + changedValue
                with open('Publisher.txt','w') as Writer:
                    for i in Pubinfo:
                        Writer.write(i)

def Main():
    readBooks ()
    readPublishers()
    while True :
        userInput = input()
        if userInput[0:9] == '-add book' :
            userInputInfo = userInput [9:]
            userInputInfo = userInputInfo.split(',')
            for i in range(len(userInputInfo)):
                userInputInfo[i] = userInputInfo[i].split(':')

            for data in userInputInfo :
                if data[0] == ' ISBN':
                    ISBN = int(data[1])

                elif data[0] == ' BookName' :
                    BookName = data[1]

                elif data[0] == ' Authors' :
                    Authors = data[1]

                elif data[0] == ' Publisher' :
                    Publisher = data[1]

                elif data[0] == ' Subjects' :
                    Subjects = data[1]

                elif data[0] == ' PublishYear':
                    PublishYear = int(data[1])

                elif data[0] == ' PageNO':
                    PageNO = int(data[1])

            addBook(ISBN,BookName,Authors,Publisher,Subjects,PublishYear,PageNO)

        elif userInput[0:9] == 'find book':
            userInput = userInput.split(' ')
            SearchSpace = userInput[-1]
            ValueToSpace = userInput[2]
            findBook(SearchSpace,ValueToSpace)

        elif userInput[0:11] == 'update book':
            userInput = userInput.split(' ')
            ISBN =userInput[2]
            ValueToSpace = userInput[4]
            SearchSpace = userInput[6]

            updateBook(ISBN,ValueToSpace,SearchSpace)

        elif userInput[0:11] == 'remove book':
            ISBN = userInput.split(' ')[-1]
            removeBook(ISBN)

        elif userInput[0:13] == 'add publisher':
            userInputInfo = userInput [13:]
            userInputInfo = userInputInfo.split(',')
            for i in range(len(userInputInfo)):
                userInputInfo[i] = userInputInfo[i].split(':')

            for data in userInputInfo :
                if data[0] == ' PubID':
                    PubID = int(data[1])

                elif data[0] == ' PubName' :
                    PubName = data[1]

                elif data[0] == ' SubjectsInterest' :
                    SubjectsInterest = data[1]

                elif data[0] == ' HeadName' :
                    HeadName = data[1]

                elif data[0] == ' PubAddress' :
                    PubAddress = data[1]

            addPublisher(PubID,PubName,SubjectsInterest,HeadName,PubAddress)

        elif userInput[0:16] == 'update publisher':
                userInput = userInput.split(' ')
                PubId =userInput[2]
                ValueToSpace = userInput[4]
                Value = userInput[6]
                updatePublisher(PubId,ValueToSpace,Value)

        elif userInput[0:14] == 'find publisher':
                userInput = userInput.split(' ')
                SearchSpace = userInput[-1]
                ValueToSpace = userInput[2]
                findPublisher(SearchSpace,ValueToSpace)

        elif userInput[0:16] == 'remove publisher':
            PubID = userInput.split(' ')[-1]
            removePublisher(PubID)

Main()
