import os
import shutil
def organise_files(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            ext = filename.split('.')[-1]
            ext_dir = os.path.join(dest_dir, ext)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            shutil.copy(os.path.join(source_dir, filename), ext_dir)
            print(f"Moved {filename} to {ext_dir}")
if __name__ == "__main__": 
    
    source_directory = input("Enter the source directory path: ")
    destination_directory = input("Enter the destination directory path: ")
    organise_files(source_directory, destination_directory)
    print("Files organised successfully.")
    print("Files copied successfully.")