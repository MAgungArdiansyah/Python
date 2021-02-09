# module abc = abstract base class
from abc import ABC, abstractclassmethod

class Button(ABC):

    @abstractclassmethod
    def click(self): # class ini wajib ada di sub class kalau tidak error
        print('siwah')

class PushButton(Button):

    def click(self):
        print('push button click')
    
    def test(self):
        print('test')

tombol1 = PushButton()


#tombol1.click()
tombol1.test()