class Delay2Machine:
    def __init__(self, val0, val1):
        # Начальное состояние хранит значения для первых двух выводов
        self.state = (val0, val1)

    def step(self, inp):
        # Вывод — это самое старое значение в памяти (элемент с индексом 0)
        output = self.state[0]
        # Обновляем состояние: сдвигаем память и записываем новый вход в конец
        self.state = (self.state[1], inp)
        return output

    def transduce(self, inputs):
        return [self.step(inp) for inp in inputs]

# Проверка работы
sm = Delay2Machine(100, 10)

# Подаем 6 элементов на вход, чтобы получить 6 элементов на выходе
inputs = [1, 2, 10, 20, 0, 0]
output = sm.transduce(inputs)

print(output)  # Результат: [100, 10, 1, 2, 10, 20]
