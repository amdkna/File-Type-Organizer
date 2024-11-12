
# File Type Organizer

**Author**: Arash Naderian (amdkna)

## Overview

File Type Organizer is a Python-based command-line tool designed to help users organize files in a directory by moving them into folders based on their file types. This tool can be customized to include or exclude specific file types, avoid certain folders, and enable or disable recursive directory scanning. It's highly configurable and supports "dry run" mode for safe testing before making changes.

## Features

- Organizes files into folders based on file type (extension).
- Supports excluding specific file types and folders.
- Option to include only specified file types.
- Recursive directory traversal (optional).
- Verbose mode for detailed output.
- Dry run mode to preview actions without making changes.
- Configurable through a `.conf` file for custom settings.
- Logs actions to a log file for reference and debugging.

## Installation

1. Ensure Python 3 is installed on your system.
2. Clone or download the repository.
3. Update `config.conf` if custom configurations are needed.

## Configuration

The configuration file `config.conf` can be used to set default values for excluded file types and folders. It should be located at `C:\A\py\Tools\filetype_organizer\config.conf`. 

### Sample `config.conf`

```ini
[exclude]
formats = jpg, png, gif  # List of file formats to exclude

[exclude_folders]
names = Temp, Backup  # List of folders to exclude
```

## Usage

Run the program using the following command:
```sh
python ftorg.bat [options]
```

### Options

- `-path /path` : Specify the directory to organize.
- `-ex /ex` : Exclude specified file types (e.g., `-ex jpg png`).
- `-i /i` : Include only specified file types (e.g., `-i docx pdf`).
- `-r /r` : Enable or disable recursion (on/off, default is on).
- `-v /v` : Enable verbose mode for detailed output.
- `-d /d` : Dry run mode to preview actions without making changes.
- `-c /c` : Specify a custom configuration file (default is `config.conf`).
- `-h /h` or `-help /help` : Display help message.

### Example Commands

Organize files in `C:\MyPhotos` with verbose mode enabled:
```sh
python ftorg.bat -path C:\MyPhotos -v
```

Organize files in `C:\Documents` excluding `pdf` and `docx` formats, dry run mode enabled:
```sh
python ftorg.bat -path C:\Documents -ex pdf docx -d
```

## Logs

All actions are logged to `C:\A\py\Tools\filetype_organizer\organizer.log`. The log file is cleared each time the program runs.

## Requirements

- Python 3
- ConfigParser (comes with Python's standard library)

## Troubleshooting

If you encounter issues, refer to the log file at `C:\A\py\Tools\filetype_organizer\organizer.log` for detailed information on actions and errors.

## License

This project is open source and available under the MIT License.

