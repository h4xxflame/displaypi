#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

# import kivy
# from kivy.config import Config
from kivy.app import App
# from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import BoundedNumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar


class Tacho(Widget):
    min_speed = 0
    max_speed = 160
    unit = NumericProperty(1.1)
    value = BoundedNumericProperty(0, min=min_speed, max=max_speed, errorvalue=0)
    file_tacho = StringProperty("img/tacho1.png")
    file_needle = StringProperty("img/needle.png")
    size_tacho = BoundedNumericProperty(128, min=128, max=256, errorvalue=128)
    size_text = NumericProperty(10)

    def __init__(self, **kwargs):
        super(Tacho, self).__init__(**kwargs)

        self._tacho = Scatter(
            size=(self.size_tacho, self.size_tacho),
            do_rotate = False,
            do_scale = False,
            do_translation = False
        )

        _img_tacho = Image(
            source=self.file_tacho,
            size=(self.size_tacho, self.size_tacho)
        )

        self._needle = Scatter(
            size=(self.size_tacho, self.size_tacho),
            do_rotate = False,
            do_scale = False,
            do_translation = False
        )

        _img_needle = Image(
            source=self.file_needle,
            size=(self.size_tacho, self.size_tacho)
        )

        self._glab = Label(font_size=self.size_text, markup=True)
        self._progress = ProgressBar(max=100, height=20, value=self.value)

        self._tacho.add_widget(_img_tacho)
        self._needle.add_widget(_img_needle)

        self.add_widget(self._tacho)
        self.add_widget(self._needle)
        self.add_widget(self._glab)
#        self.add_widget(self._progress)

        self.bind(pos=self._update)
        self.bind(size=self._update)
        self.bind(value=self._turn)

    def _update(self, *args):
        self._tacho.pos = self.pos
        self._needle.pos = (self.x, self.y)
        self._needle.center = self._tacho.center
        self._glab.center_x = self._tacho.center_x
        self._glab.center_y = self._tacho.center_y + (self.size_tacho/4)
        self._progress.x = self._tacho.x
        self._progress.y = self._tacho.y + (self.size_tacho / 4)
        self._progress.width = self.size_tacho

    def _turn(self, *args):
        self._needle.center_x = self._tacho.center_x
        self._needle.center_y = self._tacho.center_y
        self._needle.rotation = (80 * self.unit) - (self.value * self.unit)
        self._glab.text = "[b]{0:.0f}[/b]".format(self.value)
        self._progress.value = self.value


class Rpm(Widget):
    min_speed = 0
    max_speed = 160
    unit = NumericProperty(1.1)
    value = BoundedNumericProperty(0, min=min_speed, max=max_speed, errorvalue=0)
    file_rpm = StringProperty("img/tacho1.png")
    file_needle = StringProperty("img/needle.png")
    size_rpm = BoundedNumericProperty(128, min=128, max=256, errorvalue=128)
    size_text = NumericProperty(10)

    def __init__(self, **kwargs):
        super(Rpm, self).__init__(**kwargs)

        self._rpm = Scatter(
            size=(self.size_rpm, self.size_rpm),
            do_rotate = False,
            do_scale = False,
            do_translation = False
        )

        _img_rpm = Image(
            source=self.file_rpm,
            size=(self.size_rpm, self.size_rpm)
        )

        self._needle = Scatter(
            size=(self.size_rpm, self.size_rpm),
            do_rotate = False,
            do_scale = False,
            do_translation = False
        )

        _img_needle = Image(
            source=self.file_needle,
            size=(self.size_rpm, self.size_rpm)
        )

        self._glab = Label(font_size=self.size_text, markup=True)
        self._progress = ProgressBar(max=100, height=20, value=self.value)

        self._rpm.add_widget(_img_rpm)
        self._needle.add_widget(_img_needle)

        self.add_widget(self._rpm)
        self.add_widget(self._needle)
        self.add_widget(self._glab)
#        self.add_widget(self._progress)

        self.bind(pos=self._update)
        self.bind(size=self._update)
        self.bind(value=self._turn)

    def _update(self, *args):
        self._rpm.pos = self.pos
        self._needle.pos = (self.x, self.y)
        self._needle.center = self._rpm.center
        self._glab.center_x = self._rpm.center_x
        self._glab.center_y = self._rpm.center_y + (self.size_rpm/4)
        self._progress.x = self._rpm.x
        self._progress.y = self._rpm.y + (self.size_rpm / 4)
        self._progress.width = self.size_rpm

    def _turn(self, *args):
        self._needle.center_x = self._rpm.center_x
        self._needle.center_y = self._rpm.center_y
        self._needle.rotation = (80 * self.unit) - (self.value * self.unit)
        self._glab.text = "[b]{0:.0f}[/b]".format(self.value)
        self._progress.value = self.value


class TachoApp(App):
    def build(self):
        from kivy.uix.slider import Slider

        def test(*ars):
            tacho.value = s
            rpm.value = s.value
            print(s)

        box = BoxLayout(orientation='vertical', spacing=10, padding=10)
        tacho = Tacho(value=0, size_tacho=256, size_text=19)
        box.add_widget(tacho)

        rpm = Rpm(value=0, size_tacho=256, size_text=19)
#        box.add_widget(rpm)

#        s = uart.readline()
#        s.bin(value=test)
        s = Slider(min=0, max=160, value=0)
        s.bind(value=test)
        box.add_widget(s)

        return box

if __name__ == '__main__':
    '''
    import serial

    try:
        uart = serial.Serial('/dev/ttyAMA0', 9600)
    except:
        print("Failed to connect")
        exit()
'''
    TachoApp().run()

#    uart.close()
