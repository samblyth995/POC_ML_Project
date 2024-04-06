# POC_ML_Project
 Began with the task of trying to categorise the jobs ( specifically extract a list of Tech jobs)
I used the job skills first. I used K means to try this, but the skills are too broad and repeated and the 
clusters were not relevant.

step 2; Going to try the job title as it may be more descriptive. I need to standadrise the job titles first.
used a dictionary to replace strings and try and get some standardisation to the terms used.

step 3 - lemitization to reduce words to thier base form- after implementing it, it made very few changes

step 4- filter down search country to the United Kingdom and created a 1000 data set of just jobs in the UK.the 1.3Millton data set was too large for my machine

