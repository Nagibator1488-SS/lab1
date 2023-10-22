import sys
import os
import io


def fill_na(f_in, f_out):
    ages = []
    educations = []
    sexs = []
    hourses = []
    salarys = []

    for line in f_in:
        line = line.rstrip('\n').split(',')
        educations.append(line[1])
        sexs.append(line[2])
        hourses.append(line[3])
        salarys.append(line[4])
        if line[0]:
            ages.append(float(line[0]))
        else:
            ages.append(0)

    for i in range(len(ages)):
        if ages[i] == 0:
            ages[i] = sum(ages) / len(ages)

    for age, education, sex, hours, salary in zip(ages, educations, sexs, hourses, salarys):
        f_out.write("{},{},{},{}\n".format(age, education, sex, hours, salary))

f_in_name = sys.argv[1]
f_out_name = os.path.join("data", "fillna", "train.csv")
os.makedirs(os.path.join("data", "fillna"), exist_ok=True)

with io.open(f_in_name, encoding="utf8") as f_in:
    with io.open(f_out_name, "w", encoding="utf8") as f_out:
        fill_na(f_in, f_out)