import csv

from settings import output_folder, csv_path
from split_video import split_video, clear_folder


clear_folder(output_folder)
with open(csv_path, 'r') as fp:
    rows = csv.reader(fp)
    for row in rows:
        word = row[0]
        paraphrase = row[1]
        try:
            split_video(word, paraphrase)
        except Exception:
            pass