import csv
import os

path = "1"
output = f"{path}/ds.csv"

files = os.listdir(path)
txt_files = [file for file in files if file.endswith(".txt")]

ds = []

for txt_file in txt_files:
    txt_file_lines = []
    with open(f"{path}/{txt_file}", "r") as f:
        txt_file_lines = f.read().splitlines()

    pts = [j for i, j in enumerate(txt_file_lines) if i % 3 == 0]
    its = [j for i, j in enumerate(txt_file_lines) if i % 3 == 1]

    for i, pt in enumerate(pts):
        ds.append({
            "pt": pts[i].strip(),
            "it": its[i].strip(),
        })

with open(output, "w") as f:
    fieldnames = ["pt", "it"]
    writer = csv.DictWriter(f, fieldnames=fieldnames, quotechar="\"", doublequote=False, quoting=csv.QUOTE_ALL, escapechar="\\",)

    writer.writeheader()

    for e in ds:
        writer.writerow(e)
