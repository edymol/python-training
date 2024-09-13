import pandas as pd
import json
import re

input_file_path = '/path/to/input/file/Results.tsv'
output_file_path = '/path/to/output/file/flattened_data_step1.tsv'

df = pd.read_csv(input_file_path, sep='\t', dtype=object)

def clean_json_like_string(x):
    if isinstance(x, str):
        x = x.replace("None", "null").replace("True", "true").replace("False", "false")
        x = re.sub(r'(?<!\\)"', r'\"', x)
    return x

def fix_nested_json(text):
    if isinstance(text, str):
        text = re.sub(r'(?<!\\)"', r'\\"', text)
        return text
    return text

def parse_response_text(response_text):
    try:
        if isinstance(response_text, str):
            response_text = fix_nested_json(response_text)
            return json.loads(response_text)
        return response_text
    except (json.JSONDecodeError, TypeError) as e:
        print(f"Error parsing 'response_text': {response_text}, error: {str(e)}")
        return None

def flatten_wifi_column(df, column_name):
    def safe_load_entry(x):
        x = clean_json_like_string(x)
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

    flattened = pd.json_normalize(flattened)
    flattened.columns = [f'{column_name}_{col}' for col in flattened.columns]
    df_flattened = pd.concat([df.drop(columns=[column_name]), flattened], axis=1)

    print(f"Details for '{column_name}' have been flattened:")
    print(flattened.head(25))

    return df_flattened

for column in ['website', 'wifi']:
    df = flatten_wifi_column(df, column)

df = flatten_wifi_column(df, 'wifi_data')
df.to_csv(output_file_path, sep='\t', index=False)

print(f'Flattened data saved to {output_file_path}')
