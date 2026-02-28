time_units = ["second", "minute", "hour", "day", "week", "month"]
step_factors = [60, 60, 24, 7, 4]

class Basicdata:
    
    def __init__(self):
        self.a = 0
        self.original = None
        self.b = 0
        self.converter = None
        
    def get_numbers(self):
        self.a = int(input("input number:"))
        self.b = int(input("input number:"))
        
    def extract_numbers(self,a,b):
        self.a = a
        self.b = b

    def  input_data(self):
        self.a = int(input("input number:"))
        self.original = input("input time type:")
        self.converter = input("input converted time type:")   

class Calculator(Basicdata):
    
    def add(self):
        return self.a+self.b
    
    def substract(self):
        return self.a-self.b
    
    def multiply(self):
        return self.a*self.b
    
    def divide(self):
        return self.a/self.b
    
class Timeconversion(Calculator):
    
    def get_unit_index(self, unit):
        try:
            return time_units.index(unit)
        except ValueError:
            return None

    def convert(self):
        orig_idx = self.get_unit_index(self.original)
        conv_idx = self.get_unit_index(self.converter)

        if orig_idx is None or conv_idx is None:
            print("Invalid time unit entered.")
            return None

        value = self.a
        steps = conv_idx - orig_idx

        if steps > 0:
            
            for i in range(orig_idx, conv_idx):
                factor = step_factors[i]   
                self.a = value
                self.b = factor
                value = self.divide()
        elif steps < 0:
            
            for i in range(conv_idx, orig_idx):
                factor = step_factors[i]   
                self.a = value
                self.b = factor
                value = self.multiply()

        return value

def main():
    
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Convert time")
    choice = int(input("Enter your choice: "))
    
    if choice == 5:
        converter = Timeconversion()
        converter.input_data()             
        result = converter.convert()
        if result is not None:
            print(f"Converted value: {result}")
    else:
    
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
