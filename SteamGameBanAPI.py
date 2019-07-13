import requests
import json # Will be used to check JSON API output after implementation
import os # Used to clean up after ourselves

print("Welcome to the Steam Game Ban API!\n\nPlease select one of the options below that you would like to execute.")
getRequest = input("\n1: Report Profile\n2: Ban Profile\n3: Unban Profile\n4: Seamless Banning\n> ")


if getRequest == "1": # Reporting Profiles
    print("\nYou have selected to Report a Profile.")
    print("You will require the following information. Please ensure you are are ready with it.\n• Steamworks Web API PUBLISHER Key (Normal WEBAPI Keys WILL NOT work)\n• SteamID64 of the user who was banned\n• AppID of the game where the ban was applied\n")
    steamworksAPIkeyReporting = input("Please enter your Steamworks API PUBLISHER key\n> ")
    steamID64Reporting = input("Please input the SteamID64 of the person you would like to report\n> ")
    appIDReporting = input("Please input the AppID of the game where the user is being reported to\n> ")
    
    reportURL = 'https://partner.steam-api.com/ICheatReportingService/ReportPlayerCheating/v1/' #Make sure to update this if the API URL ever changes
    params = {'key': steamworksAPIkeyReporting, 'steamid': steamID64Reporting, 'appid': appIDReporting}
    
    sendReport = requests.post(url=reportURL, data=params)
    if sendReport.status_code == requests.codes.ok:
        print("Your report request was successful!")
        convertReportData = sendReport.json()
        tested = json.dumps(convertReportData)

        with open ('reportdata.txt', 'w+') as reportdata:
            print('{"payload":['+ tested +']}', file=reportdata)
            reportdata.close()
        
        with open ('reportdata.txt', 'r') as readreportdata:
            readreportjsondata = json.load(readreportdata)
            readreportdata.close()
        
        reportuser = readreportjsondata['payload'][0]['response']['reportid']
        print('The Report ID for this session is:', reportuser)
        os.remove("reportdata.txt")

    else:
        print("There was an error in your request.")




if getRequest == "2": # Banning Profiles
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
        print("You have not yet reported the user! The information provided from reporting a user is required. Program will now close so you can complete the first step and obtain a ReportID.")
    



if getRequest =="3": # Unbanning Profiles
    print("\nYou have selected to unban a previously banned profile.")
    print("You will require the following information. Please ensure you are are ready with it.\n• Steamworks Web API PUBLISHER Key (Normal WEBAPI Keys WILL NOT work)\n• SteamID64 of the user who was banned\n• AppID of the game where the ban was applied\n")
    print("")
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




if getRequest == "4": # Reporting Profiles
    print("\nYou have selected Seamless Banning.")
    print("You will require the following information. Please ensure you are are ready with it.\n• Steamworks Web API PUBLISHER Key (Normal WEBAPI Keys WILL NOT work)\n• SteamID64 of the user who was reported\n• AppID of the game where the ban should be applied\n• Cheat Description (Reason why they are banned for example)\n• Duration of ban in seconds (0 = PERMANENT)\nNOTE: Ban delays will be turned off for this however you can edit this script to turn them back on.\n")
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
        print("Your report request was successful!")
        convertReportData = sendReport.json()
        tested = json.dumps(convertReportData)

        with open ('reportdata.txt', 'w+') as reportdata:
            print('{"payload":['+ tested +']}', file=reportdata)
            reportdata.close()
        
        with open ('reportdata.txt', 'r') as readreportdata:
            readreportjsondata = json.load(readreportdata)
            readreportdata.close()
        
        reportuser = readreportjsondata['payload'][0]['response']['reportid']
        print('The Report ID for this session is:', reportuser)
        os.remove("reportdata.txt")


        banParams = {'key': steamworksAPIkey, 'steamid': steamID64Reported, 'appid': appIDReported, 'reportid': reportuser, 'cheatdescription': cheatDescriptionReported, 'duration': banDuration, 'delayban': 'false'}
        sendBan = requests.post(url=banURL, data=banParams)
        if sendBan.status_code == requests.codes.ok:
            print("Your ban request was successful!")
        else:
            print("There was an error in your request.")

    else:
        print("There was an error in your request.")