import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import spacy
nlp = spacy.load("en_core_web_sm")
#have an inital look at the data
#file_path = 'POC_ML_Project\Data_exploration\original_data\job_skills.csv'
file_path = 'POC_ML_Project\Data_exploration\original_data\linkedin_job_postings.csv'
#file_path = 'POC_ML_Project\Data_exploration\original_data\job_summary.csv'


##large dataset causes memory problems, so from nw on I will work on the 1000 sample

#file_path = 'skills_1000_prepped.csv'
df = pd.read_csv(file_path)
#print(df.head(5))
# print(df.columns)
# print(df.dtypes)
# print (df.shape)
#print(df['job_title'].head(5))
                            ########data pre-porcessing
        #dtypes are 'object' need to change to strings
df['job_title'] = df['job_title'].astype(str)
#df['job_link'] = df['job_link'].astype(str)
#change all text to lower case
#df['job_title'] = df['job_title'].str.lower()
        ##all columns lower case####

def lowercase_text_columns(df):
    for col in df.columns:
        if df[col].dtype == 'object':  # Checks if the column is of text type
            df[col] = df[col].str.lower()
    return df

# Apply the function to your DataFrame
df = lowercase_text_columns(df)        
#remove special characters
df['job_title'] = df['job_title'].str.replace('[^a-zA-Z0-9 ]', '', regex=True)
df_uk=df[df['search_country']=='united kingdom']
#standardise terms
#df = pd.DataFrame(file_path)
print(df_uk['job_title'].head(5))

# Dictionary of terms to standardize
standardization_dict = {
    r'\brn\b': ' registered nurse ',
    r'\bmgr\b': ' manager ',
    r'\bsr\.\b': ' senior ',
    r'\bmech\.\b': ' mechanical ',
    r'\bsurg\b': ' surgeon '
}


# Replace the terms based on the dictionary
for key, value in standardization_dict.items():
    df_uk['job_title'] = df_uk['job_title'].str.replace(key, value, regex=True)


#print(df['job_title'].head(5))
#print(df.dtypes)
        # data is already lower case and each skill is comma delimetered
        # there is a space after each comma so that should be removed
#df['job_skills'] = df['job_skills'].apply(lambda x: ', '.join(skill.strip() for skill in x.split(',')))
        #in this data set there are no NaN or blank values



    # Vectorization
# vectorizer = CountVectorizer(tokenizer=lambda x: x.split(', '), binary=True)
# skill_matrix = vectorizer.fit_transform(df['job_skills'])

    #vecoriser creates a sparse matrix, to view it - I can write it to a df
# feature_names = vectorizer.get_feature_names_out()
# print(feature_names)
# df_vectorized = pd.DataFrame(skill_matrix.toarray(), columns=feature_names)
# print(df_vectorized.head())

#####use the smaller data set as memory is at capacity
#df=df.head(1000)

                ###Lemitizing## reducing to the base word
# def lemmatize_text(text):
#     doc = nlp(text)
#     lemmatized_list = [token.lemma_ for token in doc]
#     # Join the lemmatized words into a single string
#     lemmatized_text = ' '.join(lemmatized_list)
#     return lemmatized_text

# # Apply the lemmatization function to each job title
# df['lemmatized_job_title'] = df['job_title'].apply(lemmatize_text)

#print(df.head[['job_title', 'lemmatized_job_title']])

df_uk=df_uk.head(1000)
df_uk.to_csv("job_postings_1000_UK_prepped.csv")
# Correct syntax to write specific columns to a CSV file
#df[['job_title', 'lemmatized_job_title']].to_csv("job_postings_1000_prepped.csv", index=False)

#print(df2)
