# VibeStopwatch

A modern, sleek stopwatch application with a beautiful dark mode interface.

## Features

- Clean, modern dark mode interface
- Millisecond precision timing
- Start, Stop, and Reset functionality
- Responsive and intuitive controls
- Standalone executable for Windows

## Installation

### Option 1: Run from Source

1. Clone the repository:
```bash
git clone https://github.com/ristana/VibeStopwatch.git
cd VibeStopwatch
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Unix/MacOS
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python src/main.py
```

### Option 2: Download Executable

1. Go to the [Releases](https://github.com/ristana/VibeStopwatch/releases) page
2. Download the latest `VibeStopwatch.exe` for Windows
3. Run the executable directly

## Usage

1. Launch the application
2. Click "Start" to begin timing
3. Click "Stop" to pause
4. Click "Reset" to clear the timer
5. The time is displayed in HH:MM:SS.mmm format

## Development

### Project Structure

```
VibeStopwatch/
├── src/
│   ├── main.py           # Application entry point
│   └── gui/
│       ├── window.py     # Main window implementation
│       └── styles.py     # GUI styling and themes
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

### Building the Executable

To build the executable:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name VibeStopwatch src/main.py
```

The executable will be created in the `dist` directory.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 