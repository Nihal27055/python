
from colorama import Fore, Style
import random

class Fruits:
    def __init__(self):
        self.fruits = []
    
    def append(self, fruit):
        self.fruits.append(fruit)
    
    def pop(self, index=-1):
        if self.fruits:
            return self.fruits.pop(index)
        return None
    
    def clear(self):
        self.fruits.clear()
    
    def __len__(self):
        return len(self.fruits)

    def print_fruit_list(self):
        """Prints the list of fruits with changing colors"""
        colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
        for fruit in self.fruits:
            color = random.choice(colors)  # Choose a random color for each fruit
            print(color + fruit + Style.RESET_ALL)  # Print the fruit in color and reset style


if __name__ == "__main__":
    my_fruits = Fruits()
    
    # Adding fruits to the collection
    my_fruits.append("apple")
    my_fruits.append("Banana")
    my_fruits.append("Oranges")
    my_fruits.append("Mango")
    my_fruits.append("Grapes")
    
    # Print the list of fruits
    my_fruits.print_fruit_list()







    