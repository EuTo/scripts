# Skript: compile_install_mongodb_pi
# Date: 16.07.2015
# Author: Eugen Geist
# Summary: Grabs the most up to date mongodb source for nonX86 architectures compiles and installs it.
#          Script created on the basis of: http://c-mobberley.com/wordpress/2013/10/14/raspberry-pi-mongodb-installation-the-working-guide/

import command_line
import sys
import os

ESSENTIALS = "sudo apt-get -y install build-essential libboost-filesystem-dev libboost-program-options-dev libboost-system-dev libboost-thread-dev scons libboost-all-dev python-pymongo git"
CLONE_GIT = "git clone https://github.com/skrabban/mongo-nonx86"
USER_CREATION = "sudo adduser --firstuid 100 --ingroup nogroup --shell /etc/false --disabled-password --gecos "" --no-create-home mongodb"


def get_user_confirmation():
    print()
    if input("Everything went alright? Continue?(Y/N)").lower() != "y":
        print("Installation aborted...")
        sys.exit(1)

if __name__ == '__main__':

    
    if sys.version_info[0] < 3:
        print("Please use Python3 for this script...")
        sys.exit(1)

    #Grab needed packages for compilation    
    print("Getting essential packages...")
    print(command_line.exec_command(ESSENTIALS))
    get_user_confirmation()

    print("Cloning MongoDB Github repository...")
    os.chdir("/home/pi/")
    print(command_line.exec_command(CLONE_GIT))
    get_user_confirmation()

    print("The following commands take a lot of time, do you want to continue?(Y/N)")
    if(input().lower() != "y"):
        print("Installation aborted...")
        sys.exit(1)

    print("You won't need to confirm anything anymore...")
    print("Compiling MongoDB...")
    os.chdir("/home/pi/mongo-nonx86")
    print(command_line.exec_command("sudo scons"))
    print("...compilation done.")

    print("Installing MongoDB...")
    print(command_line.exec_command("sudo scons --prefix=/opt/mongo install"))
    print("...installation done.")

    print("Creating needed user...")
    print(command_line.exec_command(USER_CREATION))
    print("...creating users done.")

    print("Create log folder...")
    print(command_line.exec_command("sudo mkdir /var/log/mongodb/"))
    print(command_line.exec_command("sudo chown mongodb:nogroup /var/log/mongodb/"))
    print("...log folder created.")

    print("Create folder for state data...")
    print(command_line.exec_command("sudo mkdir /var/lib/mongodb"))
    print(command_line.exec_command("sudo chown mongodb:nogroup /var/lib/mongodb"))
    print("...state folder created.")

    print("Moving around some config files...")
    print(command_line.exec_command("sudo cp debian/init.d /etc/init.d/mongod"))
    print(command_line.exec_command("sudo cp debian/mongodb.conf /etc/"))

    print("Linking up and getting permissions...")
    print(command_line.exec_command("sudo ln -s /opt/mongo/bin/mongod /usr/bin/mongod"))
    print(command_line.exec_command("sudo chmod u+x /etc/init.d/mongod"))
    print(command_line.exec_command("sudo update-rc.d mongod defaults"))

    print("If everything went alright, you can start mongodb with the following command: ")
    print("sudo /etc/init.d/mongod start")
    input("Press any key to finish...")
