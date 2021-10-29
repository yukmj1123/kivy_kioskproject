import os
from kivy.logger import WHITE
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button  import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class MainPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 1
        self.padding=[36,16]
        self.img = Image(source="logo.png")
        self.add_widget(self.img)

        self.inside=BoxLayout()
        self.inside.orientation='vertical'
        self.inside.padding=[36,16]
        self.inside.rows=5

        self.inside.button1 = Button(text="burger", font_size=15, color=(1, 1, 1, 1), background_color=(1, 0, 0, 1))
        self.inside.button1.bind(on_press=self.pressed1)
        self.inside.add_widget(self.inside.button1)

        self.inside.button2 = Button(text="set", font_size=15, color=(1, 1, 1, 1), background_color=(1, 1, 0, 1))
        self.inside.button2.bind(on_press=self.pressed2)
        self.inside.add_widget(self.inside.button2)

        self.inside.button3 = Button(text="drink", font_size=15, color=(1, 1, 1, 1), background_color=(0, 1, 0, 1))
        self.inside.button3.bind(on_press=self.pressed6)
        self.inside.add_widget(self.inside.button3)

        self.inside.button4 = Button(text="ect", font_size=15, color=(1, 1, 1, 1), background_color=(0, 1, 1, 1))
        self.inside.button4.bind(on_press=self.pressed7)
        self.inside.add_widget(self.inside.button4)


        self.add_widget(self.inside)

    def pressed1(self, instance):
    #    self.screen_manager = ScreenManager()
        app.screen_manager.current = "BurgerDetailPage"

    def pressed2(self, instance):
        app.screen_manager.current = "SetDetailPage"

    def pressed3(self, instance):
        app.screen_manager.current = "BuyPage"

    def pressed4(self, instance):
        app.screen_manager.current = "MainPage"

    def pressed5(self, instance):
        app.screen_manager.current = "CompletePage"
    def pressed6(self, instance):
        app.screen_manager.current = "DrinkPage"
    def pressed7(self, instance):
        app.screen_manager.current = "EtcPage"

class BurgerDetailPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 1
        self.padding=[36,16]
        # self.img = Image(source="bigmac.png")
        # self.add_widget(self.img)

        self.inside=BoxLayout()
        self.inside.orientation='vertical'
        self.inside.padding=[36,16]
        self.inside.rows=5

        self.inside.button1 = Button(font_size=15,
                              color=(1, 1, 1, 1), background_color=(1, 1, 1, 1), background_normal = 'bigmac.png')
        self.inside.button1.bind(on_press=self.pressed3)
        self.inside.add_widget(self.inside.button1)

        self.inside.button2 = Button(font_size=15,
                              color=(1, 1, 1, 1), background_color=(1, 1, 1, 1), background_normal = 'shanghi.png')
        self.inside.button2.bind(on_press=self.pressed3)
        self.inside.add_widget(self.inside.button2)

        self.add_widget(self.inside)


    def pressed3(self, instance):
        app.screen_manager.current = "BuyPage"

class SetDetailPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 1
        self.padding=[36,16]
        # self.img = Image(source="bigmac.png")
        # self.add_widget(self.img)

        self.inside=BoxLayout()
        self.inside.orientation='vertical'
        self.inside.padding=[36,16]
        self.inside.rows=5

        self.inside.button1 = Button(font_size=15,
                              color=(1, 1, 1, 1), background_color=(1, 1, 1, 1), background_normal = 'set1.png')
        self.inside.button1.bind(on_press=self.pressed3)
        self.inside.add_widget(self.inside.button1)

        self.inside.button2 = Button(font_size=15,
                              color=(1, 1, 1, 1), background_color=(1, 1, 1, 1), background_normal = 'shanghiset.png')
        self.inside.button2.bind(on_press=self.pressed3)
        self.inside.add_widget(self.inside.button2)

        self.add_widget(self.inside)


    def pressed3(self, instance):
        app.screen_manager.current = "BuyPage"


# class SetDetailPage(GridLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#         self.rows = 1
#         self.padding=[36,16]
#         self.img = Image(source="set1.png")
#         self.add_widget(self.img)

#         self.inside=BoxLayout()
#         self.inside.orientation='vertical'
#         self.inside.padding=[36,16]
#         self.inside.rows=5

#         self.inside.button1 = Button(text="buy", font_size=15,
#                               color=(1, 1, 1, 1), background_color=(1, 0, 0, 1))
#         self.inside.button1.bind(on_press=self.pressed1)
#         self.inside.add_widget(self.inside.button1)

#         self.inside.button2 = Button(text="back", font_size=15,
#                               color=(1, 1, 1, 1), background_color=(1, 1, 0, 1))
#         self.inside.button2.bind(on_press=self.pressed1)
#         self.inside.add_widget(self.inside.button2)

#         self.add_widget(self.inside)


#     def pressed1(self, instance):
#         app.screen_manager.current = "pageapp"

class DrinkPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 1
        self.padding=[36,16]
        # self.img = Image(source="coke.png")
        # self.add_widget(self.img)

        self.inside=BoxLayout()
        self.inside.orientation='vertical'
        self.inside.padding=[36,16]
        self.inside.rows=5

        self.inside.button1 = Button(font_size=15,
                              color=(1, 1, 1, 1), background_color=(1, 1, 1, 1), background_normal = 'coke.png')
        self.inside.button1.bind(on_press=self.pressed3)
        self.inside.add_widget(self.inside.button1)

        self.inside.button2 = Button(font_size=15,
                              color=(1, 1, 1, 1), background_color=(1, 1, 1, 1), background_normal = 'sprite.png')
        self.inside.button2.bind(on_press=self.pressed3)
        self.inside.add_widget(self.inside.button2)

        self.add_widget(self.inside)


    def pressed3(self, instance):
        app.screen_manager.current = "BuyPage"

class EtcPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 1
        self.padding=[36,16]
        # self.img = Image(source="bigmac.png")
        # self.add_widget(self.img)

        self.inside=BoxLayout()
        self.inside.orientation='vertical'
        self.inside.padding=[36,16]
        self.inside.rows=5

        self.inside.button1 = Button(font_size=15,
                              color=(1, 1, 1, 1), background_color=(1, 1, 1, 1), background_normal = 'etc1.png')
        self.inside.button1.bind(on_press=self.pressed3)
        self.inside.add_widget(self.inside.button1)

        self.inside.button2 = Button(font_size=15,
                              color=(1, 1, 1, 1), background_color=(1, 1, 1, 1), background_normal = 'macnugget.png')
        self.inside.button2.bind(on_press=self.pressed3)
        self.inside.add_widget(self.inside.button2)

        self.add_widget(self.inside)


    def pressed3(self, instance):
        app.screen_manager.current = "BuyPage"



class BuyPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 1
        self.padding=[36,16]
        # self.img = Image(source="logo.png")
        # self.add_widget(self.img)

        self.inside=BoxLayout()
        self.inside.orientation='vertical'
        self.inside.padding=[36,16]
        self.inside.rows=5

        self.inside.button1 = Button(text="buy", font_size=15, color=(1, 1, 1, 1), background_color=(1, 0, 0, 1))
        self.inside.button1.bind(on_press=self.pressed5)
        self.inside.add_widget(self.inside.button1)

        self.inside.button2 = Button(text="back", font_size=15, color=(1, 1, 1, 1), background_color=(1, 1, 0, 1))
        self.inside.button2.bind(on_press=self.pressed4)
        self.inside.add_widget(self.inside.button2)

        self.add_widget(self.inside)

    def pressed5(self, instance):
        app.screen_manager.current = "CompletePage"


    def pressed4(self, instance):
        app.screen_manager.current = "MainPage"

    # def pressed4(self, instance):
    #     app.screen_manager.current = "pageapp"

class CompletePage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 1
        self.padding=[36,16]
        self.img = Image(source="logo.png")
        self.add_widget(self.img)

        self.inside=BoxLayout()
        self.inside.orientation='vertical'
        self.inside.padding=[36,16]
        self.inside.rows=5

        self.inside.button1 = Button(text="go main", font_size=15, color=(1, 1, 1, 1), background_color=(1, 0, 0, 1))
        self.inside.button1.bind(on_press=self.pressed4)
        self.inside.add_widget(self.inside.button1)


        self.add_widget(self.inside)

    def pressed4(self, instance):
    #    self.screen_manager = ScreenManager()
        app.screen_manager.current = "MainPage"


class PageApp(App):
    def build(self):

        self.screen_manager= ScreenManager()

        self.main_page=MainPage()
        screen = Screen(name="MainPage")
        screen.add_widget(self.main_page)
        self.screen_manager.add_widget(screen)

        self.bugerdetail_page=BurgerDetailPage()
        screen = Screen(name="BurgerDetailPage")
        screen.add_widget(self.bugerdetail_page)
        self.screen_manager.add_widget(screen)

        self.setdetail_page=SetDetailPage()
        screen = Screen(name="SetDetailPage")
        screen.add_widget(self.setdetail_page)
        self.screen_manager.add_widget(screen)

        self.buy_page=BuyPage()
        screen = Screen(name="BuyPage")
        screen.add_widget(self.buy_page)
        self.screen_manager.add_widget(screen)

        self.drink_page=DrinkPage()
        screen = Screen(name="DrinkPage")
        screen.add_widget(self.drink_page)
        self.screen_manager.add_widget(screen)

        self.complete_page=CompletePage()
        screen = Screen(name="CompletePage")
        screen.add_widget(self.complete_page)
        self.screen_manager.add_widget(screen)

        self.complete_page=EtcPage()
        screen = Screen(name="EtcPage")
        screen.add_widget(self.complete_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

# class AwesomeApp(App):
#     def build(self):
#         return MyLayout()

# class MyApp(App):
#     def build(self):
#         return mainpage()

if __name__=='__main__':
    #MyApp=PageApp()
    app=PageApp()
    app.run()
    #PageApp().run()