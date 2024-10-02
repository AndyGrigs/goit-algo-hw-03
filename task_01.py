import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Recursively copy and sort files")
    parser.add_argument("source_dir", help="Path to the source directory")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Path to the destination directory")
    return parser.parse_args()

def process_directory(source_dir, dest_dir):
    try:
        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)
            if os.path.isdir(item_path):
                process_directory(item_path, dest_dir)
            elif os.path.isfile(item_path):
                process_file(item_path, dest_dir)

    except Exception as e:
        print(f"Error while processing in {source_dir}: {e}")
        

def process_file(file_path, dest_dir):
    try:
        _, ext = os.path.splitext(file_path)
        ext = ext[1:] if ext.startswith('.') else ext
        if not ext:
            ext = "No extension"
        dest_subdir = os.path.join(dest_dir, ext)
        os.makedirs(dest_subdir, exist_ok=True)
        shutil.copy(file_path, dest_subdir)
    except Exception as e:
        print(f"Error while processing in {file_path}: {e}")

def main():
    args = parse_arguments()
    source_dir = args.source_dir
    dest_dir = args.dest_dir
    # Check that source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist.")
        return
    # Create destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)
    # Start processing
    process_directory(source_dir, dest_dir)

if __name__ == '__main__':
    main()