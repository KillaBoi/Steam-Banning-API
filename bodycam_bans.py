import requests
import json

print("Minimal Banning Script created by Killa (https://twitter.com/killa) for Bodycam\n\n")
print("You will require the following information. Please ensure you are are ready with it.\n- Steamworks Web API PUBLISHER Key (Normal WEBAPI Keys WILL NOT work)\n- SteamID64 of the user who was reported\n- AppID of the game where the ban should be applied\n- Cheat Description (Reason why they are banned for example)\n- Duration of ban in seconds (0 = PERMANENT)\nNOTE: Ban delays will be turned off for this however you can edit this script to turn them back on.\n")
steamworksAPIkey = input("Please enter your Steamworks API PUBLISHER key\n> ")
steamID64Reported = input("Please input the SteamID64 of the account\n> ")
appIDReported = input("Please input the AppID of the game\n> ")
cheatDescriptionReported = input("Please input a reason for the ban\n> ")
banDuration = input ("Please input a duration for the ban in seconds (0 seconds = PERMANENT ban)\n> ")


reportURL = 'https://partner.steam-api.com/ICheatReportingService/ReportPlayerCheating/v1/'
banURL = 'https://partner.steam-api.com/ICheatReportingService/RequestPlayerGameBan/v1/'

reportParams = {'key': steamworksAPIkey, 'steamid': steamID64Reported, 'appid': appIDReported}


sendReport = requests.post(url=reportURL, data=reportParams)
if sendReport.status_code == requests.codes.ok:
    print("Report ID Request Successful")
    convertReportData = sendReport.json()
    tested = json.dumps(convertReportData)
    reportidentifier = convertReportData['response']['reportid']
    print('The Report ID for this session is:', reportidentifier)
    print("[ReportRequest] Full Response: ", tested)


    banParams = {'key': steamworksAPIkey, 'steamid': steamID64Reported, 'appid': appIDReported, 'reportid': reportidentifier, 'cheatdescription': cheatDescriptionReported, 'duration': banDuration, 'delayban': 'false'}
    sendBan = requests.post(url=banURL, data=banParams)
    if sendBan.status_code == requests.codes.ok:
        sendBanResponse = sendBan.json()
        try: 
            if sendBanResponse['response']['steamid']:
                print("Your ban request was successful!")
                print("[BanRequest] Full Response: ", sendBan.text)
            else:
                print("There was an error in your ban request")
                print("[BanRequest] Full Response: ", sendBan.text)
        except:
            print("There was an error in your ban request")
            print("[BanRequest] Full Response: ", sendBan.text)
else:
    print("Something somewhere went terribly wrong :(")
