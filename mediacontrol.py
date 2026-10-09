import subprocess

def play_pause_itunes():
    subprocess.run(['osascript', '-e', 'tell application "Music" to playpause'])

def next_track_itunes():
    subprocess.run(['osascript', '-e', 'tell application "Music" to next track'])

# Example usage:
play_pause_itunes()
next_track_itunes()
