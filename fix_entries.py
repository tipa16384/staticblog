import csv

# Read the CSV and fix specific entries
rows = []
with open('categories_simple_normalized.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 5:
            # Apply specific fixes to the normalized_name column (index 5)
            if row[5] == 'Progressquest':
                row[5] = 'ProgressQuest'
            elif row[5] == 'Pokemon Tcg Pocket':
                row[5] = 'Pokemon TCG Pocket'
            elif row[5] == 'Sages':
                row[5] = 'Sage'
            elif row[5] == 'Scott Pilgri':
                row[5] = 'Scott Pilgrim'
            elif row[5] == 'Roman Numeral Number Iii':
                row[5] = 'Roman Numeral III'
        rows.append(row)

# Write back the corrected CSV
with open('categories_simple_normalized.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print('Applied direct corrections to problematic entries')