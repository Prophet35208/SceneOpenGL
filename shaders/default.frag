#version 330 core

layout (location = 0) out vec4 fragColor;

in vec2 uv_0;
in vec3 normal; // Вектор нормалей
in vec3 fragPos; // Цвет фрагмента
in vec4 shadowCoord; // Координаты теней

// 3 характеристики освещения Фонга
struct Light {
    vec3 position;
    vec3 Ia;
    vec3 Id;
    vec3 Is;
};

# 
uniform Light light;
uniform sampler2D u_texture_0;
uniform vec3 camPos;
uniform sampler2DShadow shadowMap;
uniform vec2 u_resolution;

// Вычисляет смещение в текстурных координатах, основываясь на размере пикселя текстуры
float lookup(float ox, float oy) {
    vec2 pixelOffset = 1 / u_resolution;
    return textureProj(shadowMap, shadowCoord + vec4(ox * pixelOffset.x * shadowCoord.w,
                                                     oy * pixelOffset.y * shadowCoord.w, 0.0, 0.0));
}

// Расчёт мягких теней
float getSoftShadowX16() {
    float shadow;
    float swidth = 1.0;
    float endp = swidth * 1.5;
    for (float y = -endp; y <= endp; y += swidth) {
        for (float x = -endp; x <= endp; x += swidth) {
            shadow += lookup(x, y);
        }
    }
    return shadow / 16.0;
}


// Выборка значений из карты теней
vec3 getLight(vec3 color) {
    vec3 Normal = normalize(normal);

    // По формулам считаем 3 параметры цвета
    vec3 ambient = light.Ia;

    vec3 lightDir = normalize(light.position - fragPos);
    float diff = max(0, dot(lightDir, Normal));
    vec3 diffuse = diff * light.Id;

    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float spec = pow(max(dot(viewDir, reflectDir), 0), 32);
    vec3 specular = spec * light.Is;

    float shadow = getSoftShadowX16();

    // Полученные параметры дают нам конечный цвет
    return color * (ambient + (diffuse + specular) * shadow);
}


void main() {
    // Гамма коррекция
    float gamma = 2.2;

    vec3 color = texture(u_texture_0, uv_0).rgb; // Начальное значение цвета
    color = pow(color, vec3(gamma)); // Перед гамма коррекцией
    color = getLight(color); // После обработки светом
    color = pow(color, 1 / vec3(gamma)); // После гамма коррекции

    fragColor = vec4(color, 1.0); // Назначаем полученный цвет фрагменту
}










