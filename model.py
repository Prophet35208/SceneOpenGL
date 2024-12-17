import moderngl as mgl
import numpy as np
import glm

# В данном файле предоставлены модели, из которых далее создаются объекты на сцене

# Базовая модель, без теней
class BaseModel:
    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.app = app
        self.pos = pos
        self.vao_name = vao_name
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera

    def update(self): ...
    
    # В соответствии с начальными параметрами изменяем размер объекта, поворачиваем его
    def get_model_matrix(self):
        m_model = glm.mat4()
        # Получим текущее состояние
        m_model = glm.translate(m_model, self.pos)
        # Вертим
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        # Изменяем размер модели 
        m_model = glm.scale(m_model, self.scale)
        return m_model

    # Рендерим объект
    def render(self):
        self.update()
        self.vao.render()

# Расширенная модель, теперь с тенями
class ExtendedBaseModel(BaseModel):

    def __init__(self, app, vao_name, tex_id, pos, rot, scale):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    # При обновлении выполянем перерасчёт матриц. Точнее записываем их в словарь program для дальнейшего ипользования в шейдерах
    def update(self):
        self.texture.use(location=0)
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    # Перерасчитываем параметры теней модели
    def update_shadow(self):
        self.shadow_program['m_model'].write(self.m_model)

    # Рендерим тени
    def render_shadow(self):
        self.update_shadow()
        self.shadow_vao.render()

    # Дополнительная инициализация для теней
    def on_init(self):
        # Запоминаем данные z-буфера относительно позиции источника света
        self.program['m_view_light'].write(self.app.light.m_view_light)
        # Разрешение текстуры
        self.program['u_resolution'].write(glm.vec2(self.app.WIN_SIZE))
        # Z-буфер текстуры
        self.depth_texture = self.app.mesh.texture.textures['depth_texture']
        self.program['shadowMap'] = 1
        self.depth_texture.use(location=1)
        # Тени
        self.shadow_vao = self.app.mesh.vao.vaos['shadow_' + self.vao_name]
        self.shadow_program = self.shadow_vao.program
        # Определяем параметры для шейдеров shadow_map
        self.shadow_program['m_proj'].write(self.camera.m_proj)
        self.shadow_program['m_view_light'].write(self.app.light.m_view_light)
        self.shadow_program['m_model'].write(self.m_model)
        # Текстуры
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use(location=0)
        # Матрицы для камеры
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # Параметры света
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)


# Наш основной строительный примитив. 
# Благодаря параметрам pos, rot и scale для него реализуется: начальная позиция (координаты центра), начальный угол, масштаб (позволяет легко получить любой прямоугольник)
# По умолчанию квдарат 1 на 1 на 1
class Cube(ExtendedBaseModel):
    def __init__(self, app, vao_name='cube', tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Модель треугольника
class Triangle(ExtendedBaseModel):
    def __init__(self, app, vao_name='triangle', tex_id=0, pos=(3, 3, 3), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Первая машина (не используется, нет хорошей текстуры)
class Car(ExtendedBaseModel):
    def __init__(self, app, vao_name='car', tex_id='car',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Вторая машина, в этот раз с хорошей текстурой
class Car2(ExtendedBaseModel):
    def __init__(self, app, vao_name='car2', tex_id='car2',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class TreeBark(ExtendedBaseModel):
    def __init__(self, app, vao_name='treeBark', tex_id='treeBark',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class TreeGr(ExtendedBaseModel):
    def __init__(self, app, vao_name='treeGr', tex_id='treeGr',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Bench(ExtendedBaseModel):
    def __init__(self, app, vao_name='bench', tex_id='whiteBench',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)




















