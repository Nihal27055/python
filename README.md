# Fruits Collection

A simple Python library for managing and displaying a collection of fruits with colorful output.

## Features

- Add fruits to your collection
- Remove fruits from your collection
- Clear your entire collection
- Display fruits with random colorful text

## Requirements

- Python 3.x
- colorama

## Installation

Install the required dependencies:

```bash
pip install colorama
```

## Usage

```python
from fruits import Fruits

# Create a new fruits collection
my_fruits = Fruits()

# Add fruits to the collection
my_fruits.append("Apple")
my_fruits.append("Banana")
my_fruits.append("Orange")
my_fruits.append("Mango")
my_fruits.append("Grapes")

# Display the fruits with colorful text
my_fruits.print_fruit_list()

# Get the number of fruits
print(f"Number of fruits: {len(my_fruits)}")

# Remove the last fruit
removed_fruit = my_fruits.pop()
print(f"Removed fruit: {removed_fruit}")

# Clear all fruits
my_fruits.clear()
```

## Methods

- `append(fruit)`: Add a fruit to the collection
- `pop(index=-1)`: Remove and return a fruit at the given index (default is the last item)
- `clear()`: Remove all fruits from the collection
- `__len__()`: Get the number of fruits in the collection
- `print_fruit_list()`: Display all fruits with random colors

## License

MIT 