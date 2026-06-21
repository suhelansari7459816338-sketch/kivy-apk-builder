import sys
import nest_asyncio
nest_asyncio.apply()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from g4f.client import Client

class AICaptionApp(App):
    def build(self):
        self.title = "AI Caption Generator"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        layout.add_widget(Label(text="✨ AI Caption & Hashtag Generator ✨", font_size=20, size_hint_y=None, height=40))
        
        self.topic_input = TextInput(hint_text="e.g., Free Fire epic gameplay", multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.topic_input)
        
        self.btn = Button(text="Generate Content 🚀", background_color=(0, 0.7, 0.9, 1), font_size=18, size_hint_y=None, height=60)
        self.btn.bind(on_press=self.generate_ai_stuff)
        layout.add_widget(self.btn)
        
        scroll = ScrollView()
        self.output_label = Label(text="Aapka Content Yahan Aayega...", font_size=14, size_hint_y=None, halign='left', valign='top')
        self.output_label.bind(size=self.output_label.setter('text_size'))
        scroll.add_widget(self.output_label)
        layout.add_widget(scroll)
        return layout

    def generate_ai_stuff(self, instance):
        self.output_label.text = "AI Content Generate Kar Raha Hai... Please wait..."
        topic = self.topic_input.text
        if not topic:
            self.output_label.text = "Bhai, pehle kuch topic toh likho!"
            return
        try:
            client = Client()
            prompt = f"Create 3 engaging social media captions with emojis and 15 trending hashtags for this topic: {topic}."
            response = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt}])
            self.output_label.text = response.choices[0].message.content
            self.output_label.height = 1200 
        except Exception as e:
            self.output_label.text = f"An error occurred: {e}"

if __name__ == "__main__":
    AICaptionApp().run()
