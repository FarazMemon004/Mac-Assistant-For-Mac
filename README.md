AI Assistant for macOS 

Overview

AI Assistant for macOS is a Python-based desktop assistant designed to help users interact with their Mac using voice commands. The project aims to simplify everyday tasks through speech recognition, application control, file management, and media playback controls.

Features

- Voice activation using a custom wake phrase
- Speech recognition using OpenAI Whisper
- Open and manage applications
- File and folder operations
- Media playback controls
- Keyboard and mouse automation
- Spoken or audio feedback, depending on configuration

Technologies Used

- Python
- OpenAI Whisper
- SpeechRecognition
- SoundDevice
- NumPy
- PyObjC
- PyAutoGUI

Requirements

- macOS
- Python 3.10 or another version compatible with your dependencies
- Microphone
- Internet connection for downloading Whisper models and installing dependencies
- Required macOS privacy permissions

Installation

1. Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_REPOSITORY_NAME

Replace the placeholders with your actual GitHub repository URL and name.

2. Create a Virtual Environment

python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies

Make sure "requirements.txt" is present in the project directory.

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

If your project uses additional system-level audio dependencies, install those according to the requirements of your chosen audio library.

Configuration

Before running the assistant:

1. Review the configuration files in the project.
2. Set the wake phrase and other preferences as supported by your implementation.
3. Verify that the microphone and audio devices are available.
4. Configure any required environment variables without committing secrets to GitHub.

How to Run

1. Activate the Virtual Environment

source .venv/bin/activate

2. Start the Assistant

Run the Python entry-point file used by your project. For example, if your main file is "main.py":

python main.py

If your entry-point file has a different name, replace "main.py" with that filename.

3. Use Voice Commands

1. Start the assistant.
2. Say the configured wake phrase.
3. Wait for the wake confirmation, if enabled.
4. Speak a supported command.
5. Follow the assistant's audio or on-screen feedback.

macOS Permissions

Depending on the implemented features, you may need to enable:

- Microphone: System Settings → Privacy & Security → Microphone
- Accessibility: System Settings → Privacy & Security → Accessibility
- Automation: System Settings → Privacy & Security → Automation

Only grant permissions required by the features you use.

Troubleshooting

Microphone Not Working

- Check microphone permissions.
- Verify that the correct input device is selected.
- Confirm that the required audio dependencies are installed.

Whisper Model Loading Error

Install OpenAI Whisper in the active environment:

python -m pip install openai-whisper

Ensure your code imports the correct package and that the required model can be downloaded.

Command Not Recognized

- Speak clearly after the wake phrase.
- Check microphone input levels.
- Verify that the configured speech-recognition model supports your usage requirements.

Application Control Not Working

Check macOS Accessibility and Automation permissions, and verify that the requested application or file path exists.

Security and Privacy

- Do not commit API keys, passwords, or private credentials.
- Do not store microphone recordings unless explicitly required.
- Review permissions before enabling system-level automation.
- Use caution when executing file deletion or other destructive commands.

Project Structure

Mac-AI-Assistant/
├── requirements.txt
├── README.md
├── .gitignore
└── src/                 # Optional supporting modules

The structure above is an example. Update it to match your actual files.

License

Add a license if you intend to allow others to use, modify, or distribute your project.
