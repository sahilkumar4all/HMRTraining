import csv
def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            data.append(row)
    return data
data = read_csv('dia.csv')
print(data)
