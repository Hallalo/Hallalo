import arabic_reshaper
import webbrowser
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.core.clipboard import Clipboard
from kivymd.uix.menu import MDDropdownMenu
from kivymd.toast import toast
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen

KV = '''
ScreenManager:
    MainScreen:

<MainScreen>:
    name: 'main'
    
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Cryptage de Message"
            right_action_items: [["dots-vertical", lambda x: app.open_menu(x)]]
        
        MDBoxLayout:
            orientation: 'vertical'
            padding: 20
            spacing: 20

            MDTextField:
                id: message_input
                hint_text: "Entrez le message"
                icon_right: "message"
                size_hint_x: None
                width: 600
                pos_hint: {"center_x": 0.5}

            MDTextField:
                id: shift_input
                hint_text: "Entrez le décalage"
                helper_text: "Le décalage pour chiffrer le message (1-25)"
                helper_text_mode: "on_focus"
                icon_right: "numeric"
                size_hint_x: None
                width: 600
                pos_hint: {"center_x": 0.5}
                input_filter: 'int'

            MDRaisedButton:
                text: "Chiffrer"
                pos_hint: {"center_x": 0.5}
                on_release: app.encrypt_message()

            MDRaisedButton:
                text: "Déchiffrer"
                pos_hint: {"center_x": 0.5}
                on_release: app.decrypt_message()

            MDLabel:
                id: output_label
                text: ""
                halign: 'center'
                font_style: 'Subtitle1'

            MDRaisedButton:
                id: copy_button
                text: "Copier le texte"
                pos_hint: {"center_x": 0.5}
                disabled: True
                on_release: app.copy_to_clipboard()
'''

class MainScreen(Screen):
    pass

class EncryptApp(MDApp):

    def build(self):
        self.menu_items = [
            {
                "text": "Support",
                "icon": "currency-usd",
                "viewclass": "OneLineListItem",
                "on_release": lambda: self.menu_callback("Support"),
            },
            {
                "text": "À propos",
                "icon": "information",
                "viewclass": "OneLineListItem",
                "on_release": lambda: self.menu_callback("À propos"),
            },
        ]
        self.menu = MDDropdownMenu(
            caller=None,
            items=self.menu_items,
            width_mult=4,
        )
        return Builder.load_string(KV)

    def open_menu(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, text_item):
        if text_item == "Support":
            webbrowser.open("https://wa.me/message/C32DY44MFQLMG1")
        else:
            toast(f"Option sélectionnée: {text_item}")
        self.menu.dismiss()

    def caesar_cipher(self, text, shift, decrypt=False):
        if decrypt:
            shift =-shift
        result = ''
        for char in text:
            if char.isalpha():
                shift_amount = shift % 26
                start = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - start + shift_amount) % 26 + start)
            else:
                result += char
        return result

    def encrypt_message(self):
        message = self.root.get_screen('main').ids.message_input.text
        shift = self.root.get_screen('main').ids.shift_input.text

        if message and shift:
            try:
                shift = int(shift)
                if 1 <= shift <= 25:
                    encrypted_message = self.caesar_cipher(message, shift)
                    reshaped_text = arabic_reshaper.reshape(encrypted_message)
                    self.root.get_screen('main').ids.output_label.text = f"Message chiffré: {reshaped_text}"
                    
                    self.root.get_screen('main').ids.copy_button.disabled = False
                else:
                    toast("Le décalage doit être entre 1 et 25")
            except ValueError:
                toast("Le décalage doit être un nombre entier")
        else:
            toast("Veuillez entrer le message et le décalage")

    def decrypt_message(self):
        message = self.root.get_screen('main').ids.message_input.text
        shift = self.root.get_screen('main').ids.shift_input.text

        if message and shift:
            try:
                shift = int(shift)
                if 1 <= shift <= 25:
                    decrypted_message = self.caesar_cipher(message, shift, decrypt=True)
                    reshaped_text = arabic_reshaper.reshape(decrypted_message)
                    self.root.get_screen('main').ids.output_label.text = f"Message déchiffré: {reshaped_text}"
                    self.root.get_screen('main').ids.copy_button.disabled = False
                else:
                    toast("Le décalage doit être entre 1 et 25")
            except ValueError:
                toast("Le décalage doit être un nombre entier")
        else:
            toast("Veuillez entrer le message et le décalage")

    def copy_to_clipboard(self):
        output_text = self.root.get_screen('main').ids.output_label.text
        if output_text:
            Clipboard.copy(output_text.split(': ', 1)[-1])
            toast("Texte copié dans le presse-papiers")

if __name__ == '__main__':
    EncryptApp().run()
