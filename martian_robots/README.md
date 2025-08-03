# Martian Robots Simulator

A Python implementation of the Martian Robots programming challenge. This simulator processes robot instructions on a rectangular grid, handling the unique "scent" mechanism where robots that fall off the grid leave a scent that prevents future robots from falling off at the same position.

## Problem Overview

The surface of Mars is modelled by a rectangular grid around which robots move according to instructions from Earth. The key feature is the scent mechanism: when a robot falls off the grid, it leaves a "scent" at its last valid position, preventing subsequent robots from falling off at that exact point.

### Robot Instructions
- **L**: Turn left 90 degrees (stay in place)
- **R**: Turn right 90 degrees (stay in place)  
- **F**: Move forward one grid point in current direction

### Scent Mechanism
- If a robot falls off the grid, it leaves a scent at its last valid position
- Future robots ignore F commands that would make them fall off from a scented position
- This prevents multiple robots from falling off at the same location

## Implementation Summary

### **Modular Architecture**
The solution is structured into three main classes:

- **`Robot`**: Handles robot state (position, orientation) and movement logic
- **`Grid`**: Manages grid boundaries and the scent mechanism
- **`Simulator`**: Orchestrates the simulation and processes robot instructions

### **Key Design Decisions**

#### **Orientation Management**
- Used Python's `Enum` class for type-safe orientation handling
- Clear mapping: N=North, S=South, E=East, W=West
- Simple turn logic with explicit state transitions

#### **Scent Mechanism**
- Implemented using a `Set` of position tuples for O(1) lookup
- Scent is added when a robot falls off the grid
- Future robots ignore F commands that would make them fall off from scented positions

### **Testing Strategy**
- **25 comprehensive unit tests** covering all components
- **Edge case testing**: boundaries, scent mechanism, invalid inputs
- **Integration testing**: multiple robots, sequential processing
- **Sample data verification**: confirms correct behavior

## Verification Results

### **Sample Data Processing**
```
Input:
5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL

Output:
1 1 E
3 3 N LOST
2 3 S
```

### **Test Results**
- All 25 unit tests pass

## Installation and Setup

### Prerequisites
- Python 3.7 or higher

### Running the Program

1. **Clone or download the project**
2. **Navigate to the project directory**
   ```bash
   cd martian_robots
   ```

3. **Run the program with input from stdin**
   ```bash
   python3 main.py < sample_input.txt
   ```

4. **Or pipe input directly**
   ```bash
   echo "5 3
   1 1 E
   RFRFRFRF
   3 2 N
   FRRFLLFFRRFLL" | python3 main.py
   ```

## Input Format

The input consists of:
- **First line**: Upper-right coordinates of the rectangular world (e.g., "5 3")
- **Remaining lines**: Pairs of lines per robot:
  - Robot position: "x y orientation" (e.g., "1 1 E")
  - Instructions: String of L, R, F commands (e.g., "RFRFRFRF")

### Example Input
```
5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL
```

## Output Format

For each robot, output its final position and orientation. If a robot falls off the grid, append "LOST".

### Example Output
```
1 1 E
3 3 N LOST
2 3 S
```

## Running Tests

The project includes comprehensive unit tests for all components:

```bash
# Run all tests
python3 -m unittest discover tests -v

# Run specific test files
python3 -m unittest tests.test_robot
python3 -m unittest tests.test_grid
python3 -m unittest tests.test_simulator
```

## Design Decisions

### 1. **Modular Architecture**
- **Robot class**: Encapsulates robot state and movement logic
- **Grid class**: Manages boundaries and scent tracking
- **Simulator class**: Orchestrates the simulation and handles the scent mechanism
- **Main module**: Handles I/O and program entry point


### 2. **Enum for Orientations**
Used Python's `Enum` class for robot orientations (N, S, E, W) to ensure type safety and prevent invalid orientation values.

### 3. **Set for Scent Storage**
Chose a `Set` of tuples to store scented positions for O(1) lookup performance and automatic deduplication.

### 4. **Extensive Unit Testing**
- 100% test coverage of core logic
- Edge case testing (boundaries, scent mechanism)
- Clear test names and documentation

## Technical Choices

### **Language: Python**
- **Readability**: Python's syntax is clear and self-documenting
- **Testing**: Excellent built-in unittest framework
- **Cross-platform**: Works on all major operating systems
- **No external dependencies**: Uses only Python standard library

### **Data Structures**
- **Tuples for positions**: Immutable and hashable for set storage
- **Set for scents**: Efficient O(1) lookup and automatic deduplication

## Key Features Implemented

1. **Robot Movement**: L, R, F instructions working correctly
2. **Grid Boundaries**: Proper boundary detection and handling
3. **Scent Mechanism**: Prevents robots from falling off at scented positions
4. **Sequential Processing**: Robots processed one at a time
5. **Error Handling**: Graceful handling of invalid input
6. **Comprehensive Testing**: Full test coverage
7. **Documentation**: Clear README and inline documentation

