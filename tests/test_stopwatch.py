import pytest
import time
from src.core.stopwatch import Stopwatch

def test_stopwatch_initialization():
    stopwatch = Stopwatch()
    assert not stopwatch.is_running
    assert stopwatch.elapsed_time == 0
    assert len(stopwatch.laps) == 0

def test_stopwatch_start_stop():
    stopwatch = Stopwatch()
    
    # Start the stopwatch
    stopwatch.start()
    assert stopwatch.is_running
    
    # Wait a bit
    time.sleep(0.1)
    
    # Stop the stopwatch
    stopwatch.stop()
    assert not stopwatch.is_running
    assert stopwatch.elapsed_time > 0

def test_stopwatch_reset():
    stopwatch = Stopwatch()
    
    # Start and wait
    stopwatch.start()
    time.sleep(0.1)
    stopwatch.stop()
    
    # Reset
    stopwatch.reset()
    assert not stopwatch.is_running
    assert stopwatch.elapsed_time == 0
    assert len(stopwatch.laps) == 0

def test_stopwatch_lap():
    stopwatch = Stopwatch()
    
    # Start and record a lap
    stopwatch.start()
    time.sleep(0.1)
    lap_time = stopwatch.lap()
    
    assert lap_time > 0
    assert len(stopwatch.laps) == 1
    assert stopwatch.laps[0] == lap_time

def test_time_formatting():
    stopwatch = Stopwatch()
    
    # Test with 1 hour, 2 minutes, 3 seconds, and 456 milliseconds
    time_str = stopwatch.format_time(3723.456)
    assert time_str == "01:02:03.456" 