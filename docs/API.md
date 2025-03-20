# VibeStopwatch API Documentation

## Core Components

### Stopwatch Class
Located in `src/core/stopwatch.py`

The core stopwatch implementation that provides timing functionality.

#### Methods

- `start() -> None`
  - Starts the stopwatch
  - Sets the start time and running state

- `stop() -> None`
  - Stops the stopwatch
  - Calculates and stores the elapsed time

- `reset() -> None`
  - Resets the stopwatch to zero
  - Clears all lap times

- `lap() -> float`
  - Records a lap time
  - Returns the lap duration in seconds

- `get_elapsed_time() -> float`
  - Returns the current elapsed time in seconds

- `get_laps() -> List[float]`
  - Returns a copy of the list of lap times

- `format_time(time_in_seconds: float) -> str`
  - Formats time in seconds to HH:MM:SS.mmm format

## GUI Components

### MainWindow Class
Located in `src/gui/window.py`

The main window implementation for the GUI interface.

#### Features

- Large time display with millisecond precision
- Control buttons:
  - Start: Begins the stopwatch
  - Stop: Pauses the stopwatch
  - Reset: Resets to zero
  - Lap: Records lap times (coming soon)

#### Methods

- `start()`
  - Starts the timer
  - Updates button states

- `stop()`
  - Stops the timer
  - Updates button states

- `reset()`
  - Resets the display to zero
  - Stops the timer

- `lap()`
  - Records lap times (to be implemented)

- `update_time()`
  - Updates the elapsed time
  - Called by the timer

- `update_display()`
  - Updates the time display
  - Formats time in HH:MM:SS.mmm format

## CLI Interface

Located in `src/main.py`

The command-line interface implementation using Click.

### Commands

- `gui`
  - Launches the GUI version of the stopwatch

- `cli`
  - Launches the CLI version of the stopwatch (coming soon)

## Development

### Running Tests
```bash
pytest
```

### Code Style
The project follows PEP 8 guidelines and uses:
- Black for code formatting
- Flake8 for linting
- MyPy for type checking

### Building Executable
```bash
pyinstaller --onefile --windowed src/main.py
```

## Dependencies

### Required
- PyQt6>=6.4.0: GUI framework
- click>=8.1.0: CLI framework
- rich>=13.0.0: Terminal formatting

### Development
- pytest>=7.0.0: Testing framework
- black>=22.0.0: Code formatter
- flake8>=4.0.0: Linter
- mypy>=0.950: Type checker
- pyinstaller>=5.0.0: Executable builder 