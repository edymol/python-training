import pandas as pd
import json
import re

# Define file paths
input_file_path = '/path/to/your/input_file.tsv'  # Dummy path
output_file_path = '/path/to/your/output_file.tsv'  # Dummy path

# Step 1: Read the TSV file into a DataFrame
df = pd.read_csv(input_file_path, sep='\t', dtype=object)

# Step 2: Function to safely parse JSON-like strings and fix nested quotes
def clean_json_like_string(x):
    """
    Replaces Python-like None, True, False with their JSON equivalents,
    and ensures that keys and values are enclosed in double quotes.
    """
    if isinstance(x, str):
        x = x.replace("None", "null").replace("True", "true").replace("False", "false")
        # Use regex to fix incorrectly escaped quotes within the string
        x = re.sub(r'(?<!\\)"', r'\"', x)
    return x

# Step 3: Function to fix inner JSON issues in 'response_text'
def fix_nested_json(text):
    """
    Fixes quotes inside the 'response_text' field to ensure valid JSON parsing.
    """
    if isinstance(text, str):
        # Fix the incorrect quotes around the nested JSON structure
        text = re.sub(r'(?<!\\)"', r'\\"', text)
        return text
    return text

# Step 4: Function to parse 'response_text' and handle the nested JSON
def parse_response_text(response_text):
    """
    Parse the 'response_text' field, which is a JSON string inside a JSON object.
    """
    try:
        if isinstance(response_text, str):
            # First, clean up the response_text by fixing any issues
            response_text = fix_nested_json(response_text)
            # Now, parse the JSON string
            return json.loads(response_text)
        return response_text
    except (json.JSONDecodeError, TypeError) as e:
        print(f"Error parsing 'response_text': {response_text}, error: {str(e)}")
        return None

# Step 5: Function to flatten the wifi_data or other specific column
def flatten_column(df, column_name):
    """
    Flatten the given column, including parsing the nested 'response_text' field if applicable.
    """
    def safe_load_entry(x):
        x = clean_json_like_string(x)  # Convert Python-like values to JSON-compatible values
        try:
            if isinstance(x, str):
                return json.loads(x)
            elif isinstance(x, dict):
                return x
            elif pd.isna(x):
                return {}
            else:
                return {}
        except (json.JSONDecodeError, TypeError) as e:
            print(f"Error loading entry for column '{column_name}', value: {x}, error: {str(e)}")
            return {}

    def flatten_entry(entry):
        if isinstance(entry, dict):
            if 'response_text' in entry and isinstance(entry['response_text'], str):
                entry['response_text'] = parse_response_text(entry['response_text'])
            return entry
        return {}

    json_columns = df[column_name].apply(safe_load_entry)
    flattened = json_columns.apply(flatten_entry)

    # Normalize the data (flatten nested dicts)
    flattened = pd.json_normalize(flattened)

    # Rename flattened columns to avoid conflicts
    flattened.columns = [f'{column_name}_{col}' for col in flattened.columns]

    # Combine flattened columns with the original DataFrame
    df_flattened = pd.concat([df.drop(columns=[column_name]), flattened], axis=1)

    # Show details of the flattened data
    print(f"Details for '{column_name}' have been flattened:")
    print(flattened.head(25))  # Show the first few rows of the flattened data

    return df_flattened

# Step 6: Flatten specific columns
# Flatten 'website' and 'wifi_data' columns
for column in ['website', 'wifi_data']:
    print(f"Flattening column: {column}")
    df = flatten_column(df, column)

# Flatten 'phone_data' column with handling for nested 'response_text'
print("Flattening column: phone_data")
df = flatten_column(df, 'phone_data')

# Step 7: Save the final DataFrame with flattened columns
df.to_csv(output_file_path, sep='\t', index=False)

print(f'Flattened data saved to {output_file_path}')
