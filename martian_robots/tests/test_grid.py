import unittest
from src.grid import Grid


class TestGrid(unittest.TestCase):
    """Test cases for the Grid class."""
    
    def test_grid_initialization(self):
        """Test grid initialization with valid dimensions."""
        grid = Grid(5, 3)
        self.assertEqual(grid.max_x, 5)
        self.assertEqual(grid.max_y, 3)
        self.assertEqual(len(grid.scented_positions), 0)
    
    def test_is_within_bounds(self):
        """Test boundary checking for various positions."""
        grid = Grid(5, 3)
        
        # Test positions within bounds
        self.assertTrue(grid.is_within_bounds(0, 0))
        self.assertTrue(grid.is_within_bounds(5, 3))
        self.assertTrue(grid.is_within_bounds(2, 1))
        
        # Test positions outside bounds
        self.assertFalse(grid.is_within_bounds(-1, 0))
        self.assertFalse(grid.is_within_bounds(0, -1))
        self.assertFalse(grid.is_within_bounds(6, 3))
        self.assertFalse(grid.is_within_bounds(5, 4))
    
    def test_would_fall_off(self):
        """Test fall-off detection for various positions."""
        grid = Grid(5, 3)
        
        # Test positions that would cause fall-off
        self.assertTrue(grid.would_fall_off(-1, 0))
        self.assertTrue(grid.would_fall_off(0, -1))
        self.assertTrue(grid.would_fall_off(6, 3))
        self.assertTrue(grid.would_fall_off(5, 4))
        
        # Test positions that are safe
        self.assertFalse(grid.would_fall_off(0, 0))
        self.assertFalse(grid.would_fall_off(5, 3))
        self.assertFalse(grid.would_fall_off(2, 1))
    
    def test_scent_management(self):
        """Test adding and checking scented positions."""
        grid = Grid(5, 3)
        
        # Initially no scented positions
        self.assertFalse(grid.is_position_scented(1, 1))
        
        # Add a scent
        grid.add_scent(1, 1)
        self.assertTrue(grid.is_position_scented(1, 1))
        
        # Add another scent
        grid.add_scent(3, 2)
        self.assertTrue(grid.is_position_scented(3, 2))
        self.assertTrue(grid.is_position_scented(1, 1))  # Still scented
        
        # Check non-scented position
        self.assertFalse(grid.is_position_scented(2, 2))
    
    def test_can_move_to_position(self):
        """Test movement permission logic."""
        grid = Grid(5, 3)
        
        # Can move to positions within bounds
        self.assertTrue(grid.can_move_to_position(0, 0))
        self.assertTrue(grid.can_move_to_position(5, 3))
        self.assertTrue(grid.can_move_to_position(2, 1))
        
        # Cannot move to positions outside bounds (unless scented)
        self.assertFalse(grid.can_move_to_position(-1, 0))
        self.assertFalse(grid.can_move_to_position(6, 3))
        
        # Add scent to an out-of-bounds position
        grid.add_scent(-1, 0)
        self.assertTrue(grid.can_move_to_position(-1, 0))  # Now can move there
        
        # Other out-of-bounds positions still not allowed
        self.assertFalse(grid.can_move_to_position(6, 3))
    
    def test_multiple_scents(self):
        """Test handling multiple scented positions."""
        grid = Grid(5, 3)
        
        # Add multiple scents
        scented_positions = [(1, 1), (3, 2), (-1, 0), (6, 3)]
        for pos in scented_positions:
            grid.add_scent(*pos)
        
        # Check all are scented
        for pos in scented_positions:
            self.assertTrue(grid.is_position_scented(*pos))
        
        # Check non-scented positions
        non_scented = [(0, 0), (2, 2), (4, 1)]
        for pos in non_scented:
            self.assertFalse(grid.is_position_scented(*pos))


if __name__ == '__main__':
    unittest.main() 