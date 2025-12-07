# Custom CSV Parser

A lightweight Python CSV parser that **reads and writes CSV files** with proper handling of commas, quotes, and newlines.  
It ensures that fields containing special characters are correctly escaped and quoted.

---

## Features

- Handles commas, double quotes, and newlines in CSV fields.
- Automatically escapes double quotes by doubling them.
- Supports reading from and writing to CSV files.
- Lightweight and dependency-free (pure Python).

---

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/KrishnaTulasiSatti/Custom-CSV-Parser-in-Python.git
cd Custom-CSV-Parser-in-Python
```

## Project Structure

custom-csv-parser-in-python/
 ├── custom_csv/
 │    ├── __init__.py
 │    ├── reader.py
 │    └── writer.py
 ├── tests/
 │    ├── output_data.csv
 │    ├── sample_data.csv
 ├── .gitignore
 ├── benchmark.py
 ├── builtin_output.csv
 ├── custom_output.csv
 ├── main.py
 ├── synthetic_data.csv
 └── README.md

---

### **How to Run / Example Script**  

```markdown
## How to Run

```bash
python main.py

python benchmark.py
```

## Usage Examples

### Reading CSV

The **CustomCsvReader** allows you to read CSV files while correctly handling:

- Commas inside fields  
- Double quotes inside fields  
- Newlines inside fields  

**Example CSV (`sample_data.csv`):**

Name,Age,City,Note
Tulasi,25,"Hyderabad","Loves reading and ""traveling"""
"Nikhil",30,Bangalore,"Enjoys playing ""freefire"" and doing coding"
Pavani,28,"Chennai",Passionate about ""painting""
Durga,32,Mumbai,"Fitness ""enthusiast"""
Surekha,27,Delhi,Foodie and ""traveler""
"Deepthi",29,Kolkata,Music lover
Geetha,31,"Pune","Gardening is her ""hobby"""


**Output after reading:**

['Name', 'Age', 'City', 'Note']
['Tulasi', '25', 'Hyderabad', 'Loves reading and "traveling"']
['Nikhil', '30', 'Bangalore', 'Enjoys playing "freefire" and doing coding']
['Pavani', '28', 'Chennai', 'Passionate about "painting"']
['Durga', '32', 'Mumbai', 'Fitness "enthusiast"']
['Surekha', '27', 'Delhi', 'Foodie and "traveler"']
['Deepthi', '29', 'Kolkata', 'Music lover']
['Geetha', '31', 'Pune', 'Gardening is her "hobby"']


---

### Writing CSV

The **CustomCsvWriter** allows you to write Python lists to CSV while ensuring:

- Fields containing commas are quoted  
- Double quotes inside a field are **doubled** automatically  

**Example Output CSV (`output_data.csv`):**

Name,Age,City,Note
Tulasi,25,Hyderabad,"Loves reading and ""traveling"""
Nikhil,30,Bangalore,"Enjoys playing ""freefire"" and coding"
Pavani,28,Chennai,"Passionate about """"painting"""""
Durga,32,Mumbai,"Fitness ""enthusiast"""
Surekha,27,Delhi,"Foodie and """"traveler"""""
Deepthi,29,Kolkata,Music lover
Geetha,31,Pune,"Gardening is her ""hobby"""


---

## Benchmark Analysis

The `benchmark.py` script measures the performance of the **Custom CSV Parser** against Python's built-in `csv` module using a synthetic data with **10,000 rows × 5 columns**.

**Benchmark Results:**

| Operation        | Custom CSV Parser | Python `csv` Module |
|-----------------|-----------------|------------------|
| Reading CSV      | 0.3366 seconds   | 0.0110 seconds   |
| Writing CSV      | 0.0414 seconds   | 0.0231 seconds   |

**Analysis:**

- The **built-in `csv` module** is faster due to optimized C implementation.  
- The **Custom CSV Parser** prioritizes **correct handling of complex CSV fields** (commas, quotes, newlines) while remaining lightweight and pure Python.  
- For typical CSV files, the performance difference is negligible.  
- For very large files, built-in CSV is faster, but the custom parser ensures **data integrity** for tricky CSVs.  

---




  






