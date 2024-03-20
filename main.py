import argparse
import keyboard
import time

parser = argparse.ArgumentParser()

parser.add_argument('--file', '-f', type=str, required=True, help='Sheet file name')
parser.add_argument('--mode', '-m', type=str, required=True, help='[auto, manual]')
parser.add_argument('--tempo', '-t', default=0.5, type=float, required=False, help='0.5 is default, bigger is slower and vice versa [auto mode only]')
parser.add_argument('--key', '-k', default='delete', type=str, required=False, help='Key to press (default -> delete)')

args = parser.parse_args()

def get_sheet():
    with open(args.file, 'r') as file:
        sheet = file.read().splitlines()

    sheet = [item for sublist in sheet for item in sublist if item != ' ']
    return sheet

def play_key(i, sheet):
    if sheet[i] == '[':
        j = i + 1
        char = sheet[j]
        while sheet[j] != ']':
            if char.isupper():
                keyboard.press("shift")
                keyboard.press_and_release(f'{sheet[j]}')
                keyboard.release("shift")
            else:
                keyboard.press_and_release(sheet[j])
            print(sheet[j])
            j += 1
        i = j + 1
        return i
    else:
        char = sheet[i]
        if char.isupper():
            keyboard.press("shift")
            keyboard.press_and_release(f'{sheet[i]}')
            keyboard.release("shift")
        else:
            keyboard.press_and_release(sheet[i])
        print(sheet[i])
        i += 1
        return i
        
def main():
    sheet = get_sheet()
    i = 0

    if args.mode == 'auto':
        print(f'Auto mode: Press {args.key} to start')
        keyboard.wait(args.key)

    while i < len(sheet):
        if args.mode == 'manual':
            keyboard.wait(args.key)
        key = play_key(i, sheet)
        i = key
        if args.mode == 'auto':
            time.sleep(args.tempo)
        else:
            time.sleep(0.1)

if __name__ == '__main__':
    main()