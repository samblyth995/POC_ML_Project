# 7 broad categories of linked in industries
# Financial Services.
# Information Technology and Services.
# Hospital & Health Care.
# Construction.
# Retail.
# Education
# Accounting

import pandas as pd
file_path='labeled_training_data.csv'
df = pd.read_csv(file_path)

def lowercase_text_columns(df):
    for col in df.columns:
        if df[col].dtype == 'object':  # Checks if the column is of text type
            df[col] = df[col].str.lower()
    return df

# Apply the function to your DataFrame
df = lowercase_text_columns(df) 
print(df.dtypes)
#list of tech industry key words
industry_keywords = {
    'information technology': ['software tester','aws','azure','cloud','AI','artifical intelligence','machine learning','data','data engineer','data analyst','backend','frontend','front-end','coding','coder','digital','website','web','software', 'tech', 'developer', 'software engineer', 'network engineer' 'IT','dev-ops','cyber'],
    'financial services': ['mortgage','finance', 'financial', 'bank', 'investment','accountant'],
    'construction': ['surveyor','construction', 'building site', 'roofing','electrician','electrical','labourer','site manager','bricklayer','plasterer','tradesman'],
    'education': ['head teacher','teacher', 'school', 'education', 'educator'],
    'medical healthcare and vetinary':['optician','locum','physiotherapist','outpatient','clinic','hygenist','dental','dentist','nurse','therapist','clinical'',doctor','medical','healthcare','patient care','social care','surgeon','surgery','physician', 'pahrmaceutical','surgical'],
    'retail':['salesforce','sales','cusotmer service','retail','cashier','checkout','stocking','stock','fashion','sales floor','sales floor','delivery driver'],
    'engineering':['offshore','off-shore','solar','net zero','renewable','energy','mechanic','oil','gas','MOT','motor'],
    'hospitality':['chef','kitchen','hotel','bed and breakfast','cleaning','cleaner','domestic'],
    'legal':['law','lawyer','solicitor','magistrate','judge']
}

# Labeling function
def label_industry(job_title):
    job_title = str(job_title).lower()
    for industry, keywords in industry_keywords.items():
        if any(keyword.lower() in job_title.lower() for keyword in keywords):
            return industry
    return 'Other'  # Default label if no keywords match

# Apply the labeling function to the column
df['industry_label'] = df['job_title'].apply(label_industry)

print(df[['job_title','industry_label']].sample(100,random_state=42))