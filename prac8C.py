class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def add(self, other):
        return Complex(self.real + other.real, self.img + other.img)
    
    def display(self):
        print(f"{self.real} + {self.img}i")

n = int(input("Enter the number of complex numbers (N >= 2): "))
if n < 2:
    print("N should be at least 2.")
else:
    real = float(input("Enter the real part of complex number 1: "))
    imag = float(input("Enter the imaginary part of complex number 1: "))
    result = Complex(real, imag)

    for i in range(2, n + 1):
        real = float(input(f"Enter the real part of complex number {i}: "))
        imag = float(input(f"Enter the imaginary part of complex number {i}: "))
        result = result.add(Complex(real, imag))

    print("The sum of the complex numbers is: ", end="")
    result.display()