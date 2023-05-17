import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Santiago, Cl"
dest = "Ovalle, Cl"
key = "H7uYHxGVsuxCNjJPKpukTX19qYWvxh4G"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
json_data = requests.get(url).json()

print("Kilometers: " + str((json_data["route"]["distance"])*1.61))