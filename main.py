import requests
import json

bearer_token = ""
agenda_data_from = "2024-08-24"
agenda_data_to = "2024-08-31"

headers = {"Authorization": f"Bearer {bearer_token}"}


response = requests.get("https://citadel.magister.net/api/account?noCache=0", headers=headers)

personjson = response.json()["Persoon"]

print("Welcome to Python Magister - Log-In successful.")



print("Welcome: " + personjson["Roepnaam"])

accessid = personjson["Id"]

print("Access Token: " + str(accessid))

print("Picture: blob:https://citadel.magister.net/" + response.json()["UuId"])

agenda = requests.get("https://citadel.magister.net/api/personen/" + str(accessid) + "/afspraken?status=1&tot=" + agenda_data_to + "&van=" + agenda_data_from, headers=headers)

items = agenda.json()["Items"]

try:
    first_hour = items[0]
    print(str(first_hour["LesuurTotMet"]) + " - " + first_hour["Omschrijving"])
except IndexError:
    first_hour = 'null'

try:
    second_hour = items[1]
    print(str(second_hour["LesuurTotMet"]) + " - " + second_hour["Omschrijving"])
except IndexError:
    second_hour = 'null'

try:
    third_hour = items[2]
    print(str(third_hour["LesuurTotMet"]) + " - " + third_hour["Omschrijving"])
except IndexError:
    third_hour = 'null'

try:
    third_hour = items[3]
    print(str(third_hour["LesuurTotMet"]) + " - " + third_hour["Omschrijving"])
except IndexError:
    third_hour = 'null'

input('Press ENTER to exit')