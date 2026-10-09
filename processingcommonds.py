from FM import delete_file
from OCA import open_application, close_application, extract_path, delete_folder


def process_command(command):
    if "delete this file" in command:
        # Extract file path from the command
        file_path = extract_path(command, "delete this file")
        if file_path:
            delete_file(file_path)
    elif "delete this folder" in command:
        # Extract folder path from the command
        folder_path = extract_path(command, "delete this folder")
        if folder_path:
            delete_folder(folder_path)
    elif "open" in command:
        app_name = command.replace("open", "").strip()
        open_application(app_name)
    elif "close" in command:
        app_name = command.replace("close", "").strip()
        close_application(app_name)
    else:
        print("Command not recognized.")

