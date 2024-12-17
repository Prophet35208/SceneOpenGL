import pygame as pg
import moderngl as mgl
import glm

# Класс для подгрузки текстур
class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        # Словарь для текстур
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/close-up-bright-glitter.jpg')
        self.textures[1] = self.get_texture(path='textures/dirt.jpg')
        self.textures[2] = self.get_texture(path='textures/house_front.jpg')
        self.textures[3] = self.get_texture(path='textures/house_roof.jpg')
        self.textures[4] = self.get_texture(path='textures/house_back.jpg')
        self.textures[5] = self.get_texture(path='textures/roofT.jpg')
        self.textures['car'] = self.get_texture(path='objects/car/ser.png')
        self.textures['car2'] = self.get_texture(path='objects/car2/formula1_DefaultMaterial_Diffuse.png')
        self.textures['bark'] = self.get_texture(path='objects/tree/bark_0004.jpg')
        self.textures['green'] = self.get_texture(path='objects/tree/green.jpg')
        self.textures['whiteBench'] = self.get_texture(path='objects/bench/white_bench.jpg')
        self.textures['depth_texture'] = self.get_depth_texture()
        

    # Получаем z- буффер
    def get_depth_texture(self):
        depth_texture = self.ctx.depth_texture(self.app.WIN_SIZE)
        depth_texture.repeat_x = False
        depth_texture.repeat_y = False
        return depth_texture

    # Получаем текстуру из файла
    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]