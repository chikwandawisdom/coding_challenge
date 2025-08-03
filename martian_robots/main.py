#!/usr/bin/env python3
"""
Martian Robots Simulator

This program simulates robots moving on the surface of Mars according to
instructions provided from Earth. The simulation handles the scent mechanism
where robots that fall off the grid leave a scent that prevents future
robots from falling off at the same position.
"""

import sys
from src.simulator import Simulator


def parse_input(input_lines):
    """
    Parse input lines into grid dimensions and robot data.
    
    Args:
        input_lines: List of input strings
        
    Returns:
        Tuple of (max_x, max_y, robot_data_list)
    """
    if not input_lines:
        raise ValueError("No input provided")
    
    # Parse grid dimensions from first line
    try:
        max_x, max_y = map(int, input_lines[0].strip().split())
    except ValueError:
        raise ValueError("Invalid grid dimensions format")
    
    robot_data = []
    i = 1
    
    while i < len(input_lines):
        if i + 1 >= len(input_lines):
            raise ValueError("Incomplete robot data")
        
        # Parse robot position and orientation
        try:
            x, y, orientation = input_lines[i].strip().split()
            x, y = int(x), int(y)
        except ValueError:
            raise ValueError(f"Invalid robot position format at line {i + 1}")
        
        # Get instructions
        instructions = input_lines[i + 1].strip()
        
        robot_data.append((x, y, orientation, instructions))
        i += 2
    
    return max_x, max_y, robot_data


def main():
    """Main function to run the Martian Robots simulation."""
    try:
        # Read input from stdin
        input_lines = sys.stdin.readlines()
        
        # Parse input
        max_x, max_y, robot_data = parse_input(input_lines)
        
        # Create simulator and process robots
        simulator = Simulator(max_x, max_y)
        results = simulator.process_multiple_robots(robot_data)
        
        # Output results
        for result in results:
            print(result)
            
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main() 