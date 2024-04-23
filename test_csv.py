import pandas as pd

def validate_csv(csv_file):
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file)

        # Check file size
        file_size = df.memory_usage(deep=True).sum()  # Total memory usage
        print(f"File Size: {file_size} bytes")

        # Check column headers
        print("Column Headers:")
        print(df.columns)

        # Check data types
        print("Data Types:")
        print(df.dtypes)

        # Check for missing values
        print("Missing Values:")
        print(df.isnull().sum())

        # Check for inconsistent row lengths
        row_lengths = df.apply(lambda row: len(row), axis=1)  # Calculate row lengths
        if len(set(row_lengths)) == 1:
            print("Consistent row lengths")
        else:
            print("Inconsistent row lengths")

        print("Validation completed successfully.")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
csv_file = 'generated_articles.csv'  # Replace with the path to your CSV file
validate_csv(csv_file)
