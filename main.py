class Basicdata:
    
    def __init__(self):
        self.a = 0
        self.b = 0
        
    def get_numbers(self):
        self.a = int(input("input number:"))
        self.b = int(input("input number:"))

class Calculator(Basicdata):
    
    def add(self):
        return self.a+self.b
    
    def substract(self):
        return self.a-self.b
    
    def multiply(self):
        return self.a*self.b
    
    def divide(self):
        return self.a/self.b

def main():
    
    my_calculator = Calculator()
    
    choice = int(input("Enter your choice: 1. Add 2. Subtract 3. Multiply 4. Divide: "))

    my_calculator.get_numbers()

    if choice == 1:
        print(my_calculator.add())
    elif choice == 2:
        print(my_calculator.subtract())
    elif choice == 3:
        print(my_calculator.multiply())
    elif choice == 4:
        print(my_calculator.divide())
    


if __name__ == "__main__":
    main()
