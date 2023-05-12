#### GCP Coordinates Conversion Script
This script converts geographic information captured from a GPS rover to the expected format used by the PhytoOracle processing pipelines.

Prerequisites:
* Excel workbook (XLSX) with two sheets containing ground control point (GCP) number, easting, northing, and altitude. See Gantry_GCP_Coordinates_2023.xlsx for an example.

Steps:
1) Beginning with the Excel workbook, save each worksheet as a CSV.
2) Run the script, specifying the input CSV and the output text file. <br>
```python gcp_conversion.py \.Gantry_GCP_Coordinates_2023_paint.csv -o gcp_paint.txt```<br>
In this example, a set of GCPs called 'Paint' are listed in a CSV file. The ```-o``` output flag directs the script to output the results to the specified text file.
4) Check the results of the conversion, then upload the resultant files to the level 0 necessary files directory for the season, following the established naming convention. 

This script is hardcoded for UTM zone 12 and uses [pyproj](https://pyproj4.github.io/pyproj/stable/api/proj.html) to perform the cartographic transformation.
