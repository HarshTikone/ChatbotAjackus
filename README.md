# SQLite Chat Assistant

## 📌 Overview
The **SQLite Chat Assistant** is a Python-based chatbot that allows users to query an SQLite database using natural language. It converts user queries into SQL commands to fetch relevant information from the database.

## ⚙️ How It Works
1. The user enters a query in plain English.
2. The chatbot processes the query and extracts relevant information (e.g., department name, date).
3. Based on the query type, the chatbot generates an SQL query and fetches the data from the SQLite database.
4. The response is displayed in a structured format using **Streamlit**.

## 🔧 Features
- Retrieve employees from a specific department.
- Get the manager of a department.
- List all employees hired after a specific date.
- Calculate the total salary expense for a department.
- Interactive **Streamlit UI** for easy user interaction.

## 🚀 Steps to Run Locally
### Prerequisites
Ensure you have **Python 3.7+** installed and **SQLite3** configured.

### 1️⃣ Clone the Repository
```sh
 git clone https://github.com/HarshTikone/ChatbotAjackus.git
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
 python -m venv venv
 source venv/bin/activate  # Mac/Linux
 venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies
```sh
 pip install -r requirements.txt
```

### 4️⃣ Set Up the Database
Run the following command to create and populate the SQLite database:
```sh
 python database_setup.py
```

### 5️⃣ Run the Streamlit App
```sh
 streamlit run app.py
```

### 6️⃣ Interact with the Chatbot
Open the **localhost URL** provided in the terminal and start asking questions such as:
- "Who is the manager of Sales?"
- "Show me all employees in Engineering."
- "List all employees hired after 2022-01-01."
- "What is the total salary expense for Marketing?"

## 🔍 Known Limitations & Future Improvements
### ❌ Limitations
- **Limited Query Understanding:** The chatbot follows a structured pattern-matching approach, meaning it may not handle complex or grammatically incorrect queries.
- **Fixed Database Schema:** The chatbot works only with the predefined database schema.
- **No Machine Learning Integration:** The assistant does not use AI models for query understanding but relies on regex and rule-based parsing.

### 🔄 Future Improvements
- ✅ Add support for more flexible queries using **NLU techniques (spaCy, BERT, etc.)**.
- ✅ Implement a better UI with **autocomplete suggestions**.
- ✅ Extend support for dynamic database schemas.
- ✅ Allow **voice-based queries** for an improved experience.

---
Developed with ❤️ using **Python, SQLite, and Streamlit** 🚀

