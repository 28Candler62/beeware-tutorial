"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class HelloWorld(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            "Your name: ",
            style=Pack(padding=(0, 5))
        )

        display_label = toga.Label(
            'Display Here: ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))
        self.display_input = toga.TextInput(style=Pack(flex=1), readonly=True)

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        display_box = toga.Box(style=Pack(direction=ROW, padding=5))
        display_box.add(display_label)
        display_box.add(self.display_input)

        button = toga.Button(
            "Say Hello!",
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(display_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        self.display_input.value = self.name_input.value
        self.main_window.info_dialog(
            f"Hello, {self.name_input.value}",
            "Hi there!"
        )


def main():
    return HelloWorld()

