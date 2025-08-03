from enum import Enum
from typing import Tuple


class Orientation(Enum):
    """Enumeration for robot orientations."""
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'


class Robot:
    """
    Represents a robot on the Martian surface.
    
    A robot has a position (x, y coordinates) and an orientation (N, S, E, W).
    The robot can move forward, turn left, or turn right.
    """
    
    def __init__(self, x: int, y: int, orientation: str):
        """
        Initialize a robot with position and orientation.
        
        Args:
            x: X-coordinate of the robot
            y: Y-coordinate of the robot
            orientation: Initial orientation ('N', 'S', 'E', 'W')
        """
        self.x = x
        self.y = y
        self.orientation = Orientation(orientation)
        self.is_lost = False
    
    def turn_left(self) -> None:
        """Turn the robot 90 degrees to the left."""
        if self.orientation == Orientation.NORTH:
            self.orientation = Orientation.WEST
        elif self.orientation == Orientation.WEST:
            self.orientation = Orientation.SOUTH
        elif self.orientation == Orientation.SOUTH:
            self.orientation = Orientation.EAST
        elif self.orientation == Orientation.EAST:
            self.orientation = Orientation.NORTH
    
    def turn_right(self) -> None:
        """Turn the robot 90 degrees to the right."""
        if self.orientation == Orientation.NORTH:
            self.orientation = Orientation.EAST
        elif self.orientation == Orientation.EAST:
            self.orientation = Orientation.SOUTH
        elif self.orientation == Orientation.SOUTH:
            self.orientation = Orientation.WEST
        elif self.orientation == Orientation.WEST:
            self.orientation = Orientation.NORTH
    
    def get_next_position(self) -> Tuple[int, int]:
        """
        Get the position the robot would move to if it goes forward.
        
        Returns:
            Tuple of (x, y) coordinates for the next position
        """
        if self.orientation == Orientation.NORTH:
            return (self.x, self.y + 1)
        elif self.orientation == Orientation.SOUTH:
            return (self.x, self.y - 1)
        elif self.orientation == Orientation.EAST:
            return (self.x + 1, self.y)
        elif self.orientation == Orientation.WEST:
            return (self.x - 1, self.y)
    
    def move_forward(self) -> None:
        """Move the robot forward one grid point in the current direction."""
        next_x, next_y = self.get_next_position()
        self.x = next_x
        self.y = next_y
    
    def get_position(self) -> Tuple[int, int]:
        """Get the current position of the robot."""
        return (self.x, self.y)
    
    def get_orientation(self) -> str:
        """Get the current orientation of the robot."""
        return self.orientation.value
    
    def mark_as_lost(self) -> None:
        """Mark the robot as lost (fell off the grid)."""
        self.is_lost = True
    
    def __str__(self) -> str:
        """String representation of the robot's current state."""
        status = f"{self.x} {self.y} {self.orientation.value}"
        if self.is_lost:
            status += " LOST"
        return status 