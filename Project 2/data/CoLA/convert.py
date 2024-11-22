import csv

# File paths
tsv_file = '/Users/arunasrivastava/Desktop/547_HW2/CoLA-Task-Training/Project 2/data/CoLA/train.tsv'
csv_file = '/Users/arunasrivastava/Desktop/547_HW2/CoLA-Task-Training/Project 2/data/CoLA/train.csv'

# Convert TSV to CSV
with open(tsv_file, 'r') as tsv, open(csv_file, 'w', newline='') as csvf:
    reader = csv.reader(tsv, delimiter='\t')
    writer = csv.writer(csvf, delimiter=',')
    
    for row in reader:
        writer.writerow(row)

print(f"Converted {tsv_file} to {csv_file}.")
