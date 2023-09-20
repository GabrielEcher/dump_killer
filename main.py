import os

def dmp_killer():
    folder_path = 'C://Cyberlog'

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.dmp'):
                file_path = os.path.join(root, file_name)
                os.remove(file_path) 
                           
if __name__ == "__main__":
    dmp_killer()