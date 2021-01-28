#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###It happens all the time: someone gives you data containing malformed strings,python,lists and missing data. How do you tidy up so you can get on with the analysis?
#take this monstrosity as the dataframe to use in the following puzzles:

#df = pd.DataFrame({'From_To': ['LoNDon_paris', 'Madrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'],
#'FlightNumber': [10045, np.nan, 10065, np.nan, 10085], 
#'RecentDelays': [[23,47], [], [24,43,87], [13], [67,32]],
#'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})
    


# In[1]:


###1.Some values in the FlightNumber column are missing. These numbers are meant to increase by 10 with each row so 10055 and 10075 need to be put in place.Fill in these missing numbers and make the column an integer column
#(instead of a float column).

import numpy as np
import pandas as pd


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'Madrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085], 
'RecentDelays': [[23,47], [], [24,43,87], [13], [67,32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})
    
    
df


# In[3]:


df['FlightNumber']


# In[6]:


#setting up new index for the dataframe. this index is used for the for loop iteration created in next step
newindex=np.arange(1,df.From_To.count()+1)
newindex
df.set_index(newindex, inplace=True)
df


# In[8]:


#using for loop for interation along with isnullfunction to update the values for column FlightNumber
for i in np.arange(1,df.From_To.count()+1):
    if pd.isnull(df.FlightNumber.loc[i,]):
        df.loc[i,'FlightNumber'] = df.FlightNumber.loc[i-1] + 10
df['FlightNumber']
df


# In[9]:


#changing the data type for FlightNumber column to integer
df['FlightNumber'].astype(int)


# In[10]:


df['FlightNumber']


# In[15]:


###2.The From_To column would be better as two separate columns! split each string on the underscore delimiter_to give a new temporary dataframe with the correct values
#Assign the correct column names to this temporary dataframe.

df['From_To']


# In[5]:


#creating a new temporary dataframe which is a copy of existing dataframe df
temporarydf = df.copy()

#splitting the column into based on "_"
temporarydf[['From','To']] = temporarydf.From_To.str.split("_",expand=True)

#printing new dataframe
temporarydf


# In[12]:


###3. Notice how the capitalisation of the city names is all mixed up in this temporary dataframe. Standardise the strings so that only the first letter is uppercase(e.g."LondON" should become "london".)

#converting the first letter of values in 'From' column into uppercase
temporarydf.From = temporarydf.From.str.capitalize()

#converting the first letter of values in 'To' column into uppercase
temporarydf.To = temporarydf.To.str.capitalize()

#converting the first letter of values in 'From_To' column into uppercase
temporarydf.From_To = temporarydf.From_To.str.capitalize()

print(temporarydf)


# In[13]:


##4. Delete the From_To column from df and attach the temporary dataframe from the previous questions.


#printing the exisiting df
df


# In[14]:


##printing the dataframe after deleting the "From_To" column
df.drop('From_To',axis=1,inplace=True)
df


# In[15]:


##Adding the 'From_To' column from temporary database
df['From_To']= temporarydf['From_To']
df


# In[2]:


###5. In the recentdelays column, the values have been entered into the dataframe as a list.we would like each first value in its own column, each second value in its own column, and so on. if there isn't an Nth value, the value should be NaN

#Using the original dataframe provided for this problem.
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'Madrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23,47], [], [24,43,87], [13], [67,32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})

df
rows = []
_ = df.apply(lambda row:[rows.append([row['Airline'], row['FlightNumber'],nn,row['From_To']])
                        for nn in row.RecentDelays], axis=1)

    


# In[3]:


##printing all values in recent delay column in separate rows
rows


# In[4]:


##converting the data into data frame
df_new = pd.DataFrame(rows, columns=df.columns)

##printing existing dataframe (for comparsion view)
df


# In[5]:


##printing the revised dataframe as per the criteria defined in the problem
df_new


# In[6]:


##expand the series of lists into a dataframe named delays,rename the columns delay_1,delay_2,etc. and replace the unwanted recentdelays column in df with delays

##getting the recent delay values from the dataframe
df3 = pd.DataFrame(df['RecentDelays'].values.tolist())
df3


# In[7]:


length_cols = df3.shape[1]
length_cols


# In[8]:


df3.columns[0]


# In[9]:


##creating a for loop iteration for renaming the columns

col_list = []
col_dict ={}
for i in range(length_cols):
    key =df3.columns[i]
    
    value ="Delay" + str(i+1)
    col_dict[key] = value
    
col_dict


# In[10]:


##renaming the columns

df3.rename(columns=col_dict, inplace=True)
df3


# In[11]:


###printing the existing dataframe for comparsion
df


# In[12]:


df[["Delay1","Delay2","Delay3"]]= df3[["Delay1","Delay2","Delay3"]]


# In[13]:


###adding the new columns to the dataframe
df


# In[14]:


###printing the revised dataframe by dropping the recent delays column mentioned in the problem
df.drop('RecentDelays',axis=1,inplace=True)
df


# In[ ]:




