import argparse
import csv
# Library for converting UTM coordinates to latitude and longitude
from pyproj import Proj

def convert_coordinates(input_file, output_file):
    with open(input_file, 'r') as csv_file, open(output_file, 'w') as txt_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row
        
        for row_num, row in enumerate(csv_reader, start=1):
            GCP, easting, northing = row[:3] 
            if (len(GCP) < 1):
                break			
            easting = float(easting)
            northing = float(northing)
            
            
            utm_proj = Proj(proj='utm', zone=12, ellps='WGS84')
            longitude, latitude = utm_proj(easting, northing, inverse=True)
            

            txt_file.write(f"{row_num}" + ".0" + f", {latitude}, {longitude}\n")
    
    print("Conversion completed successfully!")

def main():
    parser = argparse.ArgumentParser(description='Convert UTM coordinates to latitude and longitude.')
    
    # Add input file argument
    parser.add_argument('input_file', type=str, help='path to the input CSV file')
    
    # Add output file argument
    parser.add_argument('-o', '--output_file', type=str, help='path to the output text file')
    

    args = parser.parse_args()

    if args.output_file:
        output_txt_file = args.output_file
    else:
        output_txt_file = "gcp_coordinates.txt"
    
    convert_coordinates(args.input_file, output_txt_file)

if __name__ == '__main__':
    main()