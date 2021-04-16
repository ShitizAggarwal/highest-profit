import csv
import json

PROFIT_KEY = "Profit (in millions)"

def read_data():
    data = []
    try:
        with open('data.csv', mode='r') as data_file:
            data_reader = csv.DictReader(data_file)
            for row in data_reader:
                data.append(row)
            # since first line is header return from first row
            return data
    except Exception as ex:
        print(f"Exception while reading data.csv: {ex}") 

def clean_data(data):
    cleansed_data = []
    for row in data:
        if row[PROFIT_KEY].isnumeric():
            cleansed_data.append(row)

    return cleansed_data

def dump_json(data):
    try:
        with open('data2.json', mode='w') as json_file:
            json.dump(data, json_file)
    except Exception as ex:
        print(f"Exception while reading data.csv: {ex}")

def get_top_20_profit(data):
    sorted_data = sorted(data, key=lambda row: row[PROFIT_KEY], reverse=True)
    return sorted_data[:20]

def main():
    data = read_data()
    print(f"Number of rows: {len(data)}")

    cleansed_data = clean_data(data)
    print(f"Number of rows left after cleaning: {len(cleansed_data)}")

    top_20_profit = get_top_20_profit(cleansed_data)
    print("Top 20 profits:")
    for row in top_20_profit:
        print(row)

    dump_json(cleansed_data)

if __name__ == "__main__":
    main()