def read_file():
    try:
        # Open the file in read mode
        with open("sample.txt", "r") as file:
            print("File content:")
            for line in file:
                print(line.strip())  # Remove extra spaces and newlines
    except FileNotFoundError:
        print("Error: The file 'sample.txt' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_file()





