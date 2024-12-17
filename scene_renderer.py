
# Ф-ия рендера сцены
class SceneRenderer:
    def __init__(self, app):
        # Получаем данные контекста, мешей и сцены
        self.app = app
        self.ctx = app.ctx
        self.mesh = app.mesh
        self.scene = app.scene
        # Буффер глубины
        self.depth_texture = self.mesh.texture.textures['depth_texture']
        self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)

    # Рендерим тени
    def render_shadow(self):
        self.depth_fbo.clear()
        self.depth_fbo.use()
        for obj in self.scene.objects:
            obj.render_shadow()

    # Рендерим сами объекты
    def main_render(self):
        self.app.ctx.screen.use()
        for obj in self.scene.objects:
            obj.render()

    # Обёртка двух прошлых методов
    def render(self):
        self.scene.update()
        self.render_shadow()
        self.main_render()

    def destroy(self):
        self.depth_fbo.release()

