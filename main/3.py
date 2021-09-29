import os,shutil
name = os.getlogin()
link = f"C:\\Users\\{name}\\Desktop"
os.chdir(link)
print(os.getcwd())
list = os.listdir(os.getcwd())
for new in list:
    if "." in new:
        try:
            os.remove(new)
        except:
            print("Error")
    else:
        shutil.rmtree(new)