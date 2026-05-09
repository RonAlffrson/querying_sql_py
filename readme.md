# Project Report: Chinook Digital Music Store Data Analysis

In this project, I connected **Python** to the **Chinook database**, a sample SQLite database representing a small digital music store. I wrote SQL queries directly from a **Jupyter Notebook** to explore the data and derive answers to key business questions.

Since SQLite requires no server or complex configuration, this approach provided an efficient workflow for integrating SQL with Python's data science ecosystem.

## Project Execution

- **Database Connection:** Successfully connected to the Chinook database file using Python's `sqlite3` library.
- **Schema Exploration:** Explored the database schema to identify all tables (such as Tracks, Invoices, Customers, and Employees) and mapped their relationships.
- **Data Querying:** Wrote and executed complex SQL queries to solve specific business problems:
    - Identified the **10 best-selling tracks** by volume.
    - Analyzed global sales to determine **which country generates the most revenue**.
    - Evaluated staff performance to find the **top-performing sales employee**.
- **Data Integration:** Loaded the results of the SQL queries into **Pandas DataFrames** for easier manipulation.
- **Visualization:** Created visual representations of the findings, including **bar charts** using Matplotlib to highlight sales trends and performance.

## Technologies Used

- **Python**
- **sqlite3**
- **Pandas**
- **Matplotlib**
- **Jupyter Notebook**

## Key Learnings

Throughout this project, I practiced writing `SELECT`, `JOIN`, `GROUP BY`, and `ORDER BY` statements. I also gained hands-on experience in moving data from a relational SQL environment into Pandas for visualization. This project demonstrated when SQL is more convenient than Pandas for querying structured data and how to combine both for a complete data analysis pipeline.
