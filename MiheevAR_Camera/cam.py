from kivy.app import App # Основной класс приложения
from kivy.uix.boxlayout import BoxLayout #Контейнер для размещения виджетов
from kivy.uix.image import Image # Виджет для отображения изображений
from kivy.clock import Clock # Для периодического обновления экрана
from kivy.graphics.texture import Texture # Для создания текстур изображений
import cv2 # Импортируем OpenCV для работы с камерой

class CameraApp(App):
    def build(self):
        # Создаем основной контейнер (BoxLayout)
        layout = BoxLayout(orientation='vertical')
                           
        # Создаем виджет для отображения изображения с камеры
        self.img1 = Image()
        
        # Добавляем виджет в контейнер
        layout.add_widget(self.img1)
        
        #Инициализируем камеру
        self.capture = cv2.VideoCapture(0)

        # Устанавливаем размер кадра (опционально)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
   
        # Запускаем цикл обновления кадров
        Clock.schedule_interval(self. update, 1.0 / 30.0) # Обновляем каждый 1/30 секунды
        
        return layout

    def update(self, dt):
        # Считываем кадр с камеры
        ret, frame = self.capture.read()
        
        #Проверяем, успешно ли считан кадр
        if ret:
            # Преобразуем цветовое пространство из BGR в RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Создаем текстуру из кадра
            texture = Texture.create(size=(frame. shape[1], frame. shape[0]))
            texture.blit_buffer(frame.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
             
            # Обновляем текстуру в виджете Image
            self.img1.texture = texture
            
    def on_stop(self):
       # Освобождаем ресурсы камеры при закрытии приложения
       self.capture.release()
       
if __name__=='__main__':
    CameraApp().run() #Запускаем приложение
