import os
import shutil
import sys
import configparser
import logging

# Define the path to the config file and log file at the top
CONFIG_FILE_PATH = r"C:\A\py\Tools\filetype_organizer\config.conf"
LOG_FILE_PATH = r"C:\A\py\Tools\filetype_organizer\organizer.log"

def setup_logging(log_file):
    # Configure the logging settings
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Clear the log file by opening it in write mode
    open(log_file, 'w').close()

def load_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    
    exclude_formats = []
    exclude_folders = []

    if 'exclude' in config:
        if 'formats' in config['exclude']:
            exclude_formats = config['exclude']['formats'].split(',')
            exclude_formats = [fmt.strip().upper() for fmt in exclude_formats]
    
    if 'exclude_folders' in config:
        if 'names' in config['exclude_folders']:
            exclude_folders = config['exclude_folders']['names'].split(',')
            exclude_folders = [name.strip() for name in exclude_folders]
    
    return exclude_formats, exclude_folders

def organize_photos(destination_dir, exclude_formats, exclude_folders, include_formats, recursive, verbose, dry_run):
    for root, dirs, files in os.walk(destination_dir):
        # Avoid processing directories that match any of the excluded folder names
        dirs[:] = [d for d in dirs if d not in exclude_folders and d.upper() not in exclude_formats + include_formats]

        for file in files:
            file_ext = file.split('.')[-1].upper()
            
            # Skip files if the folder they are already in matches their extension
            if os.path.basename(root).upper() == file_ext:
                if verbose:
                    print(f"Skipping file already in the correct folder: {file}")
                logging.info(f"Skipping file already in the correct folder: {file}")
                continue
            
            if exclude_formats and file_ext in exclude_formats:
                if verbose:
                    print(f"Excluding file: {file}")
                logging.info(f"Excluding file: {file}")
                continue

            if include_formats and file_ext not in include_formats:
                if verbose:
                    print(f"Skipping file not in include list: {file}")
                logging.info(f"Skipping file not in include list: {file}")
                continue

            folder_name = os.path.join(root, file_ext)
            
            # Skip creating/moving files into a folder if it matches the file type or if already in correct folder
            if not os.path.exists(folder_name) and os.path.basename(root).upper() != file_ext:
                if verbose:
                    print(f"Creating directory: {folder_name}")
                logging.info(f"Creating directory: {folder_name}")
                if not dry_run:
                    os.makedirs(folder_name)
            
            source_file = os.path.join(root, file)
            destination_file = os.path.join(folder_name, file)
            
            if verbose:
                print(f"Moving file: {source_file} to {destination_file}")
            logging.info(f"Moving file: {source_file} to {destination_file}")
            if not dry_run and not os.path.exists(destination_file):
                shutil.move(source_file, destination_file)

def print_help():
    help_text = """
    Usage: ftorg.bat [options]
    
    Options:
    -path /path      Specify the directory path to organize
    -ex /ex          Exclude specified file types (e.g., -ex jpg png)
    -i /i            Include only specified file types (e.g., -i docx pdf)
    -r /r            Enable or disable recursion (on/off, default is on)
    -v /v            Verbose mode, print detailed output
    -d /d            Dry run, show what would be done without making changes
    -c /c            Specify a custom config file (default is config.conf)
    -h /h -help /help Display this help message
    """
    print(help_text)

def main():
    exclude_formats = []
    exclude_folders = []
    include_formats = []
    destination_dir = None
    recursive = True
    verbose = False
    dry_run = False
    config_file = CONFIG_FILE_PATH
    
    setup_logging(LOG_FILE_PATH)
    
    args = sys.argv[1:]
    
    if not args or '-h' in args or '/h' in args or '-help' in args or '/help' in args:
        print_help()
        return

    for i, arg in enumerate(args):
        if arg in ['-path', '/path']:
            if i + 1 < len(args):
                destination_dir = os.path.normpath(args[i + 1])
            else:
                print("Error: Path not specified after -path or /path.")
                logging.error("Error: Path not specified after -path or /path.")
                return
        elif arg in ['-ex', '/ex']:
            if i + 1 < len(args):
                exclude_formats += [fmt.strip().upper() for fmt in args[i + 1:]]
                break
        elif arg in ['-i', '/i']:
            if i + 1 < len(args):
                include_formats += [fmt.strip().upper() for fmt in args[i + 1:]]
                break
        elif arg in ['-r', '/r']:
            if i + 1 < len(args):
                recursive = args[i + 1].lower() == 'on'
            else:
                print("Error: Recursion setting not specified after -r or /r.")
                logging.error("Error: Recursion setting not specified after -r or /r.")
                return
        elif arg in ['-v', '/v']:
            verbose = True
        elif arg in ['-d', '/d']:
            dry_run = True
        elif arg in ['-c', '/c']:
            if i + 1 < len(args):
                config_file = args[i + 1]
            else:
                print("Error: Config file not specified after -c or /c.")
                logging.error("Error: Config file not specified after -c or /c.")
                return

    exclude_formats_from_config, exclude_folders_from_config = load_config(config_file)
    exclude_formats += exclude_formats_from_config
    exclude_folders += exclude_folders_from_config

    if not destination_dir:
        print("Error: No path specified. Use -path or /path to specify the directory.")
        logging.error("Error: No path specified. Use -path or /path to specify the directory.")
        return
    
    organize_photos(destination_dir, exclude_formats, exclude_folders, include_formats, recursive, verbose, dry_run)
    print("Files organized successfully.")
    logging.info("Files organized successfully.")

if __name__ == "__main__":
    main()
