# Coffee Machine ☕

A simple Python console-based Coffee Machine project that simulates a coffee vending machine. Users can order coffee, insert coins, check available resources, and receive change if extra money is inserted.

## Features

* Order Espresso, Latte, or Cappuccino
* Resource management (water, milk, coffee)
* Coin-based payment system
* Change calculation
* Resource report generation
* Machine shutdown option

## Menu

| Coffee     | Water (ml) | Milk (ml) | Coffee (g) | Cost ($) |
| ---------- | ---------- | --------- | ---------- | -------- |
| Espresso   | 50         | 0         | 18         | 1.50     |
| Latte      | 200        | 150       | 24         | 2.50     |
| Cappuccino | 250        | 100       | 24         | 3.00     |

## Available Resources

Initial machine resources:

* Water: 300 ml
* Milk: 200 ml
* Coffee: 100 g
* Money: $0

## Coin Values

| Coin    | Value ($) |
| ------- | --------- |
| Penny   | 0.01      |
| Nickel  | 0.05      |
| Dime    | 0.10      |
| Quarter | 0.25      |

## How It Works

1. User selects a drink:

   * espresso
   * latte
   * cappuccino

2. Machine checks whether enough resources are available.

3. User inserts coins.

4. Machine verifies payment:

   * If payment is sufficient, coffee is prepared.
   * If payment is insufficient, the order is rejected.

5. If extra money is inserted, change is returned.

6. Resources are updated after every successful purchase.

## Commands

### View Report

Type:

```text
report
```

Displays current resources and money collected.

### Turn Off Machine

Type:

```text
off
```

Stops the coffee machine.

## Running the Project

### Clone Repository

```bash
git clone <repository-url>
```

### Run Program

```bash
python coffee_machine.py
```

## Example Usage

```text
What would you like? (espresso/latte/cappuccino): latte

How many penny?: 0
How many dime?: 0
How many nickel?: 0
How many quarters?: 12

Here is $0.50 in change.
Here is your latte. Enjoy!
```

## Project Concepts Used

* Python Dictionaries
* Functions
* Conditional Statements
* Loops
* User Input
* Resource Management
* Simple Transaction Processing

## Future Improvements

* Better resource shortage messages
* Support for refilling resources
* Menu display command
* Transaction history
* Object-Oriented Programming (OOP) version
* GUI version using Tkinter

## Author

Created as a Python learning project to practice functions, dictionaries, loops, and conditionals.
