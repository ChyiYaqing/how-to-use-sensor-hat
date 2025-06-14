from sense_hat import SenseHat
import time

sense = SenseHat()

X = [255, 0, 0] # 红色
O = [255, 255, 255] # 白色

# ?
question_mark = [
    O, O, O, X, X, O, O, O,
    O, O, X, O, O, X, O, O,
    O, O, O, O, O, X, O, O,
    O, O, O, O, X, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, X, O, O, O, O
]

sense.set_pixels(question_mark)

time.sleep(5)

sense.clear()  # 清除LED矩阵