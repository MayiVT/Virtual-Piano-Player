# Virtual Piano Player

This is a Python project that simulates a virtual piano player. It reads a sheet music file and plays the corresponding notes on a virtual piano.

## Installation

1. Clone the repository to your local machine.
2. Install the required Python packages using pip:
```
pip install -r requirements.txt
```

## Usage
1. Run the `main.py` file with the following command:
```
python main.py --file <sheet_file_name> --mode <auto/manual> --tempo <tempo_value> --key <key_to_press>
```
- `--file` or `-f`: The name of the sheet music file.
- `--mode` or `-m`: The mode of operation. It can be either `auto` or `manual`.
- `--tempo` or `-t`: The tempo value. It is optional and defaults to 0.5.
- `--key` or `-k`: The key to press. It is optional and defaults to 'delete'.
2. In `auto` mode, press the specified key to start the piano player. In `manual` mode, press the specified key to play the next note.

## Example
```
python main.py --file sheet.txt --mode auto --tempo 0.5 --key delete
```
This command will start the piano player in `auto` mode, reading the notes from the `sheet.txt` file, with a tempo of 0.5, and pressing the 'delete' key to start.

## Note
- The sheet music file should be in a specific format. Each line represents a note, and the notes are separated by spaces. The notes can be either a single character (representing a key on the piano) or a sequence of characters enclosed in square brackets (representing a chord).
- The `auto` mode plays the notes automatically with a specified tempo, while the `manual` mode waits for a key press to play the next note.
- The `tempo` value is the time (in seconds) between playing each note in `auto` mode. A smaller value means a faster tempo.
- The `key` to press is the key that starts the piano player in `auto` mode or plays the next note in `manual` mode.
- In the `auto` mode, you can add dots in the sheet to delay some notes.
