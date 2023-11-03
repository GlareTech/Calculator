from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class Calculator(App):
    pass


class cal_ui(BoxLayout):
    screen = StringProperty("0")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def power(self, widget):
        if widget.state == "down":
            widget.text = "on"
            for i, v in self.ids.items():
                v.disabled = False
        else:
            widget.text = "off"
            for i, v in self.ids.items():
                v.disabled = True

    def show(self, widget):
        if widget.text == "on" or widget.text == "off":
            return 0
        if widget.text == "<-":
            text = self.screen[0:-1]
            if text == "":
                self.screen = "0"
            else:
                self.screen = text
            return 0
        if widget.text.lower() == "c":
            self.screen = "0"
            return 0
        if widget.text == "=":
            result = eval(self.screen)
            self.screen = str(result)
            return 0

        if self.screen == "0":
            self.screen = widget.text
        else:
            self.screen += widget.text


Calculator().run()
