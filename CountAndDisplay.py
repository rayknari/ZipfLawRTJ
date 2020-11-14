import csv

# opening text file encoding="utf8"
f = open('bible.txt', "r", )
d = dict()

for res in f:
    # removing new line and extra space characters
    res = res.strip()

    # changing case to prevent matching errors - makes all lower case
    res = res.lower()

    # separating key-value pairs
    lines = res.split()

# Doing the counting
    for line in lines:
        if line in d:
            # If the key-value pair is present in d then increment its value by one
            d[line] = d[line] + 1
        else:
            # Insert the key-value pair in the dictionary and sets its value to one
            d[line] = 1

f.close()


# Printing Result
for key in list(d.keys()):
    print("{} : {}".format(key, d[key]))

#Export to text file
with open('output.csv', 'w') as output:
    writer = csv.writer(output)
    for key, value in d.items():
        writer.writerow([key, value])

#export to excel - Not working
#with xlsxwriter.Workbook('test.xlsx') as workbook:
 #   worksheet = workbook.add_worksheet()

    #for row_num, data in enumerate(key):
     #   worksheet.write_row(row_num, 0, data)