# Particle Attraction Simulation

## Description
This project is a real-time simulation of particles interacting through attraction 
and repulsion forces. 

Each particle moves within a grid and is influenced by specific parameters, 
including attraction size, repulsion strength, and a global force factor.

## Features
- Real-time simulation of particle interactions.
- Customizable attraction and repulsion laws.
- Graphical interface powered by Pygame.
- Performance monitoring with time and frequency analysis.

## Installation
1. Clone the repository or download the project files.
2. Ensure Python is installed (recommended version: 3.12+).
3. Install dependencies using the following command:
   ```bash
   pip install -r requirements.txt
   ```
   
## Usage
To run the simulation, execute the main script:

   ```bash
    python main.py
   ```
## Project Structure

### Main Components
- **`main.py`**: Entry point of the simulation. Initializes the game, configures parameters, and starts the GUI.

### Core Library (`particle_attraction_lib/`)
- **`board.py`**: Defines the game board where particles interact.
- **`vector.py`**: Provides vector arithmetic for particle movement.
- **`particle_repository.py`**: Manages collections of particles.
- **`game.py`**: Main logic for updating the simulation state.
- **`tmp_gui.py`**: Implements the graphical interface using Pygame.
- **`attraction_force.py`**: Models the forces between particles.
- **`attraction_law.py`**: Defines rules for attraction and repulsion.
- **`distance.py`**: Calculates distances between particles.
- **`particle.py`**: Represents individual particles and their properties.
- **`mover.py`**: Handles particle movement logic.

### Tests (`tests/`)
Unit tests for various modules.

### Additional Files
- **`requirements.txt`**: Lists required Python libraries for the project.

## License
This project is licensed under GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007.
