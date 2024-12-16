def read_and_write_files():
    # Ask the user for the input filename
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Attempt to open and read the file
        with open(input_filename, "r") as input_file:
            content = input_file.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, "w") as output_file:
            output_file.write(modified_content)

        print(f"File has been successfully modified and saved as '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
read_and_write_files()
