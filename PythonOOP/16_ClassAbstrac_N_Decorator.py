from abc import ABC, abstractclassmethod

class Button(ABC):

    def __init__(self, set_link):
        self.link = set_link

    @abstractclassmethod
    def click(self):
        pass

    @property
    @abstractclassmethod
    def link(self):
        pass

class PushButton(Button):
    
    def click(self):
        print('Go To: {}'.format(self.link))

    @Button.link.setter
    def link(self, input):
        self.__link = input
    
    @link.getter
    def link(self):
        return self.__link


tombol1 = PushButton("www.KelasTerbuka.id")
tombol1.click()