from subprocess import call
import os
if __name__ == "__main__":
    start


def start():
    exit = False

    while not exit:
        choice = int(
            input("1. Download movie\n2. Download movies plylist\n0.Exit\n=> "))
        if choice == 1:
            URL = input("Enter movie url => ")
            get_movie(URL)
        elif choice == 0:
            exit = True
        else:
            print("Use -h or --help")


def get_movie(URL):
    movie_info = "youtube-dl " + URL + " -F"
    call(movie_info.split(), shell=False)
    choice_format = input("Format code => ")
    command = "youtube-dl -f " + choice_format + " " + URL + " -c"
    os.chdir("Downloads")
    call(command.split(), shell=False)
