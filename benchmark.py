"""
Benchmark Script for Custom CSV Reader and Writer

This script compares:
1. CustomCSVReader   vs   csv.reader
2. CustomCSVWriter   vs   csv.writer

Dataset:
- 10,000 rows
- 5 columns
"""

import csv
import random
import timeit
import string
from custom_csv import CustomCSVReader
from custom_csv import CustomCSVWriter

def generate_random_field():
    """Generate random text with possible commas, quotes, and newlines."""
    content = ''.join(random.choices(string.ascii_letters + " ,\"\n", k=random.randint(5, 20)))
    return content.replace("\n", " ")

def generate_csv_file(filename, rows=10000, cols=5):
    """Create a synthetic CSV file with random content."""
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for _ in range(rows):
            row = [generate_random_field() for _ in range(cols)]
            writer.writerow(row)

def benchmark_reader(file_path):
    
    # Benchmark CustomCSVReader
    def custom_read():
        for _ in CustomCSVReader(file_path):
            pass
    
    # Benchmark csv.reader
    def builtin_read():
        with open(file_path, "r", encoding="utf-8") as f:
            for _ in csv.reader(f):
                pass

    custom_time = timeit.timeit(custom_read, number=1)
    builtin_time = timeit.timeit(builtin_read, number=1)

    return custom_time, builtin_time

def benchmark_writer(data, custom_file, builtin_file):
   
    # Benchmark CustomCSVWriter
    def custom_write():
        writer = CustomCSVWriter(custom_file)
        writer.write_rows(data)

    # Benchmark csv.writer
    def builtin_write():
        with open(builtin_file, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerows(data)

    custom_time = timeit.timeit(custom_write, number=1)
    builtin_time = timeit.timeit(builtin_write, number=1)

    return custom_time, builtin_time


if __name__ == "__main__":
    test_csv = "synthetic_data.csv"
    custom_output = "custom_output.csv"
    builtin_output = "builtin_output.csv"

    print("\nGenerating synthetic CSV (10,000 rows × 5 columns)...")
    generate_csv_file(test_csv)

    # Load data into memory ONCE for writer test
    print("Loading file for writer benchmark...")
    with open(test_csv, "r", encoding="utf-8") as f:
        data = list(csv.reader(f))

    # Run reader benchmark
    custom_reader_time, builtin_reader_time = benchmark_reader(test_csv)

    # Run writer benchmark
    custom_writer_time, builtin_writer_time = benchmark_writer(
        data, custom_output, builtin_output
    )

    print("\n================== BENCHMARK RESULTS ==================\n")

    print(f"Custom Reader Time   : {custom_reader_time:.4f} seconds")
    print(f"csv.reader Time      : {builtin_reader_time:.4f} seconds\n")

    print(f"Custom Writer Time   : {custom_writer_time:.4f} seconds")
    print(f"csv.writer Time      : {builtin_writer_time:.4f} seconds\n")