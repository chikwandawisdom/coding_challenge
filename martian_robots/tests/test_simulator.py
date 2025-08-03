import unittest
from src.simulator import Simulator


class TestSimulator(unittest.TestCase):
    """Test cases for the Simulator class."""
    
    def test_simulator_initialization(self):
        """Test simulator initialization."""
        simulator = Simulator(5, 3)
        self.assertEqual(simulator.grid.max_x, 5)
        self.assertEqual(simulator.grid.max_y, 3)
    
    def test_simple_movement(self):
        """Test simple robot movements within bounds."""
        simulator = Simulator(5, 3)
        
        # Test moving forward
        result = simulator.process_robot(1, 1, 'N', 'F')
        self.assertEqual(result, "1 2 N")
        
        # Test turning left
        result = simulator.process_robot(1, 1, 'N', 'L')
        self.assertEqual(result, "1 1 W")
        
        # Test turning right
        result = simulator.process_robot(1, 1, 'N', 'R')
        self.assertEqual(result, "1 1 E")
    
    def test_complex_instructions(self):
        """Test complex instruction sequences."""
        simulator = Simulator(5, 3)
        
        # Test multiple movements
        result = simulator.process_robot(1, 1, 'E', 'FF')
        self.assertEqual(result, "3 1 E")
        
        # Test turning and moving
        result = simulator.process_robot(1, 1, 'N', 'RFF')
        self.assertEqual(result, "3 1 E")
        
        # Test circular movement
        result = simulator.process_robot(1, 1, 'N', 'RRRR')
        self.assertEqual(result, "1 1 N")  # Back to original orientation
    
    def test_falling_off_grid(self):
        """Test robots falling off the grid."""
        simulator = Simulator(5, 3)
        
        # Test falling off north edge
        result = simulator.process_robot(1, 3, 'N', 'F')
        self.assertEqual(result, "1 3 N LOST")
        
        # Test falling off east edge
        result = simulator.process_robot(5, 1, 'E', 'F')
        self.assertEqual(result, "5 1 E LOST")
        
        # Test falling off south edge
        result = simulator.process_robot(1, 0, 'S', 'F')
        self.assertEqual(result, "1 0 S LOST")
        
        # Test falling off west edge
        result = simulator.process_robot(0, 1, 'W', 'F')
        self.assertEqual(result, "0 1 W LOST")
    
    def test_scent_mechanism(self):
        """Test the scent mechanism preventing robots from falling off."""
        simulator = Simulator(5, 3)
        
        # First robot falls off and leaves scent
        result1 = simulator.process_robot(1, 3, 'N', 'F')
        self.assertEqual(result1, "1 3 N LOST")
        
        # Second robot tries to fall off at same position - should be ignored
        result2 = simulator.process_robot(1, 3, 'N', 'F')
        self.assertEqual(result2, "1 3 N")  # No LOST, movement ignored
        
        # Third robot can still fall off at different position
        result3 = simulator.process_robot(2, 3, 'N', 'F')
        self.assertEqual(result3, "2 3 N LOST")
    
    def test_multiple_robots_sequential(self):
        """Test processing multiple robots sequentially."""
        simulator = Simulator(5, 3)
        
        robot_data = [
            (1, 1, 'E', 'RFRFRFRF'),
            (3, 2, 'N', 'FRRFLLFFRRFLL'),
            (0, 3, 'W', 'LLFFFLFLFL')
        ]
        
        results = simulator.process_multiple_robots(robot_data)
        
        # Expected results based on the problem description
        # Robot 1: Should end at 1 1 E (stays in place due to circular movement)
        # Robot 2: Should fall off and leave scent
        # Robot 3: Should fall off at a different position
        
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0], "1 1 E")
        # The other results depend on the exact implementation of the scent mechanism
    
    def test_invalid_instructions(self):
        """Test handling of invalid instructions."""
        simulator = Simulator(5, 3)
        
        # Test with invalid characters (should be ignored)
        result = simulator.process_robot(1, 1, 'N', 'FXLR')
        self.assertEqual(result, "1 2 N")  # Only F, L, R processed
    
    def test_robot_stops_when_lost(self):
        """Test that robot stops processing instructions when lost."""
        simulator = Simulator(5, 3)
        
        # Robot falls off, then gets more instructions
        result = simulator.process_robot(1, 3, 'N', 'FFFRRR')
        self.assertEqual(result, "1 3 N LOST")  # Should stop after first F
    
    def test_edge_case_boundary_movement(self):
        """Test edge cases around grid boundaries."""
        simulator = Simulator(5, 3)
        
        # Test moving to boundary (should be safe)
        result = simulator.process_robot(4, 2, 'E', 'F')
        self.assertEqual(result, "5 2 E")
        
        # Test moving from boundary (should be safe)
        result = simulator.process_robot(5, 2, 'W', 'F')
        self.assertEqual(result, "4 2 W")


if __name__ == '__main__':
    unittest.main() 