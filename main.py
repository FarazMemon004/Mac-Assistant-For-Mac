from OCA import close_application, open_application
from mediacontrol import play_pause_itunes
from speechrec import listen_for_command



def main():
   while True:
       command = listen_for_command()
       if command:
           if 'open safari' in command:
               open_application('Safari')
           elif 'close safari' in command:
               close_application('Safari')
           elif 'play music' in command:
               play_pause_itunes()
           elif 'stop listening' in command:
               print("Stopping the assistant.")
               break

if __name__ == "__main__":
   main()
