# DQ_Report_App
Takes a raw .csv file, removes unnecessary columns, and makes them into the proper format for the report. 
1) Install requirements with pip install -r requirements.txt
2) Create directory called unedited in project directory.
3) Put original .csv file in unedited directory.
4) Run python DQReport.py -file filename.csv -type 1

^ (1 for PODQ report, 2 for SODQ report) ^

5) Output file is saved to /edited/EDIT_filename.csv
