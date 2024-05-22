#Zach Sewell
#Lines of text
""""""

#Read file that user enters
def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

#Display line selected
def display_current_line(lines, current_line):
    print(lines[current_line])

#Asks user for file name to open, Reads file, loops menu for user.
#Series of If staments based on user input. 
def main():
    filename = input("Enter a file name to see the content: ")
    lines = read_file(filename)
    current_line = 0

    while True:
        print("\nMenu Options:")
        print("Press 'f' to see the first line")
        print("Press 'l' to see the last line")
        print("Press 'p' to see previous line")
        print("Press 'n' to see next line")
        print("Press 'd' to delete current line")
        print("Press 'r' to replace current line")
        print("Press 'i' to insert a line at current cursor position")
        print("Press 's' to save the current file")
        print("Press 'q' to quit")

        choice = input("Enter your choice: ")

        #Displays first line
        if choice == 'f':
            current_line = 0
            display_current_line(lines, current_line)

        #Displays last line
        elif choice == 'l':
            current_line = len(lines) - 1
            display_current_line(lines, current_line)

        #Displays previous line
        elif choice == 'p':
            if current_line > 0:
                current_line -= 1
            display_current_line(lines, current_line)

        #Displays next line
        elif choice == 'n':
            if current_line < len(lines) - 1:
                current_line += 1
            display_current_line(lines, current_line)

        #Deletes current line
        elif choice == 'd':
            del lines[current_line]
            if current_line >= len(lines):
                current_line = len(lines) - 1
            if current_line >= 0:
                display_current_line(lines, current_line)

        #replaces current line with user input text
        elif choice == 'r':
            new_line = input("Enter the new line: ")
            lines[current_line] = new_line
            display_current_line(lines, current_line)

        #inserts line at current point
        elif choice == 'i':
            new_line = input("Enter the new line: ")
            lines.insert(current_line, new_line)
            display_current_line(lines, current_line)

        #saves file with current edits
        elif choice == 's':
            with open(filename, 'w') as f:
                f.writelines(lines)
            print("File saved successfully")

        #breaks loop and quits
        elif choice == 'q':
            break

        #Displays if invalid input is entered
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()