import os
import sys
import keyboard
import time


def copy_to_clipboard(text):
    print("copied to clipboard: " + text)
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


# iterate through file that's just seperated by newline
def get_file(file_name, delim=None):
    if delim is None:
        with open(file_name, 'r') as f:
            return f.read().splitlines()


def begin_queue(queue):
    size = len(queue)
    copy_to_clipboard(queue[0])
    while size > 0:
        # detect when user does ctrl + v
        if keyboard.is_pressed('ctrl+v'):
            copy_to_clipboard(queue.pop(0))
            size -= 1
            time.sleep(.1)
        else:
            continue
        


def main():
    file_name = sys.argv[1]
    # if sys args is 2, then we need to set the delim
    delim = None if len(sys.argv) == 2 else sys.argv[2]
    lines = get_file(file_name, delim)
    begin_queue(lines)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_name> <optional delimiter>")
        sys.exit(1)
    else:
        # check if file exists  
        if os.path.isfile(sys.argv[1]):
            main()
        else:
            print("File does not exist")
            sys.exit(1)
