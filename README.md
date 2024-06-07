# OptiStockScreener

## Overview
Welcome to the OptiStockScreener repository! This project is part of our MGT 4100 course, where we are participating in a stock game competition. Our goal is to find the optimal portfolio to win the competition. To achieve this, we are using a stock screener to determine the best values that maximize our portfolio returns.

## Objective
The primary objective of this project is to identify the optimal stock screener values to construct a winning portfolio. By running our setup script, we aim to find the optimal screener weights that will help us achieve the highest returns.

## Setup Instructions

### Step 1: Clone the Repository
First, clone the repository to your local machine using the following command:
- bash: `git clone https://github.com/yourusername/OptiStockScreener.git`

### Step 2: Create a Virtual Environment
Navigate to the repository directory and create a Python virtual environment:
- bash: `cd OptiStockScreener`
- bash: `python3.12 -m venv .venv`

### Step 3: Activate the Virtual Environment
Activate the virtual environment:

On Windows:
- bash: `.venv\Scripts\activate`

On macOS and Linux:
- bash: `source .venv/bin/activate`

### Step 4: Install Dependencies
Install the required dependencies from the `requirements.txt` file:
- bash: `pip install -r requirements.txt`

### Step 5: Run the Main Script
Execute the main script to start the optimization process and find the optimal screener weights:
- bash: `python src/main.py`

## Running the Script
The script will iterate through various combinations of screener settings, apply them to our stock data, and determine the optimal set of filters based on backtested returns. The output will include the best backtested portfolio value and the optimal filters used to achieve this value.

## Output Example
Best backtested portfolio value: 125000.0
Optimal filters:
price: (50, 100)
market_cap: 'large'
dividend_yield: (2, 4)
average_volume: (100000, 500000)

## Conclusion
By following these steps, you can replicate our setup and run the optimization script to find the best stock screener values. Let's win this stock game competition in MGT 4100 with the optimal portfolio!

Happy investing! 🚀📈

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
