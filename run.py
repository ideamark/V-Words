import os
import csv

from settings import csv_path, output_folder
from split_video import split_video


with open(csv_path, 'r') as fp:
    rows = csv.reader(fp)
    for row in rows:
        word = row[0]
        if word not in os.listdir(output_folder):
            paraphrase = row[1]
            try:
                split_video(word, paraphrase)
            except Exception as e:
                print(e)