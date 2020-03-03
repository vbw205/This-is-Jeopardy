#Explore a Jeopardy data set and filter the data.

import pandas as pd
pd.set_option('display.max_colwidth', -1)

#2: Load the data into a DataFrame and investigate its contents.
jeopardy_data = pd.read_csv('jeopardy.csv')
#print(jeopardy_data.columns)

#2: Rename the columns.
jeopardy_data = jeopardy_data.rename(columns = {' Air Date':'Air Date',' Round':'Round',' Category':'Category',' Value':'Value',' Question':'Question',' Answer':'Answer'})
#print(jeopardy_data.columns)

#3: Write a function that filters the dataset for questions that contains all of the words in a list of words.
def filter_data(data, words):
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  return data.loc[data["Question"].apply(filter)]

#4: Test your original function with a few different sets of words to try to find some ways your function breaks. Edit your function so it is more robust.
filtered = filter_data(jeopardy_data, ['King', 'England'])
#print(filtered['Question'])
filtered = filter_data(jeopardy_data, ['novel', 'by'])
#print(filtered['Question'])
filtered = filter_data(jeopardy_data, ['beauty', 'is'])
#print(filtered['Question'])

#5: Convert the " Value" column to floats. 
jeopardy_data['Float Value'] = jeopardy_data['Value'].apply(lambda x: float(x[1:].replace(',','')) if x != 'None' else 0)

#5: what is the average value of questions that contain the word "King"?
filtered = filter_data(jeopardy_data, ['King'])
#print(filtered['Float Value'].mean())

#6: Write a function that returns the count of the unique answers to all of the questions in a dataset.
def get_answer_counts(data):
    return data['Answer'].value_counts()

#6: Testing the count function with filtered on line 29 'King'.
#print(get_answer_counts(filtered))

#7: How many questions from the 90s use the word "Computer" compared to questions from the 2000s?
def get_question_count(data):
    return data['Question'].count()
filtered = filter_data(jeopardy_data, ['Computer'])
#print(filtered['Question'])
filtered_90s = filtered[(filtered['Air Date'] >= '1990-01-01') & (filtered['Air Date'] <= '1999-12-31')]
#print(filtered_90s)
filtered_00s = filtered[(filtered['Air Date'] >= '2000-01-01') & (filtered['Air Date'] <= '2009-12-31')]
#print(get_question_count(filtered_90s))
#print(get_question_count(filtered_00s))
#Answer: There are 2 "Computer" questions from the 90s and 10 from the 2000's.

#7: Is there a connection between the round and the category? Are you more likely to find certain categories, like "Literature" in Single Jeopardy or Double Jeopardy?
def filter_data(data, words):
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  return data.loc[data["Category"].apply(filter)]
filtered = filter_data(jeopardy_data, ['Literature'])
#print(filtered['Category'])
filtered_single = filtered[(filtered['Round'] == 'Jeopardy!')]
filtered_double = filtered[(filtered['Round'] == 'Double Jeopardy!')]
filtered_final = filtered[(filtered['Round'] == 'Final Jeopardy!')]
def get_round_count(data):
    return data['Round'].count()
#print(get_round_count(filtered_single))
#print(get_round_count(filtered_double))
#print(get_round_count(filtered_final))
#For "Literature" categories, there are 0 single jeopardy rounds, 35 double jeopardy rounds, and 2 final jeopardy rounds. 
