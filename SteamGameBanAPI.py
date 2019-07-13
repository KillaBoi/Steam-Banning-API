import requests
import json # Will be used to check JSON API output after implementation

print("Welcome to the Steam Game Ban API!\n\nPlease select one of the options below that you would like to execute.")
getRequest = input("\n1: Report Profile\n2: Ban Profile\n3: Unban Profile\nUse '#' to go back to this menu at any time.\n> ")
if getRequest == "1":
    print("You have selected to Report a Profile.")
if getRequest == "2":
    print("\nYou have selected to Ban a Profile.\nPlease make sure you have already reported this profile beforehand otherwise this API call will not work.\n")
    confirmReport = input("\nCan you confirm you have already reported the profile you would like to ban? Y/N\n> ")
    if confirmReport == "Y":
        print("\nYou have confirmed that you have successfully reported the profile you would like to ban. The program will now continue.\n")
        print("You will require the following information. Please ensure you are are ready with it.\n• Steamworks Web API PUBLISHER Key (Normal WEBAPI Keys WILL NOT work)\n• SteamID64 of the user who was reported\n• AppID of the game where the ban should be applied\n• ReportID from the report that you should have done earlier.\n• Cheat Description (Reason why they are banned for example)\n• Duration of ban in seconds (0 = PERMANENT)\nNOTE: Ban delays will be turned off for this however you can edit this script to turn them back on.\n")
        print("")
        steamworksAPIkey = input("Please enter your Steamworks API PUBLISHER key\n> ")
        steamID64Reported = input("Please input the SteamID64 of the person you have reported\n> ")
        appIDReported = input("Please input the AppID of the game where the user was reported\n> ")
        reportIDReported = input("Please input the ReportID received from reporting the user\n> ")
        cheatDescriptionReported = input("Please input a reason for the ban\n> ")
        banDuration = input ("Please input a duration for the ban in seconds (0 seconds = PERMANENT ban)\n> ")
        
        banURL = 'https://partner.steam-api.com/ICheatReportingService/RequestPlayerGameBan/v1/' #Make sure to update this if the API URL ever changes
        params = {'key': steamworksAPIkey, 'steamid': steamID64Reported, 'appid': appIDReported, 'reportid': reportIDReported, 'cheatdescription': cheatDescriptionReported, 'duration': banDuration, 'delayban': 'false'} #Make sure to update this if the API params ever change

        sendBan = requests.post(url=banURL, data=params)
        if sendBan.status_code == requests.codes.ok:
            print("Your ban request was successful!")
        else:
            print("There was an error in your request.")
    if confirmReport == "N":
        print("You have not yet reported the user! This information provided from this step is needed. Program will now restart so you can complete the first step and obtain a ReportID.")
    
if getRequest =="3":
    print("\nYou have selected to unban a previously banned profile.")
    print("You will require the following information. Please ensure you are are ready with it.\n• Steamworks Web API PUBLISHER Key (Normal WEBAPI Keys WILL NOT work)\n• SteamID64 of the user who was banned\n• AppID of the game where the ban was applied\n")
    steamworksAPIkeyBanned = input("Please enter your Steamworks API PUBLISHER key\n> ")
    steamID64Banned = input("Please input the SteamID64 of the person who was banned\n> ")
    appIDBanned = input("Please input the AppID of the game where the user was banned\n> ")
    
    
    unbanURL = 'https://partner.steam-api.com/ICheatReportingService/RemovePlayerGameBan/v1/' #Make sure to update this if the API URL ever changes
    params = {'key': steamworksAPIkeyBanned, 'steamid': steamID64Banned, 'appid': appIDBanned} #Make sure to update this if the API params ever change

    sendunBan = requests.post(url=unbanURL, data=params)
    #print(sendBan.text)
    if sendunBan.status_code == requests.codes.ok:
        print("Your unban request was successful!")
    else:
        print("There was an error in your request.")

else:
    print("The option you selected do not match any of those above. Please retry.")