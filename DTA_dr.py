#Loading necesary libraries
import pandas as pd 
import numpy as np 
import os 
from matplotlib import pyplot as plt 

#Loading the datasets, and setting the datapathways
DESCRIP_PATH = "/Users/laurakhaukha/Desktop/Diss_data/SnomedCT_UKClinicalRF2_PRODUCTION_20241120T000001Z/Snapshot/Terminology/sct2_Description_UKCLSnapshot-en_GB1000000_20241120.txt"
RELASHION_PATH = "/Users/laurakhaukha/Desktop/Diss_data/SnomedCT_UKClinicalRF2_PRODUCTION_20241120T000001Z/Snapshot/Terminology/sct2_Relationship_UKCLSnapshot_GB1000000_20241120.txt"

descrip_df = pd.read_csv(DESCRIP_PATH, header=0, delimiter="\t", dtype=str)
relashion_df_ = pd.read_csv(RELASHION_PATH, delimiter="\t", dtype=str) 


# Create a smaller file copy to prevent memmory loss, for later use: COMBACK for randomisation
relation_chunk = pd.read_csv(RELASHION_PATH, delimiter="\t", dtype=str, nrows=1000) # The first 1000 rows only 
descripnchunk = pd.read_csv(DESCRIP_PATH, delimiter="\t", dtype=str, nrows=1000) # The first 1000 rows only 

########### Exploratory Data Analysis ############
print(descrip_df.columns)  
print(relashion_df_.columns)  

# Viewing the shape of the data
descrip_df.head(20)
relashion_df_.head(20)
relashion_df_.shape
descrip_df.shape

# Looking into counts per row/column
descrip_df["id"].value_counts()
descrip_df["id"].nunique()
relashion_df_["id"].value_counts()
relashion_df_["id"].nunique()

# Checking for missing values 
print(descrip_df.isnull().sum())   #No missing values
print(relashion_df_.isnull().sum())  # No missing values 

#Descriptive statistics, can not be done one th merged 
relashion_df_.describe()
relashion_df_.summary()
descrip_df.describe()
descrip_df.summary()

####### Demopgraphic analysis: Which conditions are most common in the dataset
plt.ion() # to display the plot in vs code 
# knowledge map
# Creating a bar chart for the term frequencies within the dataset
print(descrip_df.columns)
print(relashion_df_.columns)
v = descrip_df["term"].value_counts()

plt.figure(figsize=(20, 10))
plt.bar(v.index, v.values)
plt.xlabel("Term")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.title("Frequency of Terms/Diagnosis in Description Data")
plt.savefig("term_frequency2.png")
plt.show() 

# Making a table instead: for term frequencies 
term_frequencies = descrip_df["term"].value_counts().reset_index()
term_frequencies.columns = ["Term", "Count"]
print(term_frequencies.head(20))   #Displaying the most - frequent terms/ medical categories

#Making a figure for the moduleId'
m = descrip_df["term"].value_counts()
plt.figure(figsize=(12, 6))
plt.bar(m.index, m.values)

plt.xlabel("ModuleId")
plt.ylabel("Count")
plt.title("Frequency of ModuleId in Description Data")
plt.show()

# Merging datasets
# The chatbox aims to provide knowlege to the reaseachers
# Provide all the codes on this topic 
# sausage roll -(is a)-> pastry -(is_a)-> food
# Is sausage roll a food?
#is a + is a = is a

#merged_dr_df = pd.merge(descrip_df, relashion_df_, on="id", how="left") # is this reasonable ?


# use jupyter notbook file wihitn vs code for image display