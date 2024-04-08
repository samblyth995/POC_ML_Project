import pandas as pd
from sklearn.model_selection import train_test_split
file_path ='job_postings_full_UK_prepped.csv'
df=pd.read_csv(file_path)

#80% split to be labelled, 20& unlabelled
df_to_be_labeled, df_unlabeled = train_test_split(df, test_size=0.2, random_state=42)

#split the labeled and unlabled in to futher test and train

# Split the "to-be-labeled" into labeled training (60% of total) and labeled testing (20% of total)
df_labeled_train, df_labeled_test = train_test_split(df_to_be_labeled, test_size=0.25, random_state=42) # 0.25 * 0.8 = 0.2
df_labeled_train.to_csv("labeled_training_data.csv", index=False)
df_labeled_test.to_csv("labeled_testing_data.csv", index=False)
#test (unlableled train) and evaluation (unlabelled test)
df_unlabeled_train, df_unlabeled_test = train_test_split(df_unlabeled, test_size=0.5, random_state=42)
df_unlabeled_train.to_csv("unlabeled_training_data.csv", index=False)
df_unlabeled_test.to_csv("unlabeled_testing_data.csv", index=False)