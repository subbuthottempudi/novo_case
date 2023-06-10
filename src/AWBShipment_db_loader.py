from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType,StringType,StructType,DoubleType,TimestampType
from pyspark.sql.functions import col
import logging
import traceback
import sys
import os
import json
import re


def AWBMasterbillDetailsCBS_schema():
    AWBMasterbillDetailsCBS_schema = StructType() \
      .add("Shipping_No",IntegerType(),True) \
      .add("From",IntegerType(),True) \
      .add("To",StringType(),True) \
      .add("Estimated_Departure",StringType(),True) \
      .add("Estimated_Arrival",StringType(),True) \
      .add("Index",StringType(),True)
    
    return AWBMasterbillDetailsCBS_schema

def AWBShipmentDetailsCBS_schema():
    AAWBShipmentDetailsCBS_schema = StructType() \
      .add("Shipping_No",IntegerType(),True) \
      .add("TrackingNumber",StringType(),True) \
      .add("Forwarder",StringType(),True) \
      .add("Currency",StringType(),True) \
      .add("Total_Volume_cbm",DoubleType(),True) \
      .add("Origin_Code",StringType(),True) \
      .add("Origin",StringType(),True) \
      .add("Origin_Country_Region",StringType(),True) \
      .add("Proof_Of_Delivery_Date",TimestampType(),True) \
      .add("Service_Product",StringType(),True) \
      .add("Delivery_Terms",StringType(),True) \
      .add("Total_Pieces",IntegerType(),True) \
      .add("Total_Actual_Weight",StringType(),True) \
      .add("Destination_Code",StringType(),True) \
      .add("Destination",StringType(),True) \
      .add("Destination_Country_Region",StringType(),True) \
      .add("Proof_Of_Delivery_Name",StringType(),True) \
      .add("Current_Shipment_Status",StringType(),True) \
      .add("Date",TimestampType(),True)
    
    return AAWBShipmentDetailsCBS_schema

def AWBShipmentProgressCBS_schema():
    AWBShipmentProgressCBS_schema = StructType() \
      .add("Shipping_No",IntegerType(),True) \
      .add("TrackingNumber",StringType(),True) \
      .add("Status",StringType(),True) \
      .add("Flight_Number",StringType(),True) \
      .add("Location",StringType(),True) \
      .add("Date",TimestampType(),True)  \
      .add("Time",StringType(),True) \
      .add("Index",IntegerType(),True)

    return AWBShipmentProgressCBS_schema

def ShipmentEquipmentCBS_schema():
    ShipmentEquipmentCBS_schema = StructType() \
      .add("Shipping_No",IntegerType(),True) \
      .add("Type_of_Transportation",StringType(),True) \
      .add("Origin",StringType(),True) \
      .add("Country_Of_Destination",StringType(),True) \
      .add("Equipment",StringType(),True) \
      .add("Sum_full_pallets",IntegerType(),True)  \
      .add("Sum_shipperboxes",IntegerType(),True) \
      .add("Forwarder",StringType(),True) \
      .add("Airline_Name",StringType(),True)
      
    return ShipmentEquipmentCBS_schema

def TracerReadingsCBS_schema():
    TracerReadingsCBS_schema = StructType() \
      .add("Shipping_No",IntegerType(),True) \
      .add("TT_Id",IntegerType(),True) \
      .add("Type_of_Transportation",StringType(),True) \
      .add("Origin",StringType(),True) \
      .add("Country_Of_Destination",StringType(),True) \
      .add("Mission_Started",TimestampType(),True)  \
      .add("Mission_Ended",TimestampType(),True) \
      .add("Date_Time_Of_Temp",StringType(),True) \
      .add("Temp_Point",IntegerType(),True) \
      .add("Temp",DoubleType(),True) \
      .add("Rounded_Temp",DoubleType(),True)  \
      .add("Product",StringType(),True)

    return TracerReadingsCBS_schema


if __name__ == "__main__":

    # This is a pyspark docker container(jupyter), Spark context is already available if not please add it here
    #Logging configuration
    logging.basicConfig(filename='logs/debug.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %H:%M:%S')
    logging.disable(logging.DEBUG)

    #sparksession  
    try:
                    
        spark = SparkSession \
            .builder \
            .appName("Novo Data processing") \
            .config("spark.jars", "postgresql-42.2.12.jar") \
            .config("spark.some.config.option", "NovoData") \
            .getOrCreate()        
        
        logging.info('SparkSession created')
                    
    except:
        
        logging.error(str(traceback.format_exc()))
        sys.exit()


    #Postgressql Connection details  
    url = "jdbc:postgresql://your_postgresql_server:5432/your_database"
    properties = {
        "user": "your_username",
        "password": "your_password",
        "driver": "org.postgresql.Driver"
    }
    
    # This will read csv files from input folder to a DataFrame
    logging.info('Pyspark Dataframe - AWBMasterbillDetailsCBS_DF')
    AWBMasterbillDetailsCBS_DF = spark.read.format("csv") \
        .option("header",True, delimiter=',') \
        .schema(AWBMasterbillDetailsCBS_schema()) \
        .load('/input/AWBMasterbillDetailsCBS.csv')
    
    logging.info('Pyspark Dataframe - AWBShipmentDetailsCBS_DF')
    AWBShipmentDetailsCBS_DF = spark.read.format("csv") \
        .option("header",True, delimiter=',') \
        .schema(AWBShipmentDetailsCBS_schema()) \
        .load('/input/AWBShipmentDetailsCBS.csv')
    
    logging.info('Pyspark Dataframe - AWBShipmentProgressCBS_DF')
    AWBShipmentProgressCBS_DF = spark.read.format("csv") \
        .option("header",True, delimiter=',') \
        .schema(AWBShipmentProgressCBS_schema()) \
        .load('/input/AWBShipmentProgressCBS.csv')
    
    logging.info('Pyspark Dataframe - ShipmentEquipmentCBS_DF')
    ShipmentEquipmentCBS_DF = spark.read.format("csv") \
        .option("header",True, delimiter=',') \
        .schema(ShipmentEquipmentCBS_schema()) \
        .load('/input/ShipmentEquipmentCBS.csv')
    
    logging.info('Pyspark Dataframe - TracerReadingsCBS_DF')
    TracerReadingsCBS_DF = spark.read.format("csv") \
        .option("header",True, delimiter=',') \
        .schema(TracerReadingsCBS_schema()) \
        .load('/input/TracerReadingsCBS.csv')
    
    AWBMasterbillDetailsCBS_DF.printSchema()
    AWBShipmentDetailsCBS_DF.printSchema()
    AWBShipmentProgressCBS_DF.printSchema()
    ShipmentEquipmentCBS_DF.printSchema()
    TracerReadingsCBS_DF.printSchema()

     # Adding the code to save the tables to hive
    """   AWBMasterbillDetailsCBS_DF.rdd.repartition(50) \
                            .write \
                            .mode('append') \
                            .saveAsTable('AWBMasterbillDetailsCBS')

        AWBShipmentDetailsCBS_DF.rdd.repartition(50) \
                            .write \
                            .mode('append') \
                            .saveAsTable('AWBShipmentDetailsCBS')

        AWBShipmentProgressCBS_DF.rdd.repartition(50) \
                            .write \
                            .mode('append') \
                            .saveAsTable('AWBShipmentProgressCBS')

        ShipmentEquipmentCBS_DF.rdd.repartition(50) \
                            .write \
                            .mode('append') \
                            .saveAsTable('ShipmentEquipmentCBS')

        TracerReadingsCBS_DF.rdd.repartition(50) \
                            .write \
                            .mode('append') \
                            .saveAsTable('TracerReadingsCBS') """
    

    try:

        AWBMasterbillDetailsCBS_DF.write.jdbc(url, table_name= "AWBMasterbillDetailsCBS" , mode="append", properties=properties)
        AWBShipmentDetailsCBS_DF.write.jdbc(url, table_name= "AWBShipmentDetailsCBS", mode="append", properties=properties)
        AWBShipmentProgressCBS_DF.write.jdbc(url, table_name= "AWBShipmentProgressCBS", mode="append", properties=properties)
        ShipmentEquipmentCBS_DF.write.jdbc(url, table_name= "ShipmentEquipmentCBS", mode="append", properties=properties)
        TracerReadingsCBS_DF.write.jdbc(url, table_name= "TracerReadingsCBS", mode="append", properties=properties)

        logging.info('Data loaded to postgres tables')
                    
    except:
        
        logging.error(str(traceback.format_exc()))
        sys.exit()


    # Reading Table data from postgressql
    table_name = "AWBMasterbillDetailsCBS"
    test_df = spark.read.jdbc(url, table_name, properties=properties)
    