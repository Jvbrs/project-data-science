# Project Data Science

## Overview

This project focuses on data analysis in the field of data science. It includes modules for processing sales data, generating reports, and sending emails with the obtained insights.

## Project Structure
 ```bash
project-data-science/
├── src/
│ ├── init.py
│ ├── analysis_code.py
├── main/
│ ├── init.py
│ └── main.py
├── .gitignore
└── README.md
 ```

## Features

- **Data Analysis:** The `analysis_code` module contains scripts for processing sales data, calculating key metrics like revenue and average ticket, and generating meaningful insights.

- **Email Automation:** The `main` module uses the analyzed data to generate reports and automates the process of sending emails with the insights.


## Usage
1. Set up your virtual environment:
   
    python -m venv myvenv
    source myvenv/bin/activate  # For Unix/Linux
    .\myvenv\Scripts\activate   # For Windows

3. Install dependencies:

    ```bash
   - pip install -r requirements.txt

4. Run the main script:
   
   - python main.py

## Requirements
    - Python 3.x
    - Pandas
    - smtplib (for email functionality) 
