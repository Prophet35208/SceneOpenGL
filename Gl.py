import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene
from scene_renderer import SceneRenderer
import math

class OpenGl:
    def __init__(self, win_size=(1600, 900)):
        # Базовая Инициализация
        pg.init()
        self.WIN_SIZE = win_size
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # Настройки мыши, чтобы не вылезала из окна
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST)
        # Создаём объект времени для анимации
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # Подключам свет
        self.light = Light()
        # Задаём камеру
        self.camera = Camera(self,position=(0,10,4))
        # Подключаем объекты
        self.mesh = Mesh(self)
        # Подключаем сцену
        self.scene = Scene(self)
        # Подключаем рендер сцены
        self.scene_renderer = SceneRenderer(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                # Ивент на выход
                self.mesh.destroy()
                self.scene_renderer.destroy()
                pg.quit()
                sys.exit()
                
    # Ф-ия, делегирующая рендер scene_renderer-у
    def render(self):
        # Очищаем буффер, заполняеми его цветом фона
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        # Рендерим сцену
        self.scene_renderer.render()
        # Свапаем текущий буффер на отрендеренный
        pg.display.flip()


    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001
    # Запуск приложения
    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)


if __name__ == '__main__':
    app = OpenGl()
    app.run()






























