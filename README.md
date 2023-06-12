# novo_case

For this solution I am considering to Dockerise the Pyspark code and run the flow.

Initially as part of Data Modeling I have gone through the data files and desined a data model 
which can be used a reference point when creating DB data and tranforming the data and loading 
it into a Database (for exaple in our case a Hive table or Postgressql table)

The Data model for the given data is in Novo_case.pdf file which defines table structure and 
the data fields and the relation between each table.

I have created this repository with the flowing structure 

1. Input Folder has all the input data CSV files 

2. Logs folder has the debub file where I am writing all the logs to it while running the code.

3. src folder will have the functional pyspark code where the code will read all the data files 
   into pyspark dataframes and trnaform them and load into postgressql tables.

4. Docker file, In which I have a pyspark docker images which will help me to dockerise the solution
   and execute the functional code to tranform and load the data files to the destination.

5. requirements.txt file will have all the required dependecies for my functinal to run and will 
   install and import in the code.

Way to use the docker:

1. for building the docker file we need to execute the below command which will build the docker image named sparkhome.
    
   docker build . -t sparkhome

2. to list and see the build docker image run the ls commmand and see the list of docker images created.

   docker image ls

3. to run the docker image use the below command which will run the image and create a container called spark to run our pyspark code.

   docker run --platform linux/amd64 -p 8888:8888 --name spark -d sparkhome

  We can run this or in the container logs we can get the jypiter notebook access with pyspark sessions where we can just execute the code.

  docker logs spark(container name)



PostgressSql scripts:

We can create the DDLs of the tables insise the postgressql schema by defining the DDLs for each table or in the code while writing the data to the tables. And I feel the best way is to have the DDLs defined insise postgress schema tables in this case.

The schema will look like this for each table.

    CREATE TABLE AWBMasterbillDetailsCBS (
        Shipping_No INT PRIMARY KEY,
        TrackingNumber VARCHAR (50),
        From VARCHAR VARCHAR (50),
        To VARCHAR (50),
        Estimated Departure VARCHAR (50),
        Estimated Arrival VARCHAR (50),
        Index INT 
    );

    
    CREATE TABLE AWBShipmentDetailsCBS (
        Shipping_No INT PRIMARY KEY, 
        TrackingNumber VARCHAR (50),
        Forwarder VARCHAR (50),
        Currency  VARCHAR (50),
        Total_Volume_cbm float,
        Origin_Code VARCHAR (50),
        Origin  VARCHAR (50),
        Origin_Country_Region VARCHAR (50),
        Proof_Of_Delivery_Date TIMESTAMP,
        Service_Product  VARCHAR (50),
        Delivery_Terms VARCHAR (50),
        Total_Pieces INT,
        Total_Actual_Weight  VARCHAR (50),
        Destination_Code  VARCHAR (50),
        Destination  VARCHAR (50),
        Destination_Country_Region  VARCHAR (50),
        Proof_Of_Delivery_Name  VARCHAR (50),
        Current_Shipment_Status  VARCHAR (50),
        Date TIMESTAMP
    );


    CREATE TABLE AWBShipmentProgressCBS (
        Shipping_No INT PRIMARY KEY, 
        TrackingNumber VARCHAR (50),
        Status VARCHAR (50),
        Flight_Number VARCHAR (50),
        Location VARCHAR (50),
        Date TIMESTAMP,
        Time VARCHAR (50),
        Index INT
    );

    CREATE TABLE ShipmentEquipmentCBS (
        Shipping_No INT PRIMARY KEY, 
        Type_of_Transportation VARCHAR (50),
        Origin VARCHAR (50),
        Country_Of_Destination VARCHAR (50),
        Equipment VARCHAR (50),
        Sum_full_pallets INT,
        Sum_shipperboxes INT,
        Forwarder VARCHAR (50),
        Airline_Name VARCHAR (50)
    );


    CREATE TABLE TracerReadingsCBS (
        Shipping_No INT PRIMARY KEY, 
        TT_Id INT,
        Type_of_Transportation VARCHAR (50),
        Origin VARCHAR (50),
        Country_Of_Destination VARCHAR (50),
        Mission_Started TIMESTAMP,
        Mission_Ended TIMESTAMP,
        Date_Time_Of_Temp VARCHAR (50),
        Temp_Point INT,
        Temp Float,
        Rounded_Temp float,
        Product VARCHAR (50)
    );