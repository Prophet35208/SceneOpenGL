import glm

# Наш класс источника света
class Light:
    def __init__(self, position=(50, 50, -10), color=(1, 1, 1)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        self.direction = glm.vec3(0, 0, 0)
        # Параметры для модели освещения Фонга
        self.Ia = 0.06 * self.color  # Окружающий свет
        self.Id = 0.8 * self.color  # Рассеивующийся свет
        self.Is = 1.0 * self.color  # Отражение света от гладкой поверхности
        # Видовая матрица относительно источника света
        self.m_view_light = self.get_view_matrix()

    # Получаем видовую матрицу с точки зрения итосчника света
    def get_view_matrix(self):
        return glm.lookAt(self.position, self.direction, glm.vec3(0, 1, 0))