from sympy import *
import matplotlib.pyplot as plt
import numpy as np

# First, graph the equation in order to get an idea of a good guess for zero
X = np.array(range(-20, 20, 1))
Y = np.asarray([exp(4 * numb) - 4 * exp(2 * numb) + 4 for numb in X])

plt.plot(X, Y)
plt.ylim(-2, 10)
plt.show()


class NewtonRaphson(object):
    def __init__(self, f, guess=1):
        self.guess = guess
        # convert x to Symbol format
        self.x = Symbol('x')
        self.f = f

    def get_guess(self):
        return self.guess

    def get_x(self):
        return self.x

    def get_f(self):
        return self.f

    def get_derivative(self):
        f_prime = self.f.diff(x)
        return f_prime

    def get_zero(self):
        f_prime = self.get_derivative()
        f_prime = lambdify(self.x, f_prime)
        self.f = lambdify(self.x, self.f)
        self.x = self.guess
        while abs(self.f(self.x)) > 0.005:
            self.x = self.x - (f_prime(self.x)) / (self.f(self.x))
            print(self.x)
            print(self.f(self.x))
        print(self.x)
        print('with an x value of {} you get an approximate zero of {}'.format(self.x, self.f(self.x)))


x = Symbol('x')
f = NewtonRaphson(exp(4 * x) - 4 * exp(2 * x) + 4, -1)
print(f.get_derivative())
f.get_zero()
