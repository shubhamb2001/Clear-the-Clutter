"""
Clear the Clutter

This program helps organize files of a specific type in a given folder by 
renaming them sequentially. 

Functionality:
1. Counts the number of files for each file extension in the specified folder.
2. Prompts the user to select a file type (extension) to organize.
3. Renames all files of the chosen type sequentially (1.extension, 2.extension, ...).
4. Prints a mapping showing each original file name and its new name.

This is useful for quickly clearing clutter and maintaining consistent 
naming for a particular type of files (e.g., .xlsx, .txt, .png) in a folder.
"""







import os
old_files=[]
tail=[]
count={}
final={}
path= input("Enter the path of your folder: ")
path=fr"{path}"
files=os.listdir(path)


for i in range(len(files)):
    h,t=os.path.splitext(files[i])
    tail.append(t)

for i in tail:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

for i  in count.keys():
    if count[i]==1:
        print(f"You Have {count[i]} {i} file")
    else:
        print(f"You Have {count[i]} {i} files ")
        
    


while True:
    change=input("\nType the file type for which you want to Clear the Clutter:")
    if change not in count.keys():
        print(f"{change} files does not exist!!.\nEnter file type from the given list")
    else:
        break

for file in files:
    if file.endswith(change):
        old_files.append(file)

for i,file in enumerate(old_files,start=1):
        old_path=os.path.join(path,file)
        new_name=f"{i}{change}"
        new_path=os.path.join(path,new_name)
        if old_path==new_path:
            continue
        else:
            
            os.rename(old_path,new_path)
        final[file]=new_name
            
for old,new in final.items():
    print(f"\n {old} has been changed to {new} ", flush=True)


    
    





