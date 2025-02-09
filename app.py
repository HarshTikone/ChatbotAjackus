import streamlit as st
import sqlite3
import re
import pandas as pd

def create_connection():
    return sqlite3.connect("company.db")

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
        return pd.DataFrame(result, columns=["Employees"]) if result else "No employees found in this department."
    
    if "manager of" in user_query and department:
        result = execute_query("SELECT Manager FROM Departments WHERE Name = ?", (department,))
        return f"Manager: {result[0][0]}" if result else "No manager found for this department."
    
    if "hired after" in user_query and date:
        result = execute_query("SELECT Name FROM Employees WHERE Hire_Date > ?", (date,))
        return pd.DataFrame(result, columns=["Employees"]) if result else "No employees found hired after this date."
    
    if "total salary expense for" in user_query and department:
        result = execute_query("SELECT SUM(Salary) FROM Employees WHERE Department = ?", (department,))
        return f"Total Salary Expense: {result[0][0]}" if result[0][0] else "No salary data found."
    
    return "I couldn't understand the query. Try asking differently."

# Streamlit UI
st.set_page_config(page_title="SQLite Chat Assistant", page_icon="💬", layout="centered")
st.title("💬 SQLite Chat Assistant")
st.write("Ask questions about employees and departments!")

user_input = st.text_input("Enter your query:")

if st.button("Submit"):
    if user_input:
        response = process_query(user_input)
        st.subheader("Response:")
        if isinstance(response, pd.DataFrame):
            st.dataframe(response)
        else:
            st.write(response)
    else:
        st.warning("Please enter a query.")
