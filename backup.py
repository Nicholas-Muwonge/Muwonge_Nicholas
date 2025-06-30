import os
import time
import shutil   
from datetime import datetime, timedelta
def backup_files(source_folder, backup_folder, interval_minutes=3):
    """Backup files from source_folder to backup_folder if modified within the last interval_minutes."""
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    while True:
        current_time = datetime.now()
        for filename in os.listdir(source_folder):
            source_file = os.path.join(source_folder, filename)
            if os.path.isfile(source_file):
                last_modified_time = datetime.fromtimestamp(os.path.getmtime(source_file))
                if current_time - last_modified_time < timedelta(minutes=interval_minutes):
                    backup_file = os.path.join(backup_folder, filename)
                    shutil.copy2(source_file, backup_file)
                    print(f"Backed up: {filename} at {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        time.sleep(interval_minutes * 60)
if __name__ == "__main__":
    source_folder = "/home/nich_klaus/Downloads"  
    backup_folder = "/home/nich_klaus/Desktop/backup" 
    backup_files(source_folder, backup_folder, interval_minutes=3)
