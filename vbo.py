import numpy as np
import moderngl as mgl
import pywavefront

# Наследуемый класс, в котором мы определяем VBO (буфер вершин) наших объектов. 
# Класс обётка для других vbo
class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        self.vbos['cube'] = CubeVBO(ctx)
        self.vbos['triangle'] = TriangleVBO(ctx)
        self.vbos['car'] = CarVBO(ctx)
        self.vbos['car2'] = Car2VBO(ctx)
        self.vbos['treeBark'] = TreeBark(ctx)
        self.vbos['treeGr'] = TreeGr(ctx)
        self.vbos['bench'] = Bench(ctx)        

    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]

# Базовый класс
class BaseVBO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = self.get_vbo()
        self.format: str = None
        self.attribs: list = None

    def get_vertex_data(self): ...

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()





# vbo треугольника
class TriangleVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Метод для компоновки данных вершин из набора неповторяющихся вершин и индексов
    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    # Данные вершин
    def get_vertex_data(self):
        vertices = [
        (0, 1, 0),  
        (-1, -1, 0),
        (1, -1, 0)  
        ]   

        indices = [(0, 1, 2)]
        vertex_data = self.get_data(vertices, indices)
        [(-0.6, -0.8, 0.0),(0.6, -0.8, 0.0),(0.0, 0.8, 0.0)]

        tex_coord_vertices = [(0, 0), (1, 0), (0.5, 1)]
        tex_coord_indices = [(0, 1, 2)]
        tex_coord_data = self.get_data(tex_coord_vertices, tex_coord_indices)

        normals = [(0, 0, 1)] * 3
        normals = np.array(normals, dtype='f4').reshape(3, 3)

        # Дописываем нормали и текстурные координаты
        vertex_data = np.hstack([normals, vertex_data])
        vertex_data = np.hstack([tex_coord_data, vertex_data])
        return vertex_data




# vbo первой машины, текстуры нет
class CarVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '3f 3f'
        self.attribs = ['in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/car/Car.obj', cache=True, parse=True)
        all_vertices = []
       
        for name, data in objs.materials.items():
            vertices = np.array(data.vertices, dtype='f4')
            all_vertices.append(vertices)

        if all_vertices:
            vertex_data = np.concatenate(all_vertices)
        else:
            vertex_data = np.array([], dtype='f4')
        return vertex_data

# Вторая машина, с текстурой
class Car2VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']


    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/car2/Formula1mesh.obj', cache=True, parse=True)
        all_vertices = []
       
        for name, data in objs.materials.items():
            vertices = np.array(data.vertices, dtype='f4')
            all_vertices.append(vertices)

        if all_vertices:
            vertex_data = np.concatenate(all_vertices)
        else:
            vertex_data = np.array([], dtype='f4')
        return vertex_data        


class TreeBark(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']


    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/tree/Lowpoly_tree_sample.obj', cache=True, parse=True)
        obj = objs.materials.popitem()
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class TreeGr(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']


    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/tree/Lowpoly_tree_sample.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    

class Bench(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']


    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/bench/Bench_HighRes.obj', cache=True, parse=True)
        all_vertices = []
       
        for name, data in objs.materials.items():
            vertices = np.array(data.vertices, dtype='f4')
            all_vertices.append(vertices)

        if all_vertices:
            vertex_data = np.concatenate(all_vertices)
        else:
            vertex_data = np.array([], dtype='f4')
        return vertex_data  





# vbo нашего куба, заполняется по аналогии с треугольником, только сейчас у нас 3д объект
class CubeVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), ( 1, -1,  1), (1,  1,  1), (-1, 1,  1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), ( 1, 1, -1)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        vertex_data = self.get_data(vertices, indices)

        tex_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                             (0, 2, 3), (0, 1, 2),
                             (0, 1, 2), (2, 3, 0),
                             (2, 3, 0), (2, 0, 1),
                             (0, 2, 3), (0, 1, 2),
                             (3, 1, 2), (3, 0, 1),]
        tex_coord_data = self.get_data(tex_coord_vertices, tex_coord_indices)

        normals = [( 0, 0, 1) * 6,
                   ( 1, 0, 0) * 6,
                   ( 0, 0,-1) * 6,
                   (-1, 0, 0) * 6,
                   ( 0, 1, 0) * 6,
                   ( 0,-1, 0) * 6,]
        normals = np.array(normals, dtype='f4').reshape(36, 3)

        vertex_data = np.hstack([normals, vertex_data])
        vertex_data = np.hstack([tex_coord_data, vertex_data])
        return vertex_data













