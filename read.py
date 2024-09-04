import csv

# Function to read mobile numbers from a CSV file
def read_mobile_numbers_from_csv(file_path):
    mobile_numbers = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            mobile_numbers.append(row[0])  # Assumes one number per line
    return mobile_numbers



print(read_mobile_numbers_from_csv("Book1.csv"))