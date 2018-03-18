import csv
from random import randrange

for line in open('../Data_Set/loader_work_orders_sanitised.csv', newline=''):
    print(line[4].split())


with open("../Data_Set/Training.txt", "w") as training_text_file:
    with open("../Data_Set/Testing.txt", "w") as testing_text_file:
        with open('../Data_Set/loader_work_orders_sanitised.csv', newline='') as csvfile:
                data_reader = csv.reader(csvfile)
                for row in data_reader:
                    short_text = row[4]
                    print(short_text.split())
                    dice = randrange(4)
                    if dice > 3:
                        print(row[4], file=testing_text_file)
                    else:
                        print(row[4], file=training_text_file)
