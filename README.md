# Physics_simulation_tool
# Physics Simulations with Streamlit

This project is a collection of interactive physics simulations built using Streamlit and Plotly. The simulations cover a range of fundamental physics concepts including projectile motion, simple harmonic motion, electric fields and potentials, wave interference, and circular motion with centripetal force. The goal is to provide a visual and interactive way to understand these concepts.

## Features

- **Projectile Motion**: Simulate the trajectory of a projectile with adjustable initial velocity, launch angle, and initial height. Displays time of flight, maximum height, and range.
- **Simple Harmonic Motion**: Visualize the motion of a mass-spring system with adjustable mass, spring constant, and amplitude. Includes displacement vs. time and phase space plots.
- **Electric Field and Potential**: Calculate and display the electric field and potential at a distance from a point charge. Adjustable charge and distance parameters.
- **Wave Interference**: Simulate the interference of two waves with adjustable frequency, amplitude, and phase difference. Displays individual and resultant waves.
- **Circular Motion and Centripetal Force**: Visualize the circular motion of an object with adjustable mass, radius, and velocity. Calculates and displays the centripetal force.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/physics-simulations.git
    cd physics-simulations
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

## Usage

After starting the Streamlit app, use the sidebar to navigate between different simulations. Adjust the parameters using the provided sliders and observe the changes in the plots and calculations. Each simulation includes a description and the relevant mathematical formulas for better understanding.

## Project Structure

- `app.py`: The main application script containing all the simulations.
- `requirements.txt`: The list of required Python packages.

## Examples

### Projectile Motion

![Projectile Motion](images/projectile_motion.png)

### Simple Harmonic Motion

![Simple Harmonic Motion](images/simple_harmonic_motion.png)

### Electric Field and Potential

![Electric Field and Potential](images/electric_field_potential.png)

### Wave Interference

![Wave Interference](images/wave_interference.png)

### Circular Motion and Centripetal Force

![Circular Motion](images/circular_motion.png)

## Contributing

Contributions are welcome! If you have any ideas for new simulations or improvements to the existing ones, feel free to open an issue or submit a pull request.

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature/simulation-name
    ```
3. **Commit your changes**:
    ```bash
    git commit -m 'Add some feature'
    ```
4. **Push to the branch**:
    ```bash
    git push origin feature/simulation-name
    ```
5. **Open a pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

This project uses [Streamlit](https://streamlit.io/) for the web interface and [Plotly](https://plotly.com/) for the interactive plots.

---

Enjoy exploring and learning with these physics simulations! If you have any questions or feedback, please don't hesitate to reach out.
