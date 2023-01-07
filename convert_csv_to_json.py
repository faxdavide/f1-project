import json
import pandas as pd
import os

def single_file_convert(path, name_file):
    df = pd.read_csv(path)

    for index, row in df.iterrows():
        final_file = name_file + '.json'
        with open(final_file, 'a') as f:
            f.write(json.dumps(row.to_dict()))
            f.write("\n")

def multi_file_convert(num_file):
    for x in range(1,num_file):
        base_path = 'C:/Users/fassi/Desktop/f1-project/f1db_csv/split_2/pit_stops-'
        extension_file = '.csv'
        final_path = base_path + str(x) + extension_file
        print(final_path)
        df = pd.read_csv(final_path)

        for index, row in df.iterrows():
            open_file = 'pit_stops'
            json_extension = '.json'
            new_file = open_file + str(x) + json_extension
            with open(new_file, 'a') as f:
                f.write(json.dumps(row.to_dict()))
                f.write("\n")