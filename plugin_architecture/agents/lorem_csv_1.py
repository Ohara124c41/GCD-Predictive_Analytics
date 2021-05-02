import csv
import lorem

from lorem.text import TextLorem

with open('csv-random_notes_1.csv', mode='w') as csv_file:
    fieldnames = ['note_number', 'note_str']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    lorem = TextLorem(wsep='; ', srange=(2,3), words="good difficult excellent sufficient".split())

    s1 = lorem.sentence()  # 'C-B.'
    s2 = lorem.sentence()  # 'C-A-C.'

    print(s1)
    print(s2)

    writer.writeheader()
    writer.writerow({'note_number': 1, 'note_str': s1})
    writer.writerow({'note_number': 2, 'note_str': s2})