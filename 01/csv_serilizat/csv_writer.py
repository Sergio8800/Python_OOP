import csv
with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight"],
                              restkey="new", restval="MainOffice", delimiter=' ', quoting=csv.QUOTE_NONNUMERIC)
    tmp = {}
    for i, line in enumerate(csv_file):
        # print(f'{line = }')
        # print(i)
        # print(f'{line["name"] = }\t{line["age"] = }')

        tmp[i] = line
        # print(line['name'], line['age'])
    print(tmp)

with open("../subjects.csv", 'r', newline='', encoding='utf-8') as f:
    csv_file = csv.DictReader(f, fieldnames=["Математика", "Физика", "История", "Литература"], restkey="new",
                              restval="No definition",
                              delimiter=' ', quoting=csv.QUOTE_NONNUMERIC)
    # for line in csv_file:
    #     self.subjects = line
    # print(type(line))
    tmp1 = {}
    for line in csv_file:
    # for i, line in enumerate(csv_file):
        # print(f'{line = }')

        # print(f'{line["name"] = }\t{line["age"] = }')
        # print(line['Математика'], line['Физика'])
        tmp1["Ivan"] = line
    print(tmp1)