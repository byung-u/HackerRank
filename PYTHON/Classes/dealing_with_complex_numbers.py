#!/usr/bin/env python3

import sys
from math import sqrt


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        if self.imaginary + no.imaginary >= 0:
            result = '%.2f+%.2fi' % (self.real + no.real, self.imaginary + no.imaginary)
        else:
            result = '%.2f%.2fi' % (self.real + no.real, self.imaginary + no.imaginary)
        return result

    def __sub__(self, no):
        if self.imaginary - no.imaginary >= 0:
            result = '%.2f+%.2fi' % (self.real - no.real, self.imaginary - no.imaginary)
        else:
            result = '%.2f%.2fi' % (self.real - no.real, self.imaginary - no.imaginary)
        return result

    def __mul__(self, no):
        if self.real * no.imaginary + self.imaginary * no.real >= 0:
            result = '%.2f+%.2fi' % ((self.real * no.real - self.imaginary * no.imaginary), (self.real * no.imaginary + self.imaginary * no.real))
        else:
            result = '%.2f%.2fi' % ((self.real * no.real - self.imaginary * no.imaginary), (self.real * no.imaginary + self.imaginary * no.real))
        return result

    def __truediv__(self, no):
        if ((self.imaginary * no.real - self.real * no.imaginary) / (no.real ** 2 + no.imaginary ** 2)) >= 0:
            result = '%.2f+%.2fi' % (((self.real * no.real + self.imaginary * no.imaginary) / (no.real ** 2 + no.imaginary ** 2)), ((self.imaginary * no.real - self.real * no.imaginary) / (no.real ** 2 + no.imaginary ** 2)))
        else:
            result = '%.2f%.2fi' % (((self.real * no.real + self.imaginary * no.imaginary) / (no.real ** 2 + no.imaginary ** 2)), ((self.imaginary * no.real - self.real * no.imaginary) / (no.real ** 2 + no.imaginary ** 2)))
        return result

    def mod(self):
        result = '%.2f+0.00i' % sqrt(self.real ** 2 + self.imaginary ** 2)
        return result

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    C = input().split( )
    D = input().split( )
    c = Complex(float(C[0]), float(C[1]))
    d = Complex(float(D[0]), float(D[1]))
    print(c + d)
    print(c - d)
    print(c * d)
    print(c / d)
    print(c.mod())
    print(d.mod())

