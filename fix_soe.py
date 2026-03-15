import csv

rows = []
with open('categories_simple_normalized.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 5 and row[1] == '1271' and row[2] == 'soe':
            row[5] = 'Sony Online Entertainment'
        rows.append(row)

with open('categories_simple_normalized.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
    
print('Fixed SOE entry to Sony Online Entertainment')