#from _typeshed import Self
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.image import Image
import os
import random
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label


class MyGrid(GridLayout):
    screen_manager= ScreenManager()
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.rows = 1
        self.padding=[36,16]
        self.img = Image(source="logo.png")
        self.add_widget(self.img)

        self.inside=BoxLayout()
        self.inside.orientation='vertical'
        self.inside.padding=[36,16]
        self.inside.rows=5

        self.inside.button1 = Button(text="burger", font_size=15,
                              color=(1, 1, 1, 1), background_color=(1, 0, 0, 1))
        self.inside.button1.bind(on_press=self.pressed1)
        self.inside.add_widget(self.inside.button1)

        self.inside.button2 = Button(text="set", font_size=15,
                              color=(1, 1, 1, 1), background_color=(1, 1, 0, 1))
        self.inside.button2.bind(on_press=self.pressed2)
        self.inside.add_widget(self.inside.button2)

        self.inside.button3 = Button(text="drink", font_size=15,
                              color=(1, 1, 1, 1), background_color=(0, 1, 0, 1))
        self.inside.button3.bind(on_press=self.pressed3)
        self.inside.add_widget(self.inside.button3)

        self.inside.button4 = Button(text="etc", font_size=15,
                              color=(1, 1, 1, 1), background_color=(0, 1, 1, 1))
        self.inside.button4.bind(on_press=self.pressed4)
        self.inside.add_widget(self.inside.button4)

        self.add_widget(self.inside)

    def pressed1(self, instance):
        sm = ScreenManager()
        sm.current = "burgerpage"

    #def pressed2(self, instance):
    #    sm = ScreenManager()
    #    sm.current = "setpage"

    #def pressed3(self, instance):
    #    sm = ScreenManager()
    #    sm.current = "drinkpage"

    #def pressed4(self, instance):
    #    sm = ScreenManager()
    #    sm.current = "etcpage"


class BurgerPage(GridLayout):
    screen_manager= ScreenManager()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        # menu_result=menu()
        self.inside2 = GridLayout()
        self.inside2.cols = 2

        # self.inside.add_widget(Label(text="plz".format(menu_result), font_size=15))




        self.padding=[36,16]
        self.img = Image(source="bigmac.png")
        self.add_widget(self.img)

        self.button2_1 = Button(text="good", background_normal = 'normal.png',font_size=15, color=(0, 0, 0, 1), background_color=(0.4, 1, 0.2, 1))
        self.button2_1.bind(on_press=self.pressed1)
        self.inside2.add_widget(self.button2_1)


        self.inside.button2 = Image("set1.png")
        self.inside.button2.bind(on_press=self.pressed1)
        self.inside.add_widget(self.inside.button2)

        self.inside = GridLayout()
        self.inside.cols = 1

        self.add_widget((self.inside))

    # def do_action(self):
    #     self.menu_result=menu()



    def pressed1(self, instance):
        sm = ScreenManager()
        sm.current="creditpage"

    #def pressed2(self, instance):
        #MyApp.screen_manager.current = "/"


class MyApp(App):
    def build(self):
        return MyGrid()

# class MyApp1(App):
#     def build(self):
#         return bugerpage()

class EpicApp(App):
    def build(self):
        self.screen_manager= ScreenManager()

        self.connect_page=BurgerPage()
        screen=Screen(name="bugerpage")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        # self.info_page=InfoPage()
        # screen = Screen(name="InfoPage")
        # screen.add_widget(self.info_page)
        # self.screen_manager.add_widget(screen)

        # self.end_page=EndPage()
        # screen = Screen(name="EndPage")
        # screen.add_widget(self.end_page)
        # self.screen_manager.add_widget(screen)

        return self.screen_manager



if __name__ == "__main__":
    MyApp=EpicApp()
    MyApp.run()

# class bugerpage(GridLayout):
#     screen_manager= ScreenManager()
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.cols = 1

#         self.inside2 = GridLayout()
#         self.inside2.cols = 2

#         self.padding=[36,16]
#         self.img = Image(source="bigmac.png")
#         self.add_widget(self.img)

#         self.button2_1 = Button(text="good", background_normal = 'normal.png',font_size=15, color=(0, 0, 0, 1), background_color=(0.4, 1, 0.2, 1))
#         self.button2_1.bind(on_press=self.pressed1)
#         self.inside2.add_widget(self.button2_1)


#         self.inside.button2 = Image("set1.png")
#         self.inside.button2.bind(on_press=self.pressed1)
#         self.inside.add_widget(self.inside.button2)

#         self.inside = GridLayout()
#         self.inside.cols = 1

#         self.add_widget((self.inside))


#     def pressed1(self, instance):
#         sm = ScreenManager()
#         sm.current="creditpage"

#     def pressed2(self, instance):
#         MyApp.screen_manager.current = "/"

#     def build(self):
#         self.screen_manager= ScreenManager()

#         self.connect_page=bugerpage()
#         screen=Screen(name="bugerpage")
#         screen.add_widget(self.connect_page)
#         self.screen_manager.add_widget(screen)

#         return self.screen_manager

# class setpage(GridLayout):
#     screen_manager= ScreenManager()
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.cols = 1


#         self.inside.button2 = Image("set1.png")
#         self.inside.button2.bind(on_press=self.pressed1)
#         self.inside.add_widget(self.inside.button2)


#         self.inside = GridLayout()
#         self.inside.cols = 1

#         self.add_widget((self.inside))


#     def pressed1(self, instance):
#         MyApp.screen_manager.current="creditpage"

# class drinkpage(GridLayout):
#     screen_manager= ScreenManager()
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.cols = 1


#         self.inside.button2 = Image("coke.png")
#         self.inside.button2.bind(on_press=self.pressed1)
#         self.inside.add_widget(self.inside.button2)
#         #self.add_widget(self.img)


#         self.inside = GridLayout()
#         self.inside.cols = 1

#         self.add_widget((self.inside))

# class etcpage(GridLayout):
#     screen_manager= ScreenManager()
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.cols = 1

#         self.inside.button2 = Image("etc1.png")
#         self.inside.button2.bind(on_press=self.pressed1)
#         self.inside.add_widget(self.inside.button2)
#         #self.add_widget(self.img)    

#         self.inside = GridLayout()
#         self.inside.cols = 1

#         self.add_widget((self.inside))


#     def pressed1(self, instance):
#         MyApp.screen_manager.current="creditpage"

# class creditpage(GridLayout):
#     screen_manager= ScreenManager()
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.cols = 1

#         self.inside = GridLayout()
#         self.inside.cols = 1

#         self.inside.button4 = Button(text="credit", font_size=15,
#                               color=(1, 1, 1, 1), background_color=(0, 1, 1, 1))
#         self.inside.button4.bind(on_press=self.pressed1)
#         self.inside.add_widget(self.inside.button4)

#         self.inside.button4 = Button(text="cash", font_size=15,
#                               color=(1, 1, 1, 1), background_color=(0, 1, 1, 1))
#         self.inside.button4.bind(on_press=self.pressed1)
#         self.inside.add_widget(self.inside.button4)

#         self.add_widget(self.inside)

#     def pressed1(self, instance):
#         MyApp.screen_manager.current="finalpage"

# class finalpage(GridLayout):
#     screen_manager= ScreenManager()
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.cols = 1
#         self.inside = GridLayout()
#         self.inside.cols = 1
#         self.inside.button4 = Button(text="completion", font_size=15,
#                               color=(1, 1, 1, 1), background_color=(0, 1, 1, 1))
#         self.inside.button4.bind(on_press=self.pressed1)
#         self.inside.add_widget(self.inside.button4)
    
#     def pressed1(self, instance):
#         MyApp.screen_manager.current="MyGrid"


#         self.add_widget((self.inside))


# class EpicApp(App):
#     def build(self):
#         self.screen_manager= ScreenManager()

#         self.connect_page=bugerpage()
#         screen=Screen(name="bugerpage")
#         screen.add_widget(self.connect_page)
#         self.screen_manager.add_widget(screen)

        # self.info_page=setpage()
        # screen = Screen(name="setpage")
        # screen.add_widget(self.info_page)
        # self.screen_manager.add_widget(screen)

        # self.end_page=drinkpage()
        # screen = Screen(name="drinkpage")
        # screen.add_widget(self.end_page)
        # self.screen_manager.add_widget(screen)

        # self.end_page=etcpage()
        # screen = Screen(name="etcpage")
        # screen.add_widget(self.end_page)
        # self.screen_manager.add_widget(screen)

#         self.end_page=creditpage()
#         screen = Screen(name="creditpage")
#         screen.add_widget(self.end_page)
#         self.screen_manager.add_widget(screen)

#         self.end_page=finalpage()
#         screen = Screen(name="finalpage")
#         screen.add_widget(self.end_page)
#         self.screen_manager.add_widget(screen)

#         return self.screen_manager

# if __name__ == "__main__":
#     EpicApp().run()

#if __name__ == "__main__":
#   MyApp=EpicApp()
#    MyApp.run()