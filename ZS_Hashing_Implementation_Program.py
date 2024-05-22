#Zach Sewell
#Hashing Implementation
'''This program calculates the load factor of an array.'''


def calculate_load_factor(array_size, number_of_elements):

    load_factor = number_of_elements / array_size
    return load_factor

def display_key_value_implementation(array):


    for i in range(len(array)):
        print(f"key: {i}, value: {array[i]}")

#The main function.
def main():
    
    #Get the size of the array from the user.
    array_size = int(input("Enter the size of the array: "))

    #Get the elements of the array from the user.
    array = []
    for i in range(array_size):
        array.append(int(input(f"Enter element {i + 1}: ")))

    #Calculate the load factor of the array.
    load_factor = calculate_load_factor(array_size, len(array))

    #Display the load factor of the array.
    print(f"Load factor: {load_factor}")

    #Display the key-value implementation of the array.
    display_key_value_implementation(array)

if __name__ == "__main__":
    main()
