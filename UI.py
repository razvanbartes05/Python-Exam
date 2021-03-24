from Domain import Phone
from Repository import WorkRepo
from Repository import PersonalRepo

class UI:
    def __init__(self,wrepo,prepo):
        self.__wrepo = wrepo
        self.__prepo = prepo

    def printMenu(self):
        print("1.Update a contact from Work")
        print("2.Update a contact from Personal List")
        print("3.Filter contact from Work")
        print("4.Filter contact from Personal list")
        print("5.View cotacts from Work")
        print("6. View contacts form Personal List")
        print("7. Filter Work List")
        print("6. Filter Personal List")

    def load_list(self):
        self.__wrepo.addContact(Phone("Popescu",+40-711-11199))
        self.__wrepo.addContact(Phone("Ionescu",+40-722-22299))
        self.__wrepo.addContact(Phone("Toma",+40-711-11199))

        self.__prepo.addContact(Phone("Mom",+40-733-333444))
        self.__prepo.addContact(Phone("Dana",+40-744-444999))
        self.__prepo.addContact(Phone("Paul",+40-755-555999))

    def start(self):

        self.load_list()

        while True:
            self.printMenu()
            c = int(input("Choice: "))
            if c == 1:
                i = int(input("Give me an index: "))
                newname = input("Give me a new name: ")
                newnumber = input("Give me a new number: ")
                self.__wrepo.updateContact(i,newname,newnumber)
            elif c == 2:
                i = int(input("Give me an index: "))
                newname = input("Give me a new name: ")
                newnumber = input("Give me a new number: ")
                self.__prepo.updateContact(i, newname, newnumber)
            elif c == 3:
                pass
            elif c == 4:
                pass
            elif c == 5:
                self.__wrepo.printList()
            elif c == 6:
                self.__prepo.printList()
            elif c == 7:
                self.__wrepo.searchnumber_work()
            elif c == 8:
                self.__prepo.searchnumber_personal()
            else:
                break

wrepo = WorkRepo()
prepo = PersonalRepo()
u = UI(wrepo,prepo)
u.start()



