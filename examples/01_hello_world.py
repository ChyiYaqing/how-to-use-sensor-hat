from sense_hat import SenseHat

# 初始化 Sense HAT
sense = SenseHat()

# 设置低亮度模式
sense.low_light = True

sense.show_message("Hello World!", text_colour=(255, 0, 0), back_colour=(0, 0, 255))

# 关闭LED矩阵
sense.clear() 