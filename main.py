from custom_csv import CustomCSVReader
from custom_csv import CustomCSVWriter

if __name__ == "__main__":
    file_path = "tests/sample_data.csv"
    reader = CustomCSVReader(file_path)

    data = []
    for row in reader:
        data.append(row)
        print(row)
    
    output_file = "tests/output_data.csv"
    writer = CustomCSVWriter(output_file)
    
    # Writing the rows read from the original CSV
    writer.write_rows(data)
    print(f"\nData written to {output_file} successfully.")    


