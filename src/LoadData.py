# import necessary packages
import pandas
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine


# establish connection with the database
engine = create_engine('mysql+mysqlconnector://root:!2E4@127.0.0.1/bikes')

# read the pandas dataframe
# 202105-divvy-tripdata : 531633
# 202106-divvy-tripdata : 729595
# 202107-divvy-tripdata : 822410
# 202108-divvy-tripdata : 804352
# 202109-divvy-tripdata : 756147
# 202110-divvy-tripdata : 631226
# 202111-divvy-tripdata : 359978
# 202112-divvy-tripdata : 247540
# 202201-divvy-tripdata : 103770
# 202202-divvy-tripdata : 115609
# 202203-divvy-tripdata : 284042
# 202204-divvy-tripdata : 371249
data = pandas.read_csv('C:/Users/jayap/OneDrive/Desktop/BikesCSV/202204-divvy-tripdata.csv')

# connect the pandas dataframe with postgresql table
data.to_sql('bike_trips', engine,index=True, if_exists='append',chunksize=100000)

print('Data loaded successfully')
exit(0)