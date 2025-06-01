# This is a program to find the geographic location of an ip-address
# This program uses two api's that is being provided by ipstack and numverify

import ip_locator
import num_locator

import webbrowser
import math
import time

import json

#storing the logs in a log file with time and date
import logging
logging.basicConfig(filename='geo_logs.log', level=logging.INFO, format='%(asctime)s - %(message)s')

#decorative banner
import pyfiglet
print(pyfiglet.figlet_format("Geolocator"))

def checking_exsistance(choice,location):
    # a function to check the validity of the IP-address and phone number

        if choice == 1:
            # checking for the ip_locator program
            if location['continent_name'] == "null" and location['country_name'] == "null" and location['region_name'] == "null" and location['city'] == "null" and location['latitude'] == null and location['longitude'] == null:
                return "Can't find geo location for this IP"
            else:
                return "True"
        
        elif choice == 2:
            # checking for the num_locator program
            if location["valid"] == "False":
                return "the number doesn't exsist"
            else:
                return "True"


def print_location(choice,location):
    # printing all the useful information
    if choice == 1:
        print(f"\nContinent name:{location['continent_name']}")
        print(f"Country name:{location['country_name']}")
        print(f"Region name:{location['region_name']}")
        print(f"City:{location['city']}")
    else:
        print(f"\nCountry name:{location['country_name']}")
        print(f"Location:{location['location']}")
        print(f"SIM service:{location['carrier']}")


def find_dial_code(ccode):
    # Adding the country code function to check check the country code by the given 2-letter ISO
    with open("country_code/country_codes.json","r") as f:
        data = json.load(f)# Loading the full json file
        for codes in data:
            if ccode == codes["code"]:
                #searching throungh the loop if found returning the dial code of that country 
                return codes["dial_code"]
        else:
            return None


def map_viewer(x,y):
    # To see the coordinates in google maps
    
    # cheking in which hemisphere the location is
    if x >= 0:
        hemi_lat = "N"
    else:
        hemi_lat = "S"
    if y >= 0:
        hemi_lon = "E"
    else:
        hemi_lon = "W"

    # converting the latitude into degree,minute and second form
    deg_lat = abs(int(x))
    min_lat = abs((x - int(x)) * 60)  
    sec_lat = abs((min_lat - int(min_lat)) * 60)

    # converting longitude into degree,minute and second form
    deg_lon = abs(int(y))
    min_lon = abs((y - int(y)) * 60)
    sec_lon = abs((min_lon - int(min_lon)) * 60)

    # redirecting to google maps
    webbrowser.open(f"""https://www.google.com/maps/place/{str(deg_lat)}°{str(int(min_lat))}'{str(int(sec_lat))}"{hemi_lat}{str(deg_lon)}°{str(int(min_lon))}'{str(int(sec_lon))}"{hemi_lon}""") 

    # waiting for the browser to open and then exiting the program
    time.sleep(2)
    exit()

def main():
    print("[1]IP address locator\n[2]Phone number locator\n[3]Exit")
    exit = False# prob used to exit the while loop

    while(not exit):
        choice = int(input("\nEnter choice:"))
        if choice == 1:
            
            ip = input("Enter IP:")
            # passing the ip-address into the ip_loactor function present in ip_locator program
            location = ip_locator.ip_locator(ip) 
            check = checking_exsistance(choice,location)
            
            if check == "True":
                # if the ip-adress is valid
                print_location(choice,location)
                logging.info(f"ip_location->{ip} = ({location['latitude']},{location['longitude']})")#saving the log to geo_logs.log file
                map_viewer(float(location['latitude']),float(location['longitude']))
            else:
                # if ip-address is not valid (note:not all ip address can be located doesn't mean it is invalid)
                # here stated invalid just for understanding that you won't get a desired output
                print(check)
                logging.info(f"ip_location->{ip} = (null,null)")#saving the log to geo_logs.log file

        elif choice == 2:
            
            #Dial code is nessecery to get the output from the API so adding an additional program to find dial code
            ccode = input("Enter the 2-letter ISO code for your country:").upper()
            num = input("Enter phone number:")
            dial_code = find_dial_code(ccode)
            # passing the phone number into the num_loactor function present in num_locator program
            location = num_locator.num_locator(dial_code + num)
            check = checking_exsistance(choice,location)

            if check == "True":
                # if phone number is valid
                print_location(choice,location)
                logging.info(f"number_location->{num} = ({location['location']},{location['carrier']})")#saving the log to geo_logs.log file
            else:
                # if phone number is not valid (note:here invalid states that the phone number doesn't exist)
                print(check)
                logging.info(f"number_location->{num} = number doesn't exsist")#saving the log to geo_logs.log file

        elif choice == 3:
            exit = True# changing the probe value to exit the program
        else:
            print("Invaid choice!")

if __name__ == "__main__":
    main()
