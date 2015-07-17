# Skript: command_line
# Date: 16.07.2015
# Author: Eugen Geist
# Summary: Provides a method to execute bash commands.


import subprocess


def exec_command(command, dir=None):
	print("Command: " + command)
	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, cwd=dir)
	return process.communicate()[0]
