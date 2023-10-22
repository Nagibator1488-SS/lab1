import sys
import os
import io


def get_features(f_in, f_out):
    f_in.readline()
    for line in f_in:
        line = line.rstrip('\n').split(',')
        age = line[0]
        education = line[4]
        sex = line[9]
        hours = line[12]
        salary = line[14]

        f_out.write("{},{},{},{}\n".format(age, education, sex, hours, salary))

f_in_name = sys.argv[1]
f_out_name = os.path.join("data", "features", "train.csv")
os.makedirs(os.path.join("data", "features"), exist_ok=True)

with io.open(f_in_name, encoding="utf8") as f_in:
    with io.open(f_out_name, "w", encoding="utf8") as f_out:
        get_features(f_in, f_out)