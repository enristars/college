def create_input_file(filename, sample_data=None):
    """
    creates a sample input file with dictionary data. The default sample data
    contains fruit colors and is used for testing the read and invert functions.
    """
    sample_data = sample_data or """apple: red
banana: yellow
cherry: red
mango: yellow
grapes: black, green
"""
    try:
        with open(filename, 'w') as file:
            file.write(sample_data)
        print(f"Sample input file '{filename}' created successfully.")
    except IOError:
        print(f"Error: Could not write to file '{filename}'.")

def read_dictionary(filename):
    """
    reads key-value pairs from a file into a Python dictionary, expecting
    lines in 'key: value' format. It will gnore lines without a colon.
    """
    dictionary = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                if ':' in line:
                    key, value = map(str.strip, line.split(':', 1))
                    dictionary[key] = value
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Try your code again.")
    return dictionary

def invert_dictionary(original_dict):
    """
    Inverts a dictionary: each unique value becomes a key, and all original
    keys associated with that value are stored in a list as values.
    """
    inverted_dict = {}
    for key, values in original_dict.items():
        for value in map(str.strip, values.split(',')):
            inverted_dict.setdefault(value, []).append(key)
    return inverted_dict


def write_dictionary(filename, dictionary):
    """
    Writes a dictionary to a file, formatting each key with its values list.
    """
    try:
        with open(filename, 'w') as file:
            for key, values in dictionary.items():
                file.write(f"{key}: {', '.join(values)}\n")
    except IOError:
        print(f"Error: Could not write to file '{filename}'.")


def main():
    input_file = 'original_dict.txt'     # Input file with original dictionary
    output_file = 'inverted_dict.txt'    # Output file for inverted dictionary

    # Step 1: Create input file if needed
    create_input_file(input_file)

    # Step 2: Read and process the dictionary
    original_dict = read_dictionary(input_file)
    inverted_dict = invert_dictionary(original_dict)

    # Display results for verification
    print("Original Dictionary:", original_dict)
    print("Inverted Dictionary:", inverted_dict)

    # Step 3: Write the inverted dictionary to a file
    write_dictionary(output_file, inverted_dict)
    print(f"Inverted dictionary has been written to '{output_file}'.")


if __name__ == "__main__":
    main()
