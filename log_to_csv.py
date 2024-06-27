import pandas as pd
import re

def parse_log_to_csv(log_file_path, output_csv_path):
    # Create an empty list to store the data
    data = []

    # Read the log file line by line
    with open(log_file_path, 'r') as file:
        for line in file:
            # Extract timestamp, ID, and data bytes using regex
            match = re.search(r'\((.*?)\).*can1 (\w+)#(\w+)', line)
            if match:
                timestamp = float(match.group(1))
                id_hex = "0x" + match.group(2).upper()
                data_bytes = ' '.join(re.findall('..', match.group(3).upper()))

                # Add a new row to the list
                data.append({'Timestamp': timestamp, 'ID': id_hex, 'DataBytes': data_bytes})

    # Convert the list to a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a .csv file
    df.to_csv(output_csv_path, index=False)

    print(f"Log data has been successfully saved to {output_csv_path}")

if __name__ == "__main__":
    log_file_path = "path/to/your/log_file.txt"  # Change this to the path of your log file
    output_csv_path = "path/to/your/output_file.csv"  # Change this to the path where you want to save the CSV file
    parse_log_to_csv(log_file_path, output_csv_path)
