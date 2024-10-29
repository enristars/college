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
