from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from plyer import accelerometer, light
import time
import numpy as np
import matplotlib.pyplot as plt

class SensorApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = {
            "metal": [],
            "glass": [],
            "wood": [],
            "wall": []
        }
        self.current_surface = "metal"

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Натисніть, щоб почати запис")
        layout.add_widget(self.label)
        
        self.button = Button(text="Записати дані", on_press=self.record_data)
        layout.add_widget(self.button)
        
        self.analyze_button = Button(text="Аналіз", on_press=self.analyze_data)
        layout.add_widget(self.analyze_button)
        
        return layout
    
    def record_data(self, instance):
        try:
            light.enable()
            time.sleep(1)
            intensity = light.light
            self.data[self.current_surface].append(intensity)
            self.label.text = f"Зібрано {len(self.data[self.current_surface])} значень для {self.current_surface}"
        except Exception as e:
            self.label.text = f"Помилка: {e}"
    
    def analyze_data(self, instance):
        avg_values = {surface: np.mean(values) if values else 0 for surface, values in self.data.items()}
        
        surfaces = list(avg_values.keys())
        values = list(avg_values.values())
        
        plt.bar(surfaces, values, color=['silver', 'blue', 'brown', 'gray'])
        plt.xlabel("Поверхня")
        plt.ylabel("Середня інтенсивність світла")
        plt.title("Відбиття світла від різних поверхонь")
        plt.show()

if __name__ == "__main__":
    SensorApp().run()
