import requests

print("Welcome to the Steam Game Ban API!\n\nPlease select one of the options below that you would like to execute.")
getRequest = input("\n1: Report Profile\n2: Ban Profile\nUse '#' to go back to this menu at any time.\n> ")
if getRequest == "1":
    print("You have selected to Report a Profile.")
if getRequest == "2":
    print("\nYou have selected to Ban a Profile.\nPlease make sure you have already reported this profile beforehand otherwise this API call will not work.\n")
    confirmReport = input("\nCan you confirm you have already reported the profile you would like to ban? Y/N\n> ")
    if confirmReport == "Y":
        print("\nYou have confirmed that you have successfully reported the profile you would like to ban. The program will now continue.\n")
        print("You will require the following information. Please ensure you are are ready with it.\n• Steamworks Web API PUBLISHER Key (Normal WEBAPI Keys WILL NOT work)\n• SteamID64 of the user who was reported\n• AppID of the game where the ban should be applied\n• ReportID from the report that you should have done earlier.\n• Cheat Description (Reason why they are banned for example)\n• Duration of ban in seconds (0 = PERMANENT)\nNOTE: Ban delays will be turned off for this however you can edit this script to turn them back on.\n")
    if confirmReport == "N":
        print("You have not yet reported the user! This information provided from this step is needed. Program will now restart so you can complete the first step and obtain a ReportID."
        break   
else:
    print("The option you selected do not match any of those above. Please retry.")