from vbo import VBO
from shader_program import ShaderProgram

# Здесь мы компануем наши раннее определённые vbo в vao
class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        # Подгружаем шейдеры и параметры для них
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # Далее для каждого объекта мы определяем два vao: для теней и для самого объекта
        # Обычная VAO. Использует дефолтный шейдер
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cube'])
        
        self.vaos['shadow_cube'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['cube'])
        
        self.vaos['triangle'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['triangle'])
        
        self.vaos['shadow_triangle'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['triangle'])
        
        self.vaos['car'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['car'])
        
        self.vaos['shadow_car'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['car'])
        
        self.vaos['car2'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['car2'])
        
        self.vaos['shadow_car2'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['car2'])
        
        self.vaos['treeBark'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['treeBark'])
        
        self.vaos['shadow_treeBark'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['treeBark'])
        
        self.vaos['treeGr'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['treeGr'])
        
        self.vaos['shadow_treeGr'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['treeGr'])

        self.vaos['bench'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['bench'])
        
        self.vaos['shadow_bench'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['bench'])

    # Вовращаем полученные vao
    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()