import sys
import gi
from lifxlan import LifxLAN as LLAN

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_default_size(600, 250)
        self.set_title("Luminaire")

        self.lan = LLAN()

        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.button = Gtk.Button(label="Power On All")
        self.button.connect("clicked", self.powerOnAll)

        self.button2 = Gtk.Button(label="Power Off All")
        self.button2.connect("clicked", self.powerOffAll)

        self.set_child(self.box1)  # Horizontal box to window
        self.box1.append(self.box2)  # Put vert box in that box
        self.box1.append(self.box3)  # And another one, empty for now

        self.box2.append(
            self.button
        )
        
        self.box2.append(
            self.button2
        )

        self.switchbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.switch = Gtk.Switch()
        self.switch.set_active(True)

    def powerOnAll(self, button):

        self.lan.set_power_all_lights(True, 0)

    def powerOffAll(self, button):

        self.lan.set_power_all_lights(False, 0)


class Luminaire(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


app = Luminaire(application_id="us.tedha.Luminaire")
app.run(sys.argv)
