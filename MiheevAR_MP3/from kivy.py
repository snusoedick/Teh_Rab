from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from pydub import AudioSegment
import os

class AudioEditorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        #File Chooser
        self.file_chooser = FileChooserListView(path='.', filters=['*.mp3'])
        self.layout.add_widget(self.file_chooser)

        #Load Button
        self.load_button = Button(text='Load MP3')
        self.load_button.bind(on_press=self.load_mp3)
        self.layout.add_widget(self.load_button)

        #Start and End Time Inputs
        self.start_time_label = Label(text='Start Time (seconds):')
        self.layout.add_widget(self.start_time_label)

        self.start_time_input = TextInput(hint_text='0')
        self.layout.add_widget(self.end_time_input)

        self.end_time_label = Label(text='End Time (seconds):')
        self.layout.add_widget(self.end_time_label)

        self.end_time_input = TextInput(hint_text='0')
        self.layout.add_widget(self.end_time_input)

        #Save Button
        self.save_button = Button(text='Save Trimmed MP3')
        self.save_button.bind(on_press=self.save_trimmed_mp3)
        self.layout.add_widget(self.save_button)

        return self.layout
    
    def load_mp3(self, instance):
        if self.file_chooser.selection:
            self.mp3_file = self.file_chooser.selection[0]
            self.audio = AudioSegment.from_mp3(self.mp3_file)
            self.show_popup('MP3 Loaded', f'Loaded: {self.mp3_file}')

    def save_trimmed_mp3(self, instance):
        try:
            start_time = int(self.start_time_input.text)
            end_time = int(self.end_time_input.text)
            trimmed_audio = self.audio[start_time * 1000:end_time * 1000]
            output_file = os.path.join(os.getcwd(), 'trimmed_' + os.path.basename(self.mp3_file))
            trimmed_audio.export(output_file, format='mp3')
            self.show_popup('Trimming Complete', f'Saved to: {output_file}')
        except Exception as e:
            self.show_popup('Error', str(e))

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10)
        popup_label = Label(text=message)
        popup_layout.add_widget(popup_label)
        close_button = Button(text='Close')
        popup_layout.add_widget(close_button)

        popup = Popup(title=title, content=popup_layout, sixe_hint=(0.8, 0.4))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    AudioEditorApp().run()