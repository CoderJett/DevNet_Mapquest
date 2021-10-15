import urllib.parse
from pip._vendor import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington, D.C."
dest = "Baltimore, Md"
key = "QAWzHgeqVXpkMAWzKGojDst5CNgXiAq1"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
print("URL: " + (url))
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]
if json_status == 0:
 print("API Status: " + str(json_status) + " = A successful route call.\n")

