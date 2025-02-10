from flask import Flask, render_template, request
import sqlite3
import re
import pandas as pd

app = Flask(__name__)

def create_connection():
    return sqlite3.connect("company.db", check_same_thread=False)

def execute_query(query, params=()):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
    return result

def get_departments():
    result = execute_query("SELECT Name FROM Departments")
    return [row[0].lower() for row in result]

def extract_department(user_query):
    departments = get_departments()
    for dept in departments:
        if dept in user_query.lower():
            return dept.capitalize()
    return None

def extract_date(user_query):
    match = re.search(r"\d{4}-\d{2}-\d{2}", user_query)
    return match.group(0) if match else None

def process_query(user_query):
    department = extract_department(user_query)
    date = extract_date(user_query)
    
    if "employees in" in user_query and department:
        result = execute_query("SELECT Name FROM Employees WHERE Department = ?", (department,))
        return [row[0] for row in result] if result else ["No employees found in this department."]
    
    if "manager of" in user_query and department:
        result = execute_query("SELECT Manager FROM Departments WHERE Name = ?", (department,))
        return [f"Manager: {result[0][0]}"] if result else ["No manager found for this department."]
    
    if "hired after" in user_query and date:
        result = execute_query("SELECT Name FROM Employees WHERE Hire_Date > ?", (date,))
        return [row[0] for row in result] if result else ["No employees found hired after this date."]
    
    if "total salary expense for" in user_query and department:
        result = execute_query("SELECT SUM(Salary) FROM Employees WHERE Department = ?", (department,))
        return [f"Total Salary Expense: {result[0][0]}"] if result[0][0] else ["No salary data found."]
    
    return ["I couldn't understand the query. Try asking differently."]

@app.route('/', methods=['GET', 'POST'])
def index():
    response = []
    if request.method == 'POST':
        user_input = request.form.get('query')
        if user_input:
            response = process_query(user_input)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
