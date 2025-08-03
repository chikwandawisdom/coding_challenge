import unittest
from src.robot import Robot, Orientation


class TestRobot(unittest.TestCase):
    """Test cases for the Robot class."""
    
    def test_robot_initialization(self):
        """Test robot initialization with valid parameters."""
        robot = Robot(1, 2, 'N')
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 2)
        self.assertEqual(robot.orientation, Orientation.NORTH)
        self.assertFalse(robot.is_lost)
    
    def test_robot_initialization_all_orientations(self):
        """Test robot initialization with all possible orientations."""
        orientations = ['N', 'S', 'E', 'W']
        for orientation in orientations:
            robot = Robot(0, 0, orientation)
            self.assertEqual(robot.orientation.value, orientation)
    
    def test_turn_left(self):
        """Test turning left from all orientations."""
        # Test turning left from North
        robot = Robot(0, 0, 'N')
        robot.turn_left()
        self.assertEqual(robot.orientation, Orientation.WEST)
        
        # Test turning left from West
        robot.turn_left()
        self.assertEqual(robot.orientation, Orientation.SOUTH)
        
        # Test turning left from South
        robot.turn_left()
        self.assertEqual(robot.orientation, Orientation.EAST)
        
        # Test turning left from East
        robot.turn_left()
        self.assertEqual(robot.orientation, Orientation.NORTH)
    
    def test_turn_right(self):
        """Test turning right from all orientations."""
        # Test turning right from North
        robot = Robot(0, 0, 'N')
        robot.turn_right()
        self.assertEqual(robot.orientation, Orientation.EAST)
        
        # Test turning right from East
        robot.turn_right()
        self.assertEqual(robot.orientation, Orientation.SOUTH)
        
        # Test turning right from South
        robot.turn_right()
        self.assertEqual(robot.orientation, Orientation.WEST)
        
        # Test turning right from West
        robot.turn_right()
        self.assertEqual(robot.orientation, Orientation.NORTH)
    
    def test_get_next_position(self):
        """Test getting the next position for all orientations."""
        # Test North
        robot = Robot(1, 1, 'N')
        next_pos = robot.get_next_position()
        self.assertEqual(next_pos, (1, 2))
        
        # Test South
        robot.orientation = Orientation.SOUTH
        next_pos = robot.get_next_position()
        self.assertEqual(next_pos, (1, 0))
        
        # Test East
        robot.orientation = Orientation.EAST
        next_pos = robot.get_next_position()
        self.assertEqual(next_pos, (2, 1))
        
        # Test West
        robot.orientation = Orientation.WEST
        next_pos = robot.get_next_position()
        self.assertEqual(next_pos, (0, 1))
    
    def test_move_forward(self):
        """Test moving forward from all orientations."""
        # Test moving North
        robot = Robot(1, 1, 'N')
        robot.move_forward()
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 2)
        
        # Test moving South
        robot = Robot(1, 1, 'S')
        robot.move_forward()
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 0)
        
        # Test moving East
        robot = Robot(1, 1, 'E')
        robot.move_forward()
        self.assertEqual(robot.x, 2)
        self.assertEqual(robot.y, 1)
        
        # Test moving West
        robot = Robot(1, 1, 'W')
        robot.move_forward()
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 1)
    
    def test_get_position(self):
        """Test getting the current position."""
        robot = Robot(3, 4, 'N')
        position = robot.get_position()
        self.assertEqual(position, (3, 4))
    
    def test_get_orientation(self):
        """Test getting the current orientation."""
        robot = Robot(0, 0, 'E')
        orientation = robot.get_orientation()
        self.assertEqual(orientation, 'E')
    
    def test_mark_as_lost(self):
        """Test marking a robot as lost."""
        robot = Robot(0, 0, 'N')
        self.assertFalse(robot.is_lost)
        robot.mark_as_lost()
        self.assertTrue(robot.is_lost)
    
    def test_string_representation(self):
        """Test string representation of robot states."""
        # Test normal robot
        robot = Robot(2, 3, 'S')
        self.assertEqual(str(robot), "2 3 S")
        
        # Test lost robot
        robot.mark_as_lost()
        self.assertEqual(str(robot), "2 3 S LOST")


if __name__ == '__main__':
    unittest.main() 