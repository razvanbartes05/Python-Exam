from Infrastructure import search

class WorkRepo:
    def __init__(self):
        self.__data = []

    def addContact(self,newcontact):
        self.__data.append(newcontact)

    def printList(self):
        for e in self.__data:
            print(e)

    def updateContact(self,index,newname,newnumber):
        for i in range(len(self.__data)):
            if i == index:
                self.__data[i].set_name(newname)
                self.__data[i].set_name(newnumber)

    def searchnumber_work(self):
        def f(x):
            if x.get_number()[len(x.get_number())-4:] == "999":
                return True
            return False
        a = search(self.__data,f)
        for i in range(len(a)):
            del self.__data[a[i]]

    def WorkSort(self):
        sorted(self.__data, key=lambda x:x.get_name())


class PersonalRepo:
    def __init__(self):
        self.__data = []

    def addContact(self,newcontact):
        self.__data.append(newcontact)

    def printList(self):
        for e in self.__data:
            print(e)

    def updateContact(self, index, newname, newnumber):
        for e in self.__data:
            if e == index:
                e.set_name(newname)
                e.set_number(newnumber)

    def searchnumber_personal(self):
        def f(x):
            if x.get_number()%1000 == 999:
                return True
            return False
        a = search(self.__data,f)
        for i in rage(len(a)):
            print(self.__data[a[i]])


    def PersonalSort(self):
        def f(x,y):
            if x.get_number() < y.get_number():
                return True
            return False
        selection_sort(self.__data,f)

