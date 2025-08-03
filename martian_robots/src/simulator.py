from typing import List, Tuple
from .robot import Robot
from .grid import Grid


class Simulator:
    """
    Simulates robots moving on the Martian surface.
    
    The simulator processes robot instructions sequentially and handles
    the scent mechanism to prevent robots from falling off at previously
    scented positions.
    """
    
    def __init__(self, max_x: int, max_y: int):
        """
        Initialize the simulator with grid dimensions.
        
        Args:
            max_x: Maximum x-coordinate of the grid
            max_y: Maximum y-coordinate of the grid
        """
        self.grid = Grid(max_x, max_y)
    
    def process_robot(self, start_x: int, start_y: int, orientation: str, instructions: str) -> str:
        """
        Process a single robot's instructions and return the final state.
        
        Args:
            start_x: Starting x-coordinate of the robot
            start_y: Starting y-coordinate of the robot
            orientation: Starting orientation ('N', 'S', 'E', 'W')
            instructions: String of instructions ('L', 'R', 'F')
            
        Returns:
            String representation of the robot's final state
        """
        robot = Robot(start_x, start_y, orientation)
        
        for instruction in instructions:
            if robot.is_lost:
                break
                
            if instruction == 'L':
                robot.turn_left()
            elif instruction == 'R':
                robot.turn_right()
            elif instruction == 'F':
                self._process_forward_movement(robot)
            # Ignore invalid instructions
        
        return str(robot)
    
    def _process_forward_movement(self, robot: Robot) -> None:
        """
        Process a forward movement instruction for a robot.
        
        This method handles the scent mechanism: if a robot would fall off
        the grid, it checks if the position is scented. If not scented,
        the robot falls off and leaves a scent. If scented, the movement
        is ignored.
        
        Args:
            robot: The robot to move forward
        """
        next_x, next_y = robot.get_next_position()
        
        if self.grid.would_fall_off(next_x, next_y):
            # Robot would fall off - check if position is scented
            if self.grid.is_position_scented(next_x, next_y):
                # Position is scented, ignore the movement
                return
            else:
                # Position is not scented, robot falls off and leaves scent
                robot.mark_as_lost()
                self.grid.add_scent(next_x, next_y)
        else:
            # Safe to move
            robot.move_forward()
    
    def process_multiple_robots(self, robot_data: List[Tuple[int, int, str, str]]) -> List[str]:
        """
        Process multiple robots sequentially.
        
        Args:
            robot_data: List of tuples (start_x, start_y, orientation, instructions)
            
        Returns:
            List of final states for each robot
        """
        results = []
        for start_x, start_y, orientation, instructions in robot_data:
            result = self.process_robot(start_x, start_y, orientation, instructions)
            results.append(result)
        return results 