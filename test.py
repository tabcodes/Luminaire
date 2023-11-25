import sys
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_default_size(600, 250)
        self.set_title("Stocker")

        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.button = Gtk.Button(label="Hello!")
        self.button.connect("clicked", self.hello)

        self.set_child(self.box1)  # Horizontal box to window
        self.box1.append(self.box2)  # Put vert box in that box
        self.box1.append(self.box3)  # And another one, empty for now

        self.box2.append(
            self.button
        )  # Put button in the first of the two vertial boxes
        self.check = Gtk.CheckButton(label="And goodbye?")
        self.box2.append(self.check)
    
        self.switchbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.switch = Gtk.Switch()
        self.switch.set_active(True)
    
    def hello(self, button):
        print("Hello, world!")
        if self.check.get_active():
            print("Checked!")
            self.close()


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
