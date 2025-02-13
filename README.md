# Medical Data Visualizer

This project is a Medical Data Visualizer that utilizes Python libraries such as Pandas, Matplotlib, and Seaborn to analyze and visualize medical examination data. The goal of this project is to explore relationships between various health metrics and cardiovascular disease outcomes.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [License](#license)

## Features

- Visualize medical examination data using various charts.
- Analyze relationships between cardiovascular disease and health metrics.
- Create categorical plots and correlation heatmaps.
- Normalize data for better visualization.
  
## Technologies Used

- Python 3.x
- Pandas for data manipulation
- Matplotlib for plotting
- Seaborn for statistical data visualization

## Installation

To run this project, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

git clone https://github.com/freeCodeCamp/boilerplate-medical-data-visualizer.git
cd boilerplate-medical-data-visualizer


### Step 2: Install Dependencies

You will need to install the required libraries. You can do this using pip:

pip install pandas matplotlib seaborn


## Usage

To use the Medical Data Visualizer, run the `main.py` script. This script will execute the analysis and generate visualizations based on the medical examination data.

### Example Command Line Usage

1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:
   python main.py


## Functionality

The main functionalities of this project include:

1. **Data Loading**: The program reads medical examination data from `medical_examination.csv`.
2. **Data Processing**:
   - Adds an `overweight` column by calculating BMI.
   - Normalizes values for cholesterol and glucose levels.
   - Cleans the data by filtering out incorrect entries based on defined criteria.
3. **Visualization**:
   - Draws categorical plots using Seaborn's `catplot()` to show counts of health features split by cardiovascular disease presence.
   - Creates a correlation matrix heatmap to visualize relationships between different health metrics.

