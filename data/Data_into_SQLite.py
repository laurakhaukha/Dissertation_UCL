#Loading the TRUD Data into a SQLite database

#Loading and Imporrting relavent packages
import sqlite3
import pandas as pd

# Processing and Loading the description table
decrip_df = pd.read_csv("/Users/laurakhaukha/Desktop/Diss_data/SnomedCT_UKClinicalRF2_PRODUCTION_20241120T000001Z/Snapshot/Terminology/sct2_Description_UKCLSnapshot-en_GB1000000_20241120.txt", sep="\t", dtype=str)
decrip_df.columns = map(str.lower, decrip_df.columns)  # lowercase
decrip_df = decrip_df[decrip_df["active"] == "1"]  # keep only active descriptions

# Processing and loading the relationships table
rela_df = pd.read_csv("/Users/laurakhaukha/Desktop/Diss_data/SnomedCT_UKClinicalRF2_PRODUCTION_20241120T000001Z/Snapshot/Terminology/sct2_Relationship_UKCLSnapshot_GB1000000_20241120.txt", sep="\t", dtype=str)
rela_df.columns = map(str.lower, rela_df.columns)
rela_df = rela_df[rela_df["active"] == "1"]  #Removing duplicate/inactive relationships

# Creating the SQLite database
conn = sqlite3.connect("snomedct_data.db")

#Writing the description and relationship tables to the database
decrip_df.to_sql("TRUD_descriptiontable", conn, if_exists="replace", index=False)
rela_df.to_sql("TRUD_relationshiptable", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

# Verifying the database 
conn = sqlite3.connect("snomedct_data.db")
cur = conn.cursor() #Establisshing the Cursor object, used to execute SQL commands

#Listing the tables 
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())

#Looking at the contents
sqllite_df = pd.read_sql_query("SELECT * FROM TRUD_descriptiontable LIMIT 5", conn)
print(sqllite_df.head())
conn.close() #Closing the connection

