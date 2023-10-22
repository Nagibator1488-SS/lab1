import sys
import os
import io


def convert_txt(f_in, f_out):
    educations = []
    sexs = []
    hourses = []
    salarys = []
    ages = []

    for line in f_in:
        line = line.rstrip('\n').split(',')
        ages.append(line[0])
        educations.append(line[1])
        sexs.append(line[2])
        hourses.append(line[3])
        salarys.append(line[4])

    for i in range(len(sexs)):
        if sexs[i] == 'Male':
            sexs[i] = 0
        else:
            sexs[i] = 1

    for i in range(len(salarys)):
        if salarys[i] == '>50K':
            arr_salary[i] = 0
        else:
            arr_salary[i] = 1

    for age, education, sex, hourse, salary in zip(ages, educations, sexs, hourses, salarys):
        f_out.write("{},{},{},{}\n".format(survived, pclass, sex, age))

f_in_name = sys.argv[1]
f_out_name = os.path.join("data", "convert", "train.csv")
os.makedirs(os.path.join("data", "convert"), exist_ok=True)

with io.open(f_in_name, encoding="utf8") as f_in:
    with io.open(f_out_name, "w", encoding="utf8") as f_out:
        convert_txt(f_in, f_out)