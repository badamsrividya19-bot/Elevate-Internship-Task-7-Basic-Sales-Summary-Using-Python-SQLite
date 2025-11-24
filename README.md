Elevate Internship — Task 7
Basic Sales Summary Using Python & SQLite

This repository contains the submission for Elevate Internship — Task 7, which focuses on performing a basic sales summary using Python and SQLite. The objective is to create a small SQLite database, run SQL aggregation queries, and visualize the results using Python, pandas, and matplotlib.

1. Project Overview

The task demonstrates how SQL and Python can work together for quick data analysis.
Using a simple sales table, the following tasks were completed:

Creating a SQLite database (sales_data.db)

Running SQL queries inside Python to compute:

Total quantity sold per product

Total revenue per product

Loading SQL outputs into pandas for analysis

Generating a bar chart showing product-wise revenue

Preparing a PDF report summarizing the analysis

The repository includes all required scripts, database files, output images, and the final PDF report.

2. Dataset Structure

The dataset used is a small sales table with the following structure:

Column Name	Description
product	Name of the product sold
quantity	Number of units sold
price	Price per unit

Sample data is pre-inserted into sales_data.db for demonstration.

3. Repository Contents
File Name	Description
sales_task_report.pdf	Final PDF report summarizing Task 7
sales_data.db	SQLite database containing sample sales data
sales_chart.png	Bar chart showing revenue per product
task7.ipynb	Jupyter Notebook with step-by-step execution
task7.py	Python script version of the solution
README.md	Documentation for this project
4. SQL Query Used
4.1 Product-wise Quantity and Revenue (SQLite / Python)
SELECT 
  product,
  SUM(quantity) AS total_qty,
  SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;


This query aggregates the total units sold and total revenue generated for each product.

5. Sample Output Format
Product	Total Quantity	Revenue
Laptop	7	420000
Mobile	20	300000
Headphones	20	24000

(Values above correspond to the sample dataset included in the project.)

6. How to Run the Project
Using the Notebook
Open task7.ipynb in Jupyter Notebook → Run all cells

Using the Python Script
python task7.py


The script will:

Connect to sales_data.db

Execute the SQL aggregation query

Print the results

Generate the sales_chart.png file

7. Notes

SQLite requires no installation; it is built into Python.

pandas is used to load and display the SQL results.

matplotlib is used for the bar chart visualization.

The PDF report (sales_task_report.pdf) contains a clean summary for submission.

This task demonstrates the integration of SQL queries inside Python workflows.

8. Author

Badam Sri Vidya
Elevate Internship — Task 7 Submission
B.Tech CSE (Data Science)
