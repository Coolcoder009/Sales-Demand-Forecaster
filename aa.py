import os

folder_path = r'D:\Downloads\Profanity\TAPAD\audio\en-us'
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

for file_name in files:
    print(file_name)
