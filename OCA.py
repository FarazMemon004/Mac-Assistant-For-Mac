import subprocess
import shutil
import os

def open_application(app_name):
    subprocess.run(['open', '-a', app_name])

def close_application(app_name):
    subprocess.run(['pkill', app_name])


def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Deleted file: {file_path}")
    except Exception as e:
        print(f"Error deleting file: {e}")

def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Deleted folder: {folder_path}")
    except Exception as e:
        print(f"Error deleting folder: {e}")

def extract_path(command, action_phrase):
    # Example command: "delete this file /Users/username/Desktop/test.txt"
    try:
        # Split the command and get the part after the action phrase
        path = command.split(action_phrase)[1].strip()
        # Validate the path
        if os.path.exists(path):
            return path
        else:
            print(f"Path does not exist: {path}")
            return None
    except IndexError:
        print("Please specify the file or folder path after the command.")
        return None

def open_youtube_in_brave():
    subprocess.run(['open', '-a', 'Brave Browser', 'https://www.youtube.com'])

def delete_selected_file_or_folder():
    try:
        # Use AppleScript to get the path of the selected file or folder in Finder
        script = """
        tell application "Finder"
            set selectedItems to selection
            set filePathList to {}
            repeat with anItem in selectedItems
                set end of filePathList to POSIX path of (anItem as alias)
            end repeat
        end tell
        return filePathList
        """
        # Run the AppleScript command
        file_paths = subprocess.check_output(['osascript', '-e', script])

        # Convert the output to a Python list
        file_paths = file_paths.decode('utf-8').strip().split(", ")

        # Delete the selected files or folders
        for path in file_paths:
            if os.path.isfile(path):
                os.remove(path)
                print(f"File '{path}' deleted.")
            elif os.path.isdir(path):
                os.rmdir(path)
                print(f"Folder '{path}' deleted.")
            else:
                print(f"No such file or folder: '{path}'")
    except Exception as e:
        print(f"Error deleting file or folder: {e}")

def quit_application(app_name):
    try:
        subprocess.run(['osascript', '-e', f'tell application "{app_name}" to quit'])
        print(f"{app_name} has been quit.")
    except Exception as e:
        print(f"Error quitting {app_name}: {e}")

def next_song():
    try:
        subprocess.run(['osascript', '-e', 'tell application "Music" to next track'])
        print("Skipped to the next song.")
    except Exception as e:
        print(f"Error skipping to next song: {e}")

def previous_song():
    try:
        subprocess.run(['osascript', '-e', 'tell application "Music" to previous track'])
        print("Went back to the previous song.")
    except Exception as e:
        print(f"Error going back to previous song: {e}")

def go_back_in_browser():
    try:
        # This works for Safari, Chrome, and Brave
        subprocess.run(['osascript', '-e', 'tell application "System Events" to keystroke "[" using {command down}'])
        print("Went back in the browser.")
    except Exception as e:
        print(f"Error going back in browser: {e}")


def go_back_in_finder():
    try:
        # Activate Finder before going back
        subprocess.run(['osascript', '-e', 'tell application "Finder" to activate'])

        # Use AppleScript to simulate the "Go back" command in Finder
        script = '''
        tell application "Finder"
            try
                back
            on error
                display dialog "No previous folder to go back to." buttons {"OK"}
            end try
        end tell
        '''
        subprocess.run(['osascript', '-e', script])
    except Exception as e:
        print(f"Error going back in Finder: {e}")


# Example usage:
open_application('Safari')
close_application('Safari')
