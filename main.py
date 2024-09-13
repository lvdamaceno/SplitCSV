import csv
import os
import glob


def remove_existing_files(pattern):
    """Remove arquivos existentes que correspondem ao padrão fornecido."""
    for file in glob.glob(pattern):
        try:
            os.remove(file)
            print(f"Removed file: {file}")
        except OSError as e:
            print(f"Error removing file {file}: {e}")


def quebra_csv(linhas, arquivo_entrada):
    """Divide um arquivo CSV em vários arquivos menores com base no número de linhas por arquivo."""
    header = ['telefone', 'image']

    with open(arquivo_entrada, mode='r', newline='') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        batch = []
        file_count = 1

        for index, row in enumerate(reader):
            if index == 0:
                continue  # Skip header

            batch.append(row)

            if len(batch) == linhas:
                output_file = f'output_{file_count}.csv'
                with open(output_file, mode='w', newline='') as output:
                    writer = csv.writer(output)
                    writer.writerow(header)
                    writer.writerows(batch)
                print(f"Created file: {output_file}")
                batch = []
                file_count += 1

        if batch:
            output_file = f'output_{file_count}.csv'
            with open(output_file, mode='w', newline='') as output:
                writer = csv.writer(output)
                writer.writerow(header)
                writer.writerows(batch)
            print(f"Created file: {output_file}")


if __name__ == '__main__':
    # Remove existing files matching the pattern
    remove_existing_files("output*.csv")

    # Split the CSV file into smaller files
    quebra_csv(300, 'Results.csv')
