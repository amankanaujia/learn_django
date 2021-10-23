import os

def main():
    i = 1
    path = "D:/Download/Torrent/Money Heist S01-S04/Money Heist S01/"
    for filename in os.listdir(path):
        new_name = "Money Heist S01 E0" + str(i) + ".mkv"
        old_path = path + filename
        new_path = path + new_name
        os.rename(old_path,new_path)
        i = i+1

if __name__ == '__main__':
    main()