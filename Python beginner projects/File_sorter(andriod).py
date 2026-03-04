import os
import shutil
import time

print("Sort[beta] only works on andriod for now.")

def sortdir(filename,destination):    
    path2 = f"/storage/emulated/0/{filename}"
    
    #Data center
    file_type = {}
    DIRS = []
    
    if os.path.exists(path2):
        for i in os.listdir(path2):
            DIRS.append(i.lower())

        start = time.time()
        path = f"/storage/emulated/0/{filename}/{destination}"
        
        if destination in DIRS:
            print(f"Destination folder '{destination}' already exists.")
            DIRS.remove(destination)
        else:
            os.makedirs(path,exist_ok = True) # Creates Destination folder/path
            
        if len(DIRS) == 0:
            print(f"Nothing to sort, Directory \"{filename}\" is empty!")
        else:
            print(f"{len(DIRS)} items found!\n")
            for z,i in enumerate(DIRS,start=1):
                print(f"{z} - {i}")
        print("\n")
            

        for index,file in enumerate(DIRS,start=1):
            Split = os.path.splitext(file)
            current_path = f"{path2}/{file}"
            type = Split[1].upper().strip(".")
            current_destination = f"{path}/{type}"
            
            if not os.path.exists(current_destination):
                current_deslist = []
            else:
                current_deslist = os.listdir(current_destination)
            
            if os.path.isfile(current_path):         
                if not Split[1] == '':
                    os.makedirs(current_destination,exist_ok = True)
                    if not file in current_deslist:
                        shutil.move(current_path,current_destination)
                        print(f"File {index}- Moved...")
                    else:
                        Rename = Split[0] + "(1)" + Split[1]
                        Rename_path = path2 + Rename
                        os.rename(current_path,Rename_path)
                        shutil.move(Rename_path,current_destination)
                        print("File :{file}' already exists in destination, Rename file with '{Rename}'")
                else:
                    os.makedirs(f"{path}/OTHERS",exist_ok = True)
                    if not file in current_deslist:
                        shutil.move(current_path,f"{path}/OTHERS")
                        print(f"File {index}- Moved to OTHERS...")
                    else:
                        Rename = file + "(1)"
                        Rename_path = path2 + Rename 
                        os.rename(current_path,Rename_path)
                        print(f"file -'{file}'- already exists in destination, Replaced file name with '{Rename}'")
                        shutil.move(Rename_path,current_destination)
                        
            else:
                if current_path not in current_deslist:
                    shutil.move(f"{path2}/{file}",f"{path}/FOLDERS/{file}")
                    print(f"Folder [{index}]- Moved...")
                else:
                    Rename = file + "(1)"
                    Rename_path = path2 + Rename
                    os.rename(current_path,Rename_path)
                    shutil.move(Rename_path,current_destination)
        
        end = time.time()
        
        if len(DIRS) >= 1:
            print(f"Mission Accomplished under {int(end)-int(start)} seconds.")
    else:
        print("File not found.")
        


filename = input("Enter file name> ")
destination = input("Set a file name whare you want to move this'all stuff = ").lower()

sortdir(filename,destination)   