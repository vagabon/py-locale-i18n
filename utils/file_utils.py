import os

# List all files in the directory
def list_files(directory):
    files = os.listdir(directory)
    return files

# Print all files
def print_files(files):
    print("Files in the directory:")
    for file in files:
        print(file)

# Check if a file exist into a directory
def check_file_exists(directory, filename):
    files= list_files(directory)
    print_files(files)
    if filename in files:
        print(f"\nThe file '{filename}' exists in the directory.")
        return True
    else:
        print(f"\nThe file '{filename}' does not exist in the directory.")
        return False

# get the content of a file
def content_file(directory, filename):
    file_path = f"{directory}/{filename}"
    with open(file_path, "r") as file:
        content = file.read()
    return content

# write content into a file
def write_content(directory, filename, suffix, content):
    output_filename = filename.replace(".json", f"{suffix}.json")
    output_file_path = os.path.join(directory, output_filename)

    with open(output_file_path, "w") as output_file:
        output_file.write(content)
    
    print(f"Content written to {output_file_path}")
