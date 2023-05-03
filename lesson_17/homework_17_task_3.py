# Task 3
#
# Fraction
#
# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з належною
# перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій та операції порівняння
# між об'єктами класу Fraction

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'Fraction({self.numerator}, {self.denominator})'

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise ValueError("Другий аргумент не є дробом")
        common_denominator = self.denominator * other.denominator / evklid(self.denominator, other.denominator)
        result_num = (self.numerator * (common_denominator / self.denominator)) + \
                     (other.numerator * (common_denominator / other.denominator))
        return Fraction(int(result_num), int(common_denominator))

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise ValueError("Другий аргумент не є дробом")
        common_denominator = self.denominator * other.denominator / evklid(self.denominator, other.denominator)
        result_num = (self.numerator * (common_denominator / self.denominator)) - \
                     (other.numerator * (common_denominator / other.denominator))
        return Fraction(int(result_num), int(common_denominator))

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise ValueError("Другий аргумент не є дробом")
        mul_numerator = self.numerator * other.numerator
        mul_denominator = self.denominator * other.denominator
        result_num = mul_numerator / evklid(mul_numerator, mul_denominator)
        result_denom = mul_denominator / evklid(mul_numerator, mul_denominator)
        return Fraction(int(result_num), int(result_denom))

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise ValueError("Другий аргумент не є дробом")
        div_numerator = self.numerator * other.denominator
        div_denominator = self.denominator * other.numerator
        result_num = div_numerator / evklid(div_numerator, div_denominator)
        result_denom = div_denominator / evklid(div_numerator, div_denominator)
        return Fraction(int(result_num), int(result_denom))

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            raise ValueError("Другий аргумент не є дробом")
        common_denominator = self.denominator * other.denominator / evklid(self.denominator, other.denominator)
        result = self.numerator * (common_denominator / self.denominator) < \
                 other.numerator * (common_denominator / other.denominator)
        return result

    def __le__(self, other):
        if not isinstance(other, Fraction):
            raise ValueError("Другий аргумент не є дробом")
        common_denominator = self.denominator * other.denominator / evklid(self.denominator, other.denominator)
        result = self.numerator * (common_denominator / self.denominator) <= \
                 other.numerator * (common_denominator / other.denominator)
        return result

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            raise ValueError("Другий аргумент не є дробом")
        common_denominator = self.denominator * other.denominator / evklid(self.denominator, other.denominator)
        result = self.numerator * (common_denominator / self.denominator) > \
                 other.numerator * (common_denominator / other.denominator)
        return result

    def __ge__(self, other):
        if not isinstance(other, Fraction):
            raise ValueError("Другий аргумент не є дробом")
        common_denominator = self.denominator * other.denominator / evklid(self.denominator, other.denominator)
        result = self.numerator * (common_denominator / self.denominator) >= \
                 other.numerator * (common_denominator / other.denominator)
        return result

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            raise ValueError("Другий аргумент не є дробом")
        common_denominator = self.denominator * other.denominator / evklid(self.denominator, other.denominator)
        result = self.numerator * (common_denominator / self.denominator) == \
                 other.numerator * (common_denominator / other.denominator)
        return result

    def __ne__(self, other):
        if not isinstance(other, Fraction):
            raise ValueError("Другий аргумент не є дробом")
        common_denominator = self.denominator * other.denominator / evklid(self.denominator, other.denominator)
        result = self.numerator * (common_denominator / self.denominator) != \
                 other.numerator * (common_denominator / other.denominator)
        return result


def evklid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x<y)
    print(x>y)
    print(x==y)
    assert (x + y) == Fraction(3, 4)