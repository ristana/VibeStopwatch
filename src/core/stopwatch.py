from time import time
from typing import List, Optional

class Stopwatch:
    def __init__(self):
        self.start_time: Optional[float] = None
        self.elapsed_time: float = 0
        self.is_running: bool = False
        self.laps: List[float] = []
    
    def start(self) -> None:
        """Start the stopwatch."""
        if not self.is_running:
            self.start_time = time() - self.elapsed_time
            self.is_running = True
    
    def stop(self) -> None:
        """Stop the stopwatch."""
        if self.is_running:
            self.elapsed_time = time() - self.start_time
            self.is_running = False
    
    def reset(self) -> None:
        """Reset the stopwatch to zero."""
        self.stop()
        self.elapsed_time = 0
        self.laps.clear()
    
    def lap(self) -> float:
        """Record a lap time."""
        if not self.is_running:
            return 0.0
        
        current_time = time() - self.start_time
        lap_time = current_time - self.elapsed_time
        self.elapsed_time = current_time
        self.laps.append(lap_time)
        return lap_time
    
    def get_elapsed_time(self) -> float:
        """Get the current elapsed time in seconds."""
        if self.is_running:
            return time() - self.start_time
        return self.elapsed_time
    
    def get_laps(self) -> List[float]:
        """Get the list of lap times."""
        return self.laps.copy()
    
    def format_time(self, time_in_seconds: float) -> str:
        """Format time in seconds to HH:MM:SS.mmm format."""
        hours = int(time_in_seconds // 3600)
        minutes = int((time_in_seconds % 3600) // 60)
        seconds = int(time_in_seconds % 60)
        milliseconds = int((time_in_seconds % 1) * 1000)
        
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}" 