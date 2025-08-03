from typing import Set, Tuple


class Grid:
    """
    Represents the rectangular grid of the Martian surface.
    
    The grid has boundaries and tracks positions where robots have fallen off
    (scented positions) to prevent future robots from falling off at the same point.
    """
    
    def __init__(self, max_x: int, max_y: int):
        """
        Initialize the grid with maximum coordinates.
        
        Args:
            max_x: Maximum x-coordinate (upper-right corner)
            max_y: Maximum y-coordinate (upper-right corner)
        """
        self.max_x = max_x
        self.max_y = max_y
        self.scented_positions: Set[Tuple[int, int]] = set()
    
    def is_within_bounds(self, x: int, y: int) -> bool:
        """
        Check if a position is within the grid boundaries.
        
        Args:
            x: X-coordinate to check
            y: Y-coordinate to check
            
        Returns:
            True if the position is within bounds, False otherwise
        """
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y
    
    def would_fall_off(self, x: int, y: int) -> bool:
        """
        Check if a position is outside the grid boundaries.
        
        Args:
            x: X-coordinate to check
            y: Y-coordinate to check
            
        Returns:
            True if the position is outside bounds, False otherwise
        """
        return not self.is_within_bounds(x, y)
    
    def is_position_scented(self, x: int, y: int) -> bool:
        """
        Check if a position has a scent (a robot previously fell off here).
        
        Args:
            x: X-coordinate to check
            y: Y-coordinate to check
            
        Returns:
            True if the position is scented, False otherwise
        """
        return (x, y) in self.scented_positions
    
    def add_scent(self, x: int, y: int) -> None:
        """
        Add a scent to a position (when a robot falls off).
        
        Args:
            x: X-coordinate of the scented position
            y: Y-coordinate of the scented position
        """
        self.scented_positions.add((x, y))
    
    def can_move_to_position(self, x: int, y: int) -> bool:
        """
        Check if a robot can move to a position.
        A robot cannot move to a position that would make it fall off,
        unless that position is scented (in which case the move is ignored).
        
        Args:
            x: X-coordinate to check
            y: Y-coordinate to check
            
        Returns:
            True if the robot can move to this position, False otherwise
        """
        if self.is_within_bounds(x, y):
            return True
        else:
            # If the position is outside bounds, check if it's scented
            return self.is_position_scented(x, y) 