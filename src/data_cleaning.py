import pandas as pd
import pymysql
from sqlalchemy import create_engine

df = pd.read_csv('./Dataset/raw/Luxury_Housing_Bangalore.csv')
print(df)

print("***********************************************************************")
print(df.isnull().sum())

print("************************************************************************")
print(df.describe())

cleaned_df = df.copy()
print(list(cleaned_df.columns))

#******************************Start Cleaning**********************************

#Property_ID
print("********checking column : Property_ID*********")
print("Total Unique values in Property_ID :",cleaned_df["Property_ID"].count())
print("Null value in Property_ID :",cleaned_df["Property_ID"].isna().sum())


#Micro_Market
print("********checking column : Micro_Market*********")
print("Total Unique values in Micro_Market :",cleaned_df["Micro_Market"].count())
print("Unique values in Micro_Market: ",cleaned_df["Micro_Market"].unique())
print("Null value in Micro_Market :",cleaned_df["Micro_Market"].isna().sum())

# Normalize the Micro_Market names
cleaned_df["Micro_Market"] = (
    cleaned_df["Micro_Market"]
    .str.strip()             # remove leading/trailing spaces
    .str.title()             # convert to Title Case (Eg. 'Mg Road')
)
print(cleaned_df["Micro_Market"].unique())

#Project_Name
print("********checking column : Project_Name*********")
print("Total Unique values in Project_Name :",cleaned_df["Project_Name"].count())
print("Null value in Project_Name :",cleaned_df["Project_Name"].isna().sum())

#Developer_Name
print("********checking column : Developer_Name*********")
print("Total Unique values in Developer_Name :",cleaned_df["Developer_Name"].count())
print("Null value in Developer_Name :",cleaned_df["Developer_Name"].isna().sum())
print("Unique values in Developer_Name: ",cleaned_df["Developer_Name"].unique())


#Configuration
print("********checking column : Configuration	*********")
print("Total Unique values in Configuration :",cleaned_df["Configuration"].count())
print("Null value in Configuration :",cleaned_df["Configuration"].isna().sum())
print("Unique values in Configuration : ",cleaned_df["Configuration"].unique())
# Make uppercase and strip spaces
cleaned_df['Configuration'] = cleaned_df['Configuration'].str.upper().str.strip()
# Standardize the "+" cases
cleaned_df['Configuration'] = cleaned_df['Configuration'].str.replace("BHK+", "BHK+", regex=False)
cleaned_df['Configuration'] = cleaned_df['Configuration'].str.replace("BHK", "BHK", regex=False)
cleaned_df['Configuration'].unique()

#Unit_Size_Sqft
print("********checking column : Unit_Size_Sqft	*********")
print("Total Unique values in Unit_Size_Sqft :",cleaned_df["Unit_Size_Sqft"].count())
print("Null value in Unit_Size_Sqft before:",cleaned_df["Unit_Size_Sqft"].isna().sum())
print("Unique values in Unit_Size_Sqft : ",cleaned_df["Unit_Size_Sqft"].unique())

# Replace -1 with NaN
cleaned_df['Unit_Size_Sqft'] = cleaned_df['Unit_Size_Sqft'].replace(-1, pd.NA)

# Fill NaN using group mean (Micro_Market + Developer_Name + Configuration)
cleaned_df['Unit_Size_Sqft'] = cleaned_df.groupby(
    ['Micro_Market', 'Developer_Name', 'Configuration']
)['Unit_Size_Sqft'].transform(lambda x: x.fillna(x.mean()))
print("Remaining nulls:", cleaned_df['Unit_Size_Sqft'].isna().sum())

#Ticket_Price_Cr
print("******** checking column : Ticket_Price_Cr	*********")
print("Total Unique values in Ticket_Price_Cr :",cleaned_df["Ticket_Price_Cr"].count())
print("Null value in Ticket_Price_Cr :",cleaned_df["Ticket_Price_Cr"].isna().sum())
cleaned_df['Ticket_Price_Cr'] = pd.to_numeric(cleaned_df['Ticket_Price_Cr'], errors='coerce')

# Price_medians (Micro_Market + Configuration)
price_medians = cleaned_df.groupby(['Micro_Market', 'Configuration'])['Ticket_Price_Cr'].median()
cleaned_df['Ticket_Price_Cr'] = cleaned_df.apply(
    lambda row: price_medians.get((row['Micro_Market'], row['Configuration']))
    if pd.isna(row['Ticket_Price_Cr']) else row['Ticket_Price_Cr'],
    axis=1
)
print("Null value in Ticket_Price_Cr after :",cleaned_df["Ticket_Price_Cr"].isna().sum())

#Amenity_Score
print("******** checking column : Amenity_Score	*********")
print("Total Unique values in Amenity_Score :",cleaned_df["Amenity_Score"].count())
print("Null value in Amenity_Score :",cleaned_df["Amenity_Score"].isna().sum())

# Amenity_Score Imputation (Micro_Market + Developer_Name) 
if 'Developer_Name' in cleaned_df.columns:
    amenity_medians = cleaned_df.groupby(['Micro_Market', 'Developer_Name'])['Amenity_Score'].median()
    cleaned_df['Amenity_Score'] = cleaned_df.apply(
        lambda row: amenity_medians.get((row['Micro_Market'], row['Developer_Name']))
        if pd.isna(row['Amenity_Score']) else row['Amenity_Score'],
        axis=1
    )

print("Null value in Amenity_Score after :",cleaned_df["Amenity_Score"].isna().sum())

#Transaction_Type
print("******** checking column : Transaction_Type	*********")
print("Total Unique values in Transaction_Type :",cleaned_df["Transaction_Type"].count())
print("Null value in Transaction_Type :",cleaned_df["Transaction_Type"].isna().sum())
print("Unique values in Transaction_Type : ",cleaned_df["Transaction_Type"].unique())

#Buyer_Type
print("******** checking column : Buyer_Type	*********")
print("Total Unique values in Buyer_Type :",cleaned_df["Buyer_Type"].count())
print("Null value in Buyer_Type :",cleaned_df["Buyer_Type"].isna().sum())
print("Unique values in Buyer_Type : ",cleaned_df["Buyer_Type"].unique())

#Purchase_Quarter
print("******** checking column : Purchase_Quarter	*********")
print("Total Unique values in Purchase_Quarter :",cleaned_df["Purchase_Quarter"].count())
print("Null value in Purchase_Quarter :",cleaned_df["Purchase_Quarter"].isna().sum())
print("Unique values in Purchase_Quarter : ",cleaned_df["Purchase_Quarter"].unique())
cleaned_df["Purchase_Quarter"].info()
cleaned_df['Purchase_Quarter'] = pd.to_datetime(cleaned_df['Purchase_Quarter'], errors='coerce')
cleaned_df["Purchase_Quarter"].info()

#Connectivity_Score
print("******** checking column : Connectivity_Score	*********")
print("Total Unique values in Connectivity_Score :",cleaned_df["Connectivity_Score"].count())
print("Null value in Connectivity_Score :",cleaned_df["Connectivity_Score"].isna().sum())
print("Unique values in Connectivity_Score : ",cleaned_df["Connectivity_Score"].unique())

#Possession_Status
print("******** checking column : Possession_Status	*********")
print("Total Unique values in Possession_Status :",cleaned_df["Possession_Status"].count())
print("Null value in Possession_Status :",cleaned_df["Possession_Status"].isna().sum())
print("Unique values in Possession_Status : ",cleaned_df["Possession_Status"].unique())

#Sales_Channel
print("******** checking column : Sales_Channel	*********")
print("Total Unique values in Sales_Channel :",cleaned_df["Sales_Channel"].count())
print("Null value in Sales_Channel :",cleaned_df["Sales_Channel"].isna().sum())
print("Unique values in Sales_Channel : ",cleaned_df["Sales_Channel"].unique())

#NRI_Buyer
print("******** checking column : NRI_Buyer	*********")
print("Total Unique values in NRI_Buyer :",cleaned_df["NRI_Buyer"].count())
print("Null value in NRI_Buyer :",cleaned_df["NRI_Buyer"].isna().sum())
print("Unique values in NRI_Buyer : ",cleaned_df["NRI_Buyer"].unique())

#Locality_Infra_Score
print("******** checking column : Locality_Infra_Score*********")
print("Total Unique values in Locality_Infra_Score :",cleaned_df["Locality_Infra_Score"].count())
print("Null value in Locality_Infra_Score :",cleaned_df["Locality_Infra_Score"].isna().sum())
print("Unique values in Locality_Infra_Score : ",cleaned_df["Locality_Infra_Score"].unique())

#Avg_Traffic_Time_Min
print("******** checking column : Avg_Traffic_Time_Min*********")
print("Total Unique values in Avg_Traffic_Time_Min :",cleaned_df["Avg_Traffic_Time_Min"].count())
print("Null value in Avg_Traffic_Time_Min :",cleaned_df["Avg_Traffic_Time_Min"].isna().sum())
print("Unique values in Avg_Traffic_Time_Min : ",cleaned_df["Avg_Traffic_Time_Min"].unique())

#Buyer_Comments
print("******** checking column : Buyer_Comments	*********")
print("Total Unique values in Buyer_Comments :",cleaned_df["Buyer_Comments"].count())
print("Null value in Buyer_Comments :",cleaned_df["Buyer_Comments"].isna().sum())
print("Unique values in Buyer_Comments : ",cleaned_df["Buyer_Comments"].unique())

# Buyer_Comments Imputation 
cleaned_df['Buyer_Comments'] = cleaned_df['Buyer_Comments'].fillna("No comment")
print("Unique values in Buyer_Comments after : ",cleaned_df["Buyer_Comments"].unique())


# Missing Value Check 
missing_before = df.isna().sum()
missing_after = cleaned_df.isna().sum()
missing_summary = pd.DataFrame({
    "Missing Before": missing_before,
    "Missing After": missing_after
}).loc[["Ticket_Price_Cr", "Unit_Size_Sqft", "Amenity_Score", "Buyer_Comments"]]


#************************************Derived columns*************************************
#Price_per_Sqft
cleaned_df['Price_per_Sqft'] = ((cleaned_df['Ticket_Price_Cr'] * 1e7) / cleaned_df['Unit_Size_Sqft']).round(1)
print(cleaned_df['Price_per_Sqft'])

#Purchase_Quarter
cleaned_df["Purchase_Quarter"].head()
cleaned_df['Purchase_Quarter'] = pd.to_datetime(cleaned_df['Purchase_Quarter'])
cleaned_df['Quarter_Number'] = cleaned_df['Purchase_Quarter'].dt.quarter
print(cleaned_df["Purchase_Quarter"])
print(cleaned_df['Quarter_Number'])

#Booking_Flag
cleaned_df['Booking_Flag'] = cleaned_df['Transaction_Type'].apply(
    lambda x: 1 if str(x).strip().lower() == "primary" else 0
)
print(cleaned_df[['Transaction_Type', 'Booking_Flag']].head(10))
print(cleaned_df['Booking_Flag'].value_counts())
print(cleaned_df)

print(cleaned_df.info())

#Save into csv
Cleaned_data = "./Dataset/cleaned/Luxury_Housing_Bangalore_Cleaned_data.csv"
cleaned_df.to_csv(Cleaned_data, index=False)
print(f"Cleaned CSV saved at: {Cleaned_data}")


#load into sql
#Credential
username = "root"
password = "12345"
host = "localhost"
port = 3306
database = "luxurydb"

#connect with mysql
connection = pymysql.connect(
    host=host,
    user=username,
    password=password,
)
cursor = connection.cursor()
print("MySQL Database connection successful")

# Create database 
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
print(f"Database '{database}' is ready.")
cursor.execute(f"USE {database}")

#create table 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS luxury_housing_bangalore (
        Property_ID VARCHAR(50) PRIMARY KEY,
        Micro_Market VARCHAR(255),
        Project_Name VARCHAR(255),
        Developer_Name VARCHAR(255),
        Unit_Size_Sqft FLOAT,
        Configuration VARCHAR(50),
        Ticket_Price_Cr FLOAT,
        Transaction_Type VARCHAR(50),
        Buyer_Type VARCHAR(50),
        Purchase_Quarter DATE,
        Connectivity_Score FLOAT,
        Amenity_Score FLOAT,
        Possession_Status VARCHAR(50),
        Sales_Channel VARCHAR(50),
        NRI_Buyer VARCHAR(50),
        Locality_Infra_Score FLOAT,
        Avg_Traffic_Time_Min FLOAT,
        Buyer_Comments TEXT,
        Price_per_Sqft FLOAT,
        Quarter_Number INT,
        Booking_Flag BOOLEAN
    )
""")
print("Table 'luxury_housing_bangalore' is ready.")

#insert data
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")
cleaned_df.to_sql('luxury_housing_bangalore', con=engine, if_exists='replace', index=False)

print("DataFrame inserted into MySQL table 'luxury_housing_bangalore' successfully")
