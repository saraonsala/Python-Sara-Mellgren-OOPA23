# Python-Sara-Mellgren-OOPA23
# Python Learning Projects

## Overview

This repository contains projects, exercises, and examples that I worked on during my journey to learn Python programming. These projects span various topics, from basic Python syntax to more advanced concepts like object-oriented programming, data manipulation, and even some initial AI experiments.

## Projects

1. **Basic Python Exercises**:  
   Fundamental exercises to learn the syntax of Python, including data types, loops, functions, and control flow. These exercises helped me build a solid foundation in Python.

2. **Object-Oriented Programming (OOP)**:  
   Projects and exercises that focus on OOP concepts such as classes, inheritance, polymorphism, and encapsulation. These projects were essential in understanding how to create more structured and maintainable code.

3. **Data Analysis**:  
   Using libraries like Pandas and Matplotlib to analyze and visualize data. This includes smaller data sets where I practiced techniques such as data cleaning, aggregation, and visualization.

4. **Mini Projects**:

   - **Calculator App**: A simple command-line calculator to practice functions and basic operations.
   - **To-Do List**: A small to-do list application that helps track tasks. This was a great exercise in working with lists and file I/O.

5. **Python for Automation**:  
   Scripts written to automate simple tasks, such as file handling, web scraping, or system operations. These scripts demonstrate the power of Python to simplify repetitive tasks.

6. **Labb 1: Simplified Machine Learning Algorithm**:  
   The purpose of this lab was to use the tools I learned in Python to implement a simplified machine learning algorithm.
   
   - In this lab, I worked with simulated data of Pichus and Pikachus, including their lengths and widths. The goal was to create an algorithm that, based on the given data, could classify new data points as either Pichu or Pikachu.
   - **Restrictions**: No data processing libraries like Pandas or any machine learning libraries were allowed. The focus was on practicing Python, NumPy, and Matplotlib.
   
   **Tasks Completed**:
   - Built a basic algorithm following a flowchart to classify data points.
   - Implemented user input functionality, allowing users to input a test point and receive a classification. Added error handling to manage negative values and non-numeric inputs, ensuring user-friendly error messages.
   - Enhanced the classification approach by selecting the five nearest points to a test point and classifying it based on the majority class of these points (k-nearest neighbors approach).
   
   **Bonus Tasks**:
   - Divided the original data randomly into training and test sets (90% training data and 10% test data).
   - Calculated accuracy using a provided formula, treating Pikachu as the positive class and Pichu as the negative class.

7. **Labb 2: School Statistics Analysis**:  
   This lab aimed to explore school statistics using data from Sweden's national exams for 9th grade. The focus was on visualizing and analyzing trends in student performance.
   
   **Data**:  
   The data was collected from Skolverket, including information on national exams across different subjects.
   
   **Tasks Completed**:
   - Exported all graphs to a subfolder named `visualiseringar`. Matplotlib/Seaborn graphs were saved as PNG files, and Plotly graphs as HTML files. Ensured proper naming conventions for easier reference.
   - Paid attention to data storytelling by ensuring the graphs had suitable titles, labels, and annotations, while removing clutter and working with colors to focus attention.
   
   **Subtasks**:
   - **Uppgift 0 - Nation Overview**:
     - Loaded the `riket2023_åk9_np.xlsx` file and renamed columns for better readability.
     - Found the number of students who received an F in mathematics, separated by gender.
     - Created bar charts of total scores for different subjects using Matplotlib/Seaborn.
     - Created four subplots for total scores across subjects for different school authorities.
   - **Uppgift 1 - Grades and Exams Overview**:
     - Used Plotly to create line charts showing trends from the dataset `betyg_o_prov_riksnivå.xlsx`.
     - Visualized trends such as students lacking passing grades in one or more subjects from 2018-2023.
     - Examined factors affecting grades, such as parents' education level, and plotted these using relevant graphs.
   - **Uppgift 2 - KPIs & Exploratory Data Analysis (EDA)**:
     - Defined 3-6 Key Performance Indicators (KPIs) and conducted exploratory analysis on datasets other than those used in earlier tasks.
     - Documented findings using Markdown and saved all visualizations.

## Goals

The main goals of this repository are:

- To showcase my progress in learning Python.
- To serve as a reference for myself and others who are also learning Python.
- To document my journey from a beginner to someone who can develop more complex projects and apply Python in practical scenarios.

## Technologies Used

- **Python 3.10**: The main programming language.
- **Pandas, Matplotlib, Seaborn, Plotly**: For data analysis and visualization.
- **BeautifulSoup, Requests**: Used in automation and web scraping projects.

## Installation
To run any of the projects, make sure you have Python installed. Clone the repository and use a virtual environment to manage dependencies:

```sh
# Clone the repo
git clone https://github.com/username/python-learning-projects.git
cd python-learning-projects

# Set up a virtual environment
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Usage
Each folder contains a separate project or set of exercises. Navigate to the relevant folder and follow the instructions in the `README.md` file within each folder if available.

## Future Plans
- Expand on the automation scripts.
- Start a project involving machine learning, such as a simple prediction model.
- Explore additional Python libraries such as Flask for web development.

## Contributions
Feel free to fork this repository, submit pull requests, or open issues with suggestions. I'm always open to learning from others and improving my code.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thanks for checking out my Python learning projects! If you have any suggestions or just want to connect, feel free to reach out.

