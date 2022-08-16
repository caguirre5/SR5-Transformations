from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, tryshader, unlit, gourad, toon, glow, textureBlend

width = 540
height = 540

rend = Renderer(width, height)

rend.dirLight = V3(-1, 0, 1)

rend.glClearColor(0.7, 0.7, 0.7)
rend.glClear()

# LowAngle Cam Position -> V3(-2, -1.5, -2)
# HighAngle Cam Position -> V3(0, 8, -3.5)
# DutchAngle Cam Position -> V3(2, 1, -2)

modelPosition = V3(0.8, -2, -4)
modelPositionFixed = V3(0, -0.4, -4)

rend.glLookAt(modelPositionFixed, V3(2, 1, -2))

rend.active_texture = Texture("models/Teddy.bmp")
rend.active_shader = tryshader
rend.glLoadModel("models/Teddy.obj",
                 translate=modelPosition,
                 scale=V3(3, 3, 3),
                 rotate=V3(0, 90, 0))

rend.glFinish("output.bmp")
