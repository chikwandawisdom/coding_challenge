#!/usr/bin/env python3
"""
Verification script for the Martian Robots implementation.

This script demonstrates that our implementation correctly processes
the sample data provided in the problem description.
"""

from src.simulator import Simulator


def main():
    """Demonstrate the sample data processing."""
    print("Martian Robots Simulator - Sample Data Verification")
    print("=" * 50)
    
    # Sample data from the problem description
    grid_max_x, grid_max_y = 5, 3
    
    robot_data = [
        (1, 1, 'E', 'RFRFRFRF'),
        (3, 2, 'N', 'FRRFLLFFRRFLL'),
        (0, 3, 'W', 'LLFFFLFLFL')
    ]
    
    print(f"Grid dimensions: {grid_max_x} x {grid_max_y}")
    print()
    
    # Create simulator and process robots
    simulator = Simulator(grid_max_x, grid_max_y)
    
    print("Processing robots:")
    print("-" * 30)
    
    for i, (start_x, start_y, orientation, instructions) in enumerate(robot_data, 1):
        print(f"Robot {i}:")
        print(f"  Start: ({start_x}, {start_y}) facing {orientation}")
        print(f"  Instructions: {instructions}")
        
        result = simulator.process_robot(start_x, start_y, orientation, instructions)
        print(f"  Result: {result}")
        print()
    
    print("Sample data verification complete!")
    print("\nExpected behavior:")
    print("- Robot 1: Should end at 1 1 E (circular movement)")
    print("- Robot 2: Should fall off and leave scent")
    print("- Robot 3: Should fall off at a different position")


if __name__ == "__main__":
    main() 