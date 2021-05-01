import json
import csv
with open('/content/notes.csv') as f:
    a_dictionary = dict(filter(None, csv.reader(f)))

## print(a_dictionary)

values = a_dictionary.values()
values_list = list(values)

note1 = values_list[1]
note2 = values_list[2]
note3 = values_list[3]
note4 = values_list[4]
note5 = values_list[5]

print(note1, note2, note3, note4, note5)

json_notes = {'note1': note1, 'note2': note2, 'note3': note3, 'note4': note4, 'note5': note5}
json_object["designer_notes"] = json_notes

a_file = open("ARCH01.json", "w")
json.dump(json_object, a_file, indent=4)
a_file.close()
