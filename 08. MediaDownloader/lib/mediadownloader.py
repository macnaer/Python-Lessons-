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
        elif choice == 2:
            URL = input("Enter playlist url => ")
            get_playlist(URL)
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


def get_playlist(URL):

    choice_format = input(
        "18           mp4        640x360    360p  700k , avc1.42001E, mp4a.40.2@ 96k (44100Hz), 16.30MiB (best)")
    os.chdir("Downloads")
    command = "youtube-dl -f " + choice_format + " " + URL + " -c"
    call(command.split(), shell=False)
