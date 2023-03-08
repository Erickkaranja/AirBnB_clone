PROJECT DESCRIPTION

This is a full web application which we will be building by the use of other tools such as HTML/CSS templating, database storage, API, front-end integration etc…. This project is based some tasks which are linked to the directory of the project using another online platform called GitHub. 

Each Task will help us to:

	- put in place a parent class (called BaseModel) to take care of the 	initialization, serialization and deserialization of your future instances

	- Create a simple flow of serialization/deserialization: Instance <-> 	Dictionary <-> JSON string <-> file

	- Create all classes used for AirBnB (User, State, City, Place…) that inherit 	from BaseModel.

	- Create the first abstracted storage engine of the project: File storage.

	- Create all unittests to validate all our classes and storage engine


COMMAND INTERPRETER DESCRIPTION

- This is a command-line interface (CLI) program designed to provide a simple interpreter for executing a set of predefined commands. The program is written in Python and allows the user to interact with it through the command-line interface.

- The command interpreter is a simple CLI program that accepts user input in the form of commands and executes them. The program provides a set of predefined commands that allow the user to perform various operations.


HOW TO START THE PROGRAM

- To start the program, you will need to have Python installed on your system. Once you have installed Python, follow these steps:

	- Clone the repository or download the source code
	- Open the terminal or command prompt
	- Navigate to the directory where the program is located
	- Run the following command to start the program:
	(python main.py)


HOW TO USE THE PROGRAM

- The program accepts user input in the form of commands. To execute a command, simply type it into the command line and press enter. The program will then execute the command and provide any output that may be required.

The following commands are currently supported by the program:

help: displays a list of available commands and their descriptions
create <filename>: creates a new file with the specified name
delete <filename>: deletes the specified file
rename <filename> <new_filename>: renames the specified file to the new name
read <filename>: displays the contents of the specified file
write <filename> <content>: writes the specified content to the specified file


EXAMPLES

- To create a new file named example.txt, enter the following command:
(create example.txt)

- To delete a file named example.txt, enter the following command:
(delete example.txt)

- To rename a file named example.txt to new_example.txt, enter the following command:
(rename example.txt new_example.txt)

- To read the contents of a file named example.txt, enter the following command:
(read example.txt)

- To write some content to a file named example.txt, enter the following command:
(write example.txt "Hello, world!")
