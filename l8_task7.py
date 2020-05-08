"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата."""


class ComplexNumber:
    def __init__(self, real_num, imaginary):
        self.real_num = real_num
        self.imaginary = imaginary

    def __add__(self, other):
        return complex(self.real_num + other.real_num, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return complex(self.real_num * other.real_num, self.imaginary * other.imaginary)


z1 = ComplexNumber(1, 2)
z2 = ComplexNumber(3, 4)
print(z1 + z2)
print(z1 * z2)

