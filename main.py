import os
import csv

def list_files_in_directory(directory_path: str) -> list:
    try:
        # List all files and directories in the specified path
        files_and_dirs = os.listdir(directory_path)
        
        # Filter and return only the files with their absolute paths
        full_paths = [os.path.abspath(os.path.join(directory_path, f)) for f in files_and_dirs if os.path.isfile(os.path.join(directory_path, f))]
        return full_paths
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def create_books_csv(file_paths: list, output_csv: str = "books.csv"):
    # Define the column headers
    headers = ['title', 'description', 'author', 'source', 'source_url']
    
    # Open (or create) the CSV file for writing
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        
        # Write the header row
        writer.writeheader()
        
        # Write rows for each file path, leaving other fields empty
        for file_path in file_paths:
            writer.writerow({
                'title': '',
                'description': '',
                'author': '',
                'source': file_path,  # Add file path to 'source' column
                'source_url': ''
            })

    print(f"CSV file '{output_csv}' created successfully with file paths.")


if __name__ == "__main__":
    directory = "./data"
    print("[INFO] Reading files from directory:", directory)
    files = list_files_in_directory(directory)
    print(f"[INFO] Loaded {len(files)} files.")
    print("[INFO] Creating CSV file with file paths...")
    create_books_csv(files)
    print("[INFO] Done!")