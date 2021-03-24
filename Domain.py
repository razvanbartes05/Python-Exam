class Phone:
    def __init__(self,name,number):
        if isinstance(name,str) == True and name != "":
            self.__name = name
        else:
            raise ValueError("Name must be a string and can't by empty")

        self.__number = number

    def get_name(self):
        return self.__name

    def set_name(self,name):
        if isinstance(name, str) == True and name != "":
            self.__name = name
        else:
            raise ValueError("Name must be a string and can't by empty")

    def get_number(self):
        return self.__number

    def set_number(self,number):
        self.__number = number

    def __str__(self):
        return "Contact's name = " + str(self.get_name()) + " and number " + str(self.get_number())

import unittest

class TestDomain(unittest.TestCase):
    def test_domain(self):
        p = Phone("Alex",2000)
        self.assertEqual(p.get_name(),"Alex")
        self.assertEqual(p.get_number(),2000)

t = TestDomain()
t.test_domain()
