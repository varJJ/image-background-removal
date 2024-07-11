import kivy
from kivy.app import App
from kivy.uix.button import Button
from kgit iivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

class ImageApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.img = Image(source='path/to/your/image.jpg')
        layout.add_widget(self.img)
        
        process_btn = Button(text='Remove Background')
        process_btn.bind(on_press=self.process_image)
        layout.add_widget(process_btn)
        
        return layout

    def process_image(self, instance):
        
        pass

if __name__ == '__main__':
    ImageApp().run()