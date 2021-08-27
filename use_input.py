import os
import umfragen_skript as umsk

# Ermöglicht es die input datei mit beliebigem namen in den Ordner /input zu legen und diese Datei auszuführen
def main():
    input_path = os.path.join(os.path.dirname(__file__), 'input')
    for file in os.listdir(input_path):
        if not file.endswith('xlsx'):
            output_prefix = get_output_prefix(file)
            f = open('input/' + file)
            umsk.main(f, output_prefix)

# Liest den Titel der Umfrage aus
# Format erwartet: 4._Umfrage_xxxx_xxxxx_xxxxx
def get_output_prefix(file_name):
    prefix = file_name.split('_')
    prefix = prefix[0] + prefix[1]
    return prefix

if __name__ == '__main__':
    main()