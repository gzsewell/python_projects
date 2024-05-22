
#Zach Sewell
#Parsing and Expressions
"""This program takes an expression from a given file and asks the user if they want to parse the expression
if yes, the program will parse the expression and write it to an output file. """


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def parse_expression_tree(tree):
    if isinstance(tree, Node):
        if tree.value == "+":
            return parse_expression_tree(tree.left) + parse_expression_tree(tree.right)
        elif tree.value == "-":
            return parse_expression_tree(tree.left) - parse_expression_tree(tree.right)
        elif tree.value == "*":
            return parse_expression_tree(tree.left) * parse_expression_tree(tree.right)
        elif tree.value == "/":
            return parse_expression_tree(tree.left) / parse_expression_tree(tree.right)
        else:
            return tree.value
    else:
        return tree

def save_result_to_file(result, filename):
    with open(filename, "w") as f:
        f.write(str(result))

if __name__ == "__main__":

    # Read the expression from the file.
    with open("C:\Python\ZS_Parsing_Expressions_Program\input.txt", "r") as f:
        expression = f.readline().strip()

    # Display the expression to the user.
    print("Given expression:", expression)

    # Ask the user if they want to parse the expression.
    choice = input("Want to parse the expression? (Y/N) ")

    if choice == "Y" or choice == "y":

        # Parse the expression tree.
        tree = Node(expression)
        result = parse_expression_tree(tree)

        # Save the result to a file.
        save_result_to_file(result,'output.txt')

        # Print the result to the console.
        print("The value of the expression:", result)

    else:
        print("Expression not parsed.")

