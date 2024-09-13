import csv
import os
import glob

for file in glob.glob("output*.csv"):
    os.remove(file)

header = ['telefone', 'image']


def quebra_csv(linhas, arquivo):
    with open(arquivo, mode='r', newline='') as arquivo_csv:
        reader = csv.reader(arquivo_csv)

        batch_size = linhas
        batch = []
        file_count = 1

        for index, row in enumerate(reader, start=1):
            batch.append(row)

            if index % batch_size == 0:
                with open(f'output_{file_count}.csv', mode='w', newline='') as output_file:
                    writer = csv.writer(output_file)
                    writer.writerow(header)
                    writer.writerows(batch)
                batch = []
                file_count += 1

        if batch:
            with open(f'output_{file_count}.csv', mode='w', newline='') as output_file:
                writer = csv.writer(output_file)
                writer.writerow(header)
                writer.writerows(batch)


if __name__ == '__main__':
    quebra_csv(450, 'Results.csv')
