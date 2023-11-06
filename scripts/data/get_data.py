#!/usr/bin/python3

from catboost.datasets import adult
train_df, test_df = adult()
train_df.to_csv("/home/ml-srv-admin/lab1/data/raw/train.csv", columns=train.columns)
test_df.to_csv("/home/ml-srv-admin/lab1/data/raw/test.csv", columns=test.columns)