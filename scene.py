from model import *
import glm

# Класс сцены. Здесь мы загружаем наши объекты
class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    # Загружаем на сцену объекты, объявленные в этой ф-ии
    # Здесь прописываются статичные объекты сцены
    def load(self):
        app = self.app
        add = self.add_object

        # С использованием примитивов релизуем дома
        # Основная площадка для размещения
        add(Cube(app, pos=(0, 0, 0),scale=(20,0.1,20),tex_id=1))

        # Дорога, проложенная на земле
        add(Cube(app, pos=(0, 0.2, 0),scale=(2.5,0.02,20),tex_id=0))

        # Нарисуем дом
        # Окна и дверь
        add(Cube(app, pos=(13, 4, -4),scale=(4,4,4),tex_id=2))
        # Стены
        add(Cube(app, pos=(13, 4, -8),scale=(0.05,4,4),tex_id=4,rot=(0,90,0)))
        add(Cube(app, pos=(13, 4, 0),scale=(0.05,4,4),tex_id=4,rot=(0,90,0)))
        add(Cube(app, pos=(13, 8, -4),scale=(0.05,4,4),tex_id=4,rot=(0,0,90)))
        add(Cube(app, pos=(17, 4, -4),scale=(0.05,4,4),tex_id=4,rot=(0,0,0)))

        # Крыша
        add(Cube(app, pos=(11, 10, -4),scale=(3,0.1,5),tex_id=3,rot=(0,0,45)))
        add(Cube(app, pos=(15, 10, -4),scale=(3,0.1,5),tex_id=3,rot=(0,0,-45)))

        add(Triangle(app, pos=(13, 10, 0),scale=(4,2,2),tex_id=5))
        add(Triangle(app, pos=(13, 10, -8),scale=(4,2,2),tex_id=5))



        # Нарисуем второй дом
        # Окна и дверь
        add(Cube(app, pos=(13, 4, 10),scale=(4,4,4),tex_id=2))
        # Стены
        add(Cube(app, pos=(13, 4, 6),scale=(0.05,4,4),tex_id=4,rot=(0,90,0)))
        add(Cube(app, pos=(13, 4, 14),scale=(0.05,4,4),tex_id=4,rot=(0,90,0)))
        add(Cube(app, pos=(13, 8, 10),scale=(0.05,4,4),tex_id=4,rot=(0,0,90)))
        add(Cube(app, pos=(17, 4, 10),scale=(0.05,4,4),tex_id=4,rot=(0,0,0)))

        # Крыша
        add(Cube(app, pos=(11, 10, 10),scale=(3,0.1,5),tex_id=3,rot=(0,0,45)))
        add(Cube(app, pos=(15, 10, 10),scale=(3,0.1,5),tex_id=3,rot=(0,0,-45)))

        add(Triangle(app, pos=(13, 10, 14),scale=(4,2,2),tex_id=5))
        add(Triangle(app, pos=(13, 10, 6),scale=(4,2,2),tex_id=5))

        # Подгрузим модельку машины
        #add(Car(app, pos=(0, 0, 0),scale=(1,1,1),tex_id='car',rot=(0,0,0)))
        add(Car2(app, pos=(0, 0.2, 0),scale=(0.01,0.01,0.01),tex_id='car2',rot=(0,90,0))) 


        # Тепер сделаем что то вроде парка. Цель - 2 дерева и скамья. Будем использовать модельки
        add(TreeGr(app, pos=(-10, 0.2, -5),scale=(0.2,0.2,0.2),tex_id='green',rot=(0,0,0))) 
        add(TreeBark(app, pos=(-10, 0.2, -5),scale=(0.2,0.2,0.2),tex_id='bark',rot=(0,0,0))) 

        add(TreeGr(app, pos=(-10, 0.2, 5),scale=(0.2,0.2,0.2),tex_id='green',rot=(0,0,0))) 
        add(TreeBark(app, pos=(-10, 0.2, 5),scale=(0.2,0.2,0.2),tex_id='bark',rot=(0,0,0))) 

        # Теперь скамейка
        add(Bench(app, pos=(-10, 0, 0),scale=(0.01,0.01,0.01),tex_id='whiteBench',rot=(0,90,0))) 

    def update(self):
        pass
