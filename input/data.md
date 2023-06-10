# Data Dictionary

Note: temp tracer, temp logger, logger = all words to describe the IoT sensor that is put on the shipments.
All of this data is for the lanes DK-> Canada and DK -> Japan. There are about 370 shipments for you to explore.
Additionally on 85 shipments additional data has been collected form various sources, this data is scraped from DHL.

* * *

**File:** ShipmentEquipmentCBS.csv
**Size:** 371 rows
This dataset tells basic information about each shipment, such as what equipment it is in.

**Shipping_No:** This is the Novo Shipping number

**Type_of_Transportation:** The main mode of transportation. In this dataset they should all be Airfreight.

**Origin:** Starting point of the shipment. Should always be DK in this dataset which is the Shipping Warehouse located in Greve, DK.

**Country_Of_Destination:** This is the destination country of the shipment. In this dataset, this is the most specific we get in where the shipment goes in the world.

**Equipment:** This is what equipment the shipment was shipped in. Please see the additional file for more information about this column

**Sum_Full_Pallets:** For most shipments, we know how many full pallets the shipment contained

**Sum_Shipperboxes:** For most shipments, we know how many shipperboxes the shipment contained

**Forwarder:** What company did we use as a freight forwarder for this shipment?

**Airline_Name:** The airline the shipment was sent with

* * *

**File:** TracerReadings.csv
**Size:** 334,883 rows
This datafile includes a subset of readings from the temperature loggers. It includes 85 airfreight shipments from the lanes DK-> Canada and DK -> Japan. Data was collected in 2018 by TSS and uploaded by Novo Nordisk Supply Chain Analytics. The data has been given to CBS students for analysis.
The unique key for this table is Shipping_No,TT_Id,Temp_Point

**Shipping_No:** This is the Novo Shipping number

**TT_Id:** This is the ID of the temp tracer. Each Shipping_No can have multiple Tracer_Id

**Type_of_Transportation:** The main mode of transportation. In this dataset they should all be Airfreight.

**Origin:** Starting point of the shipment. Should always be DK in this dataset which is the Shipping Warehouse located in Greve, DK.

**Country_Of_Destination:** This is the destination country of the shipment. In this dataset, this is the most specific we get in where the shipment goes in the world.

**Mission_Started:** This is the first timestamp where the logger was turned on. This is not necessarily the same as the first temperature reading for this logger.

**Mission_Ended:** This is the last timestamp where the logger was turned on. This is not necessarily the same as the last temperature reading for this logger.

**Date_Time_Of_Temp:** This is the timestamp of the temperature reading. All have been converted to DK time

**Temp_Point:** This is a counting index of what number reading this row is on the specific tracer. In this dataset it might not necessarily start at 1,
but it should always be consecutive.

**Temp:** The exact temperature reading

**Rounded_Temp:** The temperature reading rounded to two decimal points

**Product:** A short description of the product inside the corresponding shipper box

* * *

**File:** AWBMasterbillDetailsCBS.csv
**Size:** 118 rows
This datafile we scrape from the web, and gives flight information for the 85 shipments.

**Shipping_No:** This is the novo Shipping number  

**TrackingNumber:** This is the DHL house airway bill number

**From:** The departing airport

**To:** The receiving airport

**Estimated Departure:** Just how it sounds. It is in local time for the departing airport.

**Estimated Arrival:** Also just how it sounds. It is in local time for the arrival airport.

**Index:** This is a counter reseting for each shipment. Starts at 0.

* * *

**File:** AWBMasterbillDetailsCBS.csv
**Size:** 118 rows
This datafile we scrape from the web, and gives flight information for the 85 shipments.

**Shipping_No:** This is the novo Shipping number  

**TrackingNumber:** This is the DHL house airway bill number

**From:** The departing airport

**To:** The receiving airport

**Estimated Departure:** Just how it sounds. It is in local time for the departing airport.

**Estimated Arrival:** Also just how it sounds. It is in local time for the arrival airport.

**Index:** This is a counter resetting for each shipment. Starts at 0.

* * *

**File:** AWBShipmentDetailsCBS.csv
**Size:** 86 Rows
This datafile we scrape from the web, and gives the information about the shipment that the forwarder has. There has been no editing or cleaning to this file, it is exactly as scraped from the web.

**Shipping_No:** This is the novo Shipping number  

**TrackingNumber:** This is the DHL house airway bill number

**Forwarder:** Should always be DHL

**Currency:** What currency Novo paid the bill in

**Total Volume:** Total volume of the shipment in cbm.

**Origin Code:** DHL's origin code

**Origin:** Origin of shipment, normally a city name

**Origin Country:** Pretty self explanatory

**Proof of Delivery Date:** A timestamp where the delivery was received. Accuracy of this timestamp has not yet been assessed. In local time of destination.

**Service/Product:** Normally null unless express

**Delivery Terms:** Normally prepaid

**Total Pieces:** Number of cargo pieces.

**Total Actual Weight:** Weight of the shipment.

**Destination Code:** DHL's destination code (normally corresponds to airport)

**Destination:** Normally a city name

**Destination Country:** Destination country

**Proof of Delivery Name:** Some sort of key of who the shipment was delivered to and signed for

**Current Shipment Status:** Shipment status. Should all be "delivered"

**Date:** Last updated date of this shipment in DHLs data. Normally the same as delivery date.

* * *

**File:** AWSShipmentProgress.csv
**Size:** 469 rows
This data is scraped from DHLs website. It shows progress markets along the shipments journey. There has been no editing or cleaning to this file, it is exactly as scraped from the web.

**Shipping_No:** This is the novo Shipping number  

**TrackingNumber:** This is the DHL house airway bill number

**Status:** DHL's status of the delivery

**Flight Number:** normally null

**Location:** Location of the shipment at this progress mark

**Date:** Date of the progress marker (local time to location)

**Time:** Time of the progress marker (local time to location)

**Index:** The step of progress on the shipments journey. Counting restarts for each shipment. Counting starts at 0
