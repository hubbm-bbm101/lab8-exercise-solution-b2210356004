import sys
file = open(sys.argv[1], "r")
records = {}
for i in file:
    key, record = i.split(":")
    record.strip("\n")
    records[key] = record
file.close()
students = sys.argv[2].split(",")

try:
    for i in students:
        print("Name: {}, University: {},".format(i, records[i]))
except:
    print("No record of '{}' was found".format(i))
