import os

def rename_files(folder_path):
    try:
        files = os.listdir(folder_path)
        existing_files = set(files)  # Track existing files to avoid conflicts
        numbered_files = {}
        max_number = 0

        # Extract numbers from filenames and track the highest number
        for filename in files:
            name, extension = os.path.splitext(filename)
            if name.isdigit():
                number = int(name)
                numbered_files[number] = filename
                if number > max_number:
                    max_number = number

        print(f"Numbered files found: {numbered_files}")
        print(f"Max number found: {max_number}")

        # Determine the starting counter
        # if 1 in numbered_files:
            # start_number = int(input(f"A file named '1' exists. Enter the starting number: "))
        #else:
        
        start_number = max_number + 1

        counter = start_number
        print(f"Starting renaming from number: {counter}")

        for filename in files:
            name, extension = os.path.splitext(filename)
            if name.isdigit() and int(name) < start_number:
                print(f"Skipping '{filename}' because it is already correctly numbered.")
                continue  # Skip files that are already in the correct order and below start_number
            
            # Skip files that are already correctly numbered in the new sequence
            if name.isdigit() and int(name) >= start_number and int(name) <= max_number:
                print(f"Skipping '{filename}' because it is already correctly numbered in the new sequence.")
                continue

            new_name = f"{counter}{extension}"
            
            # Find the next available name if the new name already exists
            while new_name in existing_files:
                counter += 1
                new_name = f"{counter}{extension}"
            
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_name)
            
            print(f"Renaming '{old_file}' to '{new_file}'")
            os.rename(old_file, new_file)
            existing_files.add(new_name)  # Update the set of existing files
            
            counter += 1  # Increment the counter for the next file

        print("Renaming completed.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
folder_path = input("Enter the path to the folder: ")
rename_files(folder_path)
