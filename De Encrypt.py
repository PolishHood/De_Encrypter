from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
import sys
import pycipher
import clipboard

Builder.load_string("""
<Button>:
    font_size: 50

<TextInput>:
    font_size: 50
    padding_x: [self.center[0] - self._get_text_width(max(self._lines, key=len), self.tab_width, self._label_cached) / 2.0, 0] if self.text else [self.center[0], 0]
    padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]

<SelectingCipherScreen>:
    GridLayout:
        rows: 6
        Button:
            text: 'Ceasar Cipher'
            on_press: root.cipher_c()
            on_press: root.manager.current = 'cshift'
        Button:
            text: 'Autokey'
            on_press: root.cipher_ak()
            on_press: root.manager.current = 'autokey'
        Button:
            text: 'WIP'
            on_press:
        Button:
            text: 'WIP'
            on_press:
        Button:
            text: 'WIP'
            on_press:
        Button:
            text: 'WIP'
            on_press:
        Button:
            text: 'WIP'
            on_press:
        Button:
            text: 'Exit'
            on_press: exit()

<CShiftScreen>:
    GridLayout:
        rows: 6
        Button:
            text: '1'
            on_press: root.cbutt_1()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '2'
            on_press: root.cbutt_2()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '3'
            on_press: root.cbutt_3()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '4'
            on_press: root.cbutt_4()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '5'
            on_press: root.cbutt_5()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '6'
            on_press: root.cbutt_6()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '7'
            on_press: root.cbutt_7()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '8'
            on_press: root.cbutt_8()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '9'
            on_press: root.cbutt_9()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '10'
            on_press: root.cbutt_10()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '11'
            on_press: root.cbutt_11()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '12'
            on_press: root.cbutt_12()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '13'
            on_press: root.cbutt_13()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '14'
            on_press: root.cbutt_14()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '15'
            on_press: root.cbutt_15()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '16'
            on_press: root.cbutt_16()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '17'
            on_press: root.cbutt_17()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '18'
            on_press: root.cbutt_18()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '19'
            on_press: root.cbutt_19()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '20'
            on_press: root.cbutt_20()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '21'
            on_press: root.cbutt_21()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '22'
            on_press: root.cbutt_22()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '23'
            on_press: root.cbutt_23()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '24'
            on_press: root.cbutt_24()
            on_press: root.manager.current = 'keep_punct'
        Button:
            text: '25'
            on_press: root.cbutt_25()
            on_press: root.manager.current = 'keep_punct'

<KeepPunctScreen>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        Label:
            size_hint: .5, .5
            font_size: 50
            text: 'Do you want to keep punctuation?'
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'bottom'
        Button:
            size_hint: .5, .5
            text: 'Yes'
            on_press: root.true()
            on_press: root.manager.current = 'menu'
    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'bottom'
        Button:
            size_hint: .5, .5
            text: 'No'
            on_press: root.false()
            on_press: root.manager.current = 'menu'

<AutoKeyScreen>:
    on_enter: akey.text = 'Enter key'
    GridLayout:
        rows: 2
        TextInput:
            id: akey
        Button:
            text: 'OK'
            on_press: root.submit_ak()
            on_press: root.manager.current = 'menu'

<MenuScreen>:
    GridLayout:
        rows: 5
        Button:
            text: 'Encrypt'
            on_press: root.manager.current = 'encrypt'
        Button:
            text: 'Decrypt'
            on_press: root.manager.current = 'decrypt'
        Button:
            text: 'Back to cipher list'
            on_press: root.manager.current = 'selcipher'
        Button:
            text: 'Exit'
            on_press: exit()

<EncryptScreen>:
    on_enter: ptext.text = 'Enter plaintext'
    GridLayout:
        rows: 5
        TextInput:
            id: ptext
        Button:
            text: 'Encrypt'
            on_press: root.encryption(ptext.text)
        Button:
            text: 'Copy'
            on_press: root.copy()
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
        Button:
            text: 'Exit'
            on_press: exit()

<DecryptScreen>:
    on_enter: dtext.text = 'Enter ciphertext'
    GridLayout:
        rows: 5
        TextInput:
            id: dtext
        Button:
            text: 'Decrypt'
            on_press: root.decryption(dtext.text)
        Button:
            text: 'Copy'
            on_press: root.copy()
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
        Button:
            text: 'Exit'
            on_press: exit()
""")

class SelectingCipherScreen(Screen):

    def cipher_c(self):
        global cipher
        cipher = 1

    def cipher_ak(self):
        global cipher
        cipher = 2

class CShiftScreen(Screen):

    def cbutt_1(self):
        global cshift
        cshift = 1

    def cbutt_2(self):
        global cshift
        cshift = 2

    def cbutt_3(self):
        global cshift
        cshift = 3

    def cbutt_4(self):
        global cshift
        cshift = 4

    def cbutt_5(self):
        global cshift
        cshift = 5

    def cbutt_6(self):
        global cshift
        cshift = 7

    def cbutt_8(self):
        global cshift
        cshift = 8

    def cbutt_9(self):
        global cshift
        cshift = 9

    def cbutt_10(self):
        global cshift
        cshift = 10

    def cbutt_11(self):
        global cshift
        cshift = 11

    def cbutt_12(self):
        global cshift
        cshift = 12

    def cbutt_13(self):
        global cshift
        cshift = 13

    def cbutt_14(self):
        global cshift
        cshift = 14

    def cbutt_15(self):
        global cshift
        cshift = 15

    def cbutt_16(self):
        global cshift
        cshift = 16

    def cbutt_17(self):
        global cshift
        cshift = 17

    def cbutt_18(self):
        global cshift
        cshift = 18

    def cbutt_19(self):
        global cshift
        cshift = 19

    def cbutt_20(self):
        global cshift
        cshift = 20

    def cbutt_21(self):
        global cshift
        cshift = 21

    def cbutt_22(self):
        global cshift
        cshift = 22

    def cbutt_23(self):
        global cshift
        cshift = 23

    def cbutt_24(self):
        global cshift
        cshift = 24

    def cbutt_25(self):
        global cshift
        cshift = 25

class KeepPunctScreen(Screen):

    def true(self):
        global bl
        bl = True

    def false(self):
        global bl
        bl = False

class AutoKeyScreen(Screen):

    def submit_ak(self):
        global ak
        ak = self.ids.akey.text

class MenuScreen(Screen):
    pass

class EncryptScreen(Screen):

    def encryption(self, text):
        if cipher == 1:
            plaintext = self.ids.ptext.text
            self.ids.ptext.text = pycipher.Caesar(cshift).encipher(plaintext, keep_punct=bl)

        elif cipher == 2:
            plaintext = self.ids.ptext.text
            self.ids.ptext.text = pycipher.Autokey(ak).encipher(plaintext)

    def copy(self):
        copied = self.ids.ptext.text
        clipboard.copy(copied)

class DecryptScreen(Screen):

    def decryption(self, text):
        if cipher == 1:
            ciphertext = self.ids.dtext.text
            self.ids.dtext.text = pycipher.Caesar(cshift).decipher(ciphertext, keep_punct=bl)

        elif cipher == 2:
            ciphertext = self.ids.dtext.text
            self.ids.dtext.text = pycipher.Autokey(ak).decipher(ciphertext)

    def copy(self):
        copied = self.ids.dtext.text
        clipboard.copy(copied)

sm = ScreenManager()
sm.add_widget(SelectingCipherScreen(name='selcipher'))
sm.add_widget(AutoKeyScreen(name='autokey'))
sm.add_widget(CShiftScreen(name='cshift'))
sm.add_widget(KeepPunctScreen(name='keep_punct'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(EncryptScreen(name='encrypt'))
sm.add_widget(DecryptScreen(name='decrypt'))

class De_EncryptApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    De_EncryptApp().run()
