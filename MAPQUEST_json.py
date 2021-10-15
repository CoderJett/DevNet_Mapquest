import urllib.parse
import colorama
from colorama import Fore, Back, Style
#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM, NORMAL, BRIGHT, RESET_ALL
colorama.init(autoreset=True)
from pip._vendor import requests


main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "QAWzHgeqVXpkMAWzKGojDst5CNgXiAq1"
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print(Fore.RED +"<><><><><><><><><><><><><><><><><><><><><><><>")
        print(Fore.CYAN + Style.BRIGHT + Back.WHITE + "Directions from " + (orig) + " to " + (dest))
        print(Fore.GREEN+"Trip Duration: " + Fore.BLUE + (json_data["route"]["formattedTime"]))
        print(Fore.GREEN+"Kilometers: " + Fore.BLUE + str("{:.2f}".format(json_data["route"]["distance"] * 1.6 ))) #changed into KM
        print(Fore.GREEN+"Fuel Used (Liters): " + Fore.BLUE + str("{:.2f}".format(json_data["route"]["fuelUsed"] * 3.78 ))) #changed into Liters
        
        #added FEATURE Toll Roads and Route Type
        print(Fore.GREEN + "Toll Roads between: " + Fore.BLUE + str(json_data["route"]["hasTollRoad"]))
        print(Fore.GREEN + "Route Type: " + Fore.BLUE + str(json_data["route"]["options"]["routeType"]))
        print(Fore.RED +"<><><><><><><><><><><><><><><><><><><><><><><>\n")
        
        #added FEATURE GEOLOCATOR Longitude and Latitude
        print(Fore.RED + "<><><><><><><><><><><><><><><><><><><><><><><>")
        print(Fore.CYAN + Style.BRIGHT + Back.WHITE + "DISPLAY LONGITUDE and LATITUDE")
        for each in json_data["route"]["locations"][0]["latLng"]:
            print (Fore.GREEN+ "LOCATION ➪ " + Fore.BLUE + str(json_data["route"]["locations"][0]["latLng"] ) )
            
        print(Fore.RED +"<><><><><><><><><><><><><><><><><><><><><><><>\n")
        
        #added NARRATIVE 
        print(Fore.RED + "<><><><><><><><><><><><><><><><><><><><><><><>")
        print(Fore.CYAN + Style.BRIGHT + Back.WHITE + "Travel narrations of " + (orig) + " to " + (dest))
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(Fore.CYAN + (each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print(Fore.RED +"<><><><><><><><><><><><><><><><><><><><><><><>\n")

        
        #added FEATURE mapURL link providing snapshot of the location
        print(Fore.RED +"<><><><><><><><><><><><><><><><><><><><><><><>")
        print(Fore.CYAN + Style.BRIGHT + Back.WHITE + "Static Maps URL for " + (orig) + " to " + (dest) + " route:")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            try:
                print (Fore.GREEN+ "LINK ➪ " + Fore.BLUE+ (each["mapUrl"]) )
            except KeyError:
                print(Fore.BLACK + Back.WHITE + "    100% FINISH    ")
                
          #colorama error code      
    elif json_status == 402:
        print(Fore.RED + "**********************************************")
        print(Fore.RED + "Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print(Fore.RED + "**********************************************\n")
    elif json_status == 611:
        print(Fore.RED + "**********************************************")
        print(Fore.RED + "Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print(Fore.RED + "**********************************************\n")
    else:
        print(Fore.BLUE + "************************************************************************")
        print(Fore.BLUE + "For Status Code: " + str(json_status) + "; Refer to:")
        print(Fore.BLUE + "https://developer.mapquest.com/documentation/directions-api/status-codes")
        print(Fore.BLUE + "************************************************************************\n")