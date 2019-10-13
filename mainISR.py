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
    attsName = ["ISBN","BookName","Authors","Publisher","Subjects","PublishYear","PageNO"]
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

def Display(Book):
    Att1 = [ISBN,BookName,Authors,Publisher,Subjects,PublishYear,PageNO]
    Att2 = ["ISBN","BookName","Authors","Publisher","Subjects","PublishYear","PageNO"]
    info = ''
    for i in range(7):
        info += Att2[i] +':' + str(Att1[i]) + '/'
    print(info)

def findBook(SearchSpace,ValueToSpace):
    if (SearchSpace == 'ISBN'):
        for book in BooksTemp:
            if book.ISBN == int(ValueToSpace):
                Display(book)

    elif SearchSpace =='BookName':
        for book in BooksTemp:
            if book.BookName == ValueToSpace:
                Display(book)
    elif SearchSpace =='Authors':
        for book in BooksTemp:
            if book.Authors == ValueToSpace:
                Display(book)
    elif SearchSpace =='Subjects':
        for book in BooksTemp:
            if book.Subjects == ValueToSpace:
                Display(book)

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
                        if String[j] == "-":
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
        for item in attribute:
            count = item.index('-')
            info = item[count+1:]
            info = info.split('/')
        for item in info:
            att1,att2 = item.split(':')
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
    attsName = ["PubID","PubName","SubjectInterest","HeadName","PubAddress"]
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
            if SearchSpace == "BookName" and len(ValueToSpace) <=200:
                Publishers[i].BookName = ValueToSpace
            elif SearchSpace == "Authors" and len(ValueToSpace) <=200:
                Publishers[i].Authors = ValueToSpace
            elif SearchSpace == "Publisher" and len(ValueToSpace) <=200:
                Publishers[i].Publisher = ValueToSpace
            elif SearchSpace == "Subjects" and len(ValueToSpace) <=200:
                Publishers[i].Subjects = ValueToSpace
            elif SearchSpace == "PublishYear" and len(ValueToSpace) <=200:
                Publishers[i].PublishYear = ValueToSpace
            elif SearchSpace == "PageNO" and len(ValueToSpace) <=200:
                Publishers[i].PageNO = ValueToSpace


            with open('Publisher.txt','r+') as Writer:
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

def Display(Publisher):
    Att1 = [PubID,PubName,SubjectInterest,HeadName,PubAddress]
    Att2 = ["PubID","PubName","SubjectInterest","HeadName","PubAddress"]
    info = ''
    for i in range(7):
        info += Att2[i] +':' + str(Att1[i]) + '/'
    print(info)

def findPublisher(SearchSpace,ValueToSpace):
    elif SearchSpace == 'PubName':
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
                        if String[j] == "-":
                            number = int(String[:j])-1
                            Update = str(number) + String[j:]
                            changedValue.append(Update)
                            break
                Pubinfo = Publisherinfo[:PubIndex] + changedValue
                with open('Publishers.txt','w') as Writer:
                    for i in Pubinfo:
                        Writer.write(i)

def Main():

    ReadBookTextFile()
    ReadPublisherTextFile()

    while True :
        Commend = input()
        if Commend[0:9] == '-add book' :
            CommendInfo == Commend [9:]
            CommendInfo = CommendInfo.split(",")
            for Index in Range(len(CommendInfo)):
                CommendInfo[Index] == CommendInfo[Index].split(":")

            for Item in CommendInfo :

                if Item[0] == " ISBN ":
                    ISBN = int(Item[1][1:len(Item[1])-1])

                elif Item[0] == " BookName " :
                    BookName = Item[1][1:len(Item[1])-1]

                elif Item[0] == " Authors " :
                    Authors = Item[1][1:len(Item[1])-1]

                elif Item[0] == "Publisher" :
                    Publisher = Item[1][1:len(Item[1])-1]

                elif Item[0] == " Subjects " :
                    Subjects = Item[1][1:len(Item[1])-1]

                elif Item[0] == " PublishYear ":
                    PublishYear = int(Item[1][1:len(Item[1])-1])

                elif Item[0] == " PageNO ":
                    PageNO = int(Item[1][1:len(Item[1])-1])

            AddBook(ISBN,BookName,Authors,Publisher,Subjects,PublishYear,PageNO)

        elif Commend[0:9] == "find book":
            Commend = Commend.split(" ")
            SearchSpace = Commend[-1]
            Title = Commend[2]
            FindBook(SearchSpace,Title)

        elif Commend[0:11] == "update book":
            Commend = Commend.split(" ")
            ISBN =Commend[2]
            Title = Commend[4]
            Value = Commend[6]
            UpdateBook(ISBN,Title,Value)

        elif Commend[0:11] == "remove book":
            ISBN = Commend.split(" ")[-1]
            RemoveBook(ISBN)

        elif Commend[0:13]:
            CommendInfo = Commend[13:]
            CommendInfo = CommendInfo.split(",")
            for Item in CommendInfo:
                if Item[0] == " PubId ":
                    PubId = int(Item[1][1:len(Item[1])-1])

                elif Item[0] == " PubName " :
                    PubName = Item[1][1:len(Item[1])-1]

                elif Item[0] == " SubjectInterest " :
                    SubjectInterest = Item[1][1:len(Item[1])-1]

                elif Item[0] == " HeadName " :
                    HeadName = Item[1][1:len(Item[1])-1]

                elif Item[0] == " PubAddress " :
                    PubAddress = Item[1][1:len(Item[1])-1]

            AddPublisher(PubId,PubName,SubjectInterest,HeadName,PubAddress)

        elif Commend[0:16] == "remove publisher":
            PubId = Commend.split(" ")[-1]
            RemovePublisher(PubId)

        elif Commend[0:16] == "update Publisher":
            Commend = Commend.split(" ")
            PubId =Commend[2]
            Title = Commend[4]
            Value = Commend[6]
            UpdatePublisher(PubId,Title,Value)

        elif Commend[0:14] == "find publisher":
            Commend = Commend.split(" ")
            Value = Commend[2]
            FindPublisher(Value)