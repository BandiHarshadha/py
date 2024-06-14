import csv
csv_file_path = "path/to/your/csv/file.csv"
try:
    with open(csv_file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(", ".join(row)) 
except FileNotFoundError:
    print(f"File '{csv_file_path}' not found. Please check the file path.")
