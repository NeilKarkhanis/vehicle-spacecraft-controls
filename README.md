# Vehicle & Spacecraft Controls Verification Platform

A software-in-the-loop (SIL) simulation and verification project designed to model vehicle and spacecraft dynamics, evaluate control algorithms, and automate engineering tests.

The project is being developed using Python, with planned C++17 and Linux integration.

## Current Features

- One-dimensional vehicle dynamics simulation
- Aerodynamic drag and rolling resistance modelling
- Semi-implicit Euler numerical integration
- Position, velocity, and acceleration tracking
- Comparison of ideal and realistic vehicle motion
- Automated unit testing using PyTest
- Simulation visualization using Matplotlib

## Vehicle Dynamics Model

The vehicle model calculates acceleration using Newton's second law:

\[
a = \frac{F_{\text{engine}} - F_{\text{drag}} - F_{\text{rolling}}}{m}
\]

Aerodynamic drag is calculated as:

\[
F_{\text{drag}} = \frac{1}{2}\rho C_d A v^2
\]

Rolling resistance is approximated as:

\[
F_{\text{rolling}} = C_{rr}mg
\]

Where:

- \(m\): Vehicle mass (kg)
- \(F_{\text{engine}}\): Applied driving force (N)
- \(\rho\): Air density (kg/m³)
- \(C_d\): Aerodynamic drag coefficient
- \(A\): Vehicle frontal area (m²)
- \(v\): Vehicle velocity (m/s)
- \(C_{rr}\): Rolling resistance coefficient
- \(g\): Gravitational acceleration (9.81 m/s²)

The model assumes forward-only motion on a level surface. Velocity is constrained to be nonnegative.

### Numerical Integration

The simulation uses semi-implicit Euler integration:

\[
v_{k+1} = \max(0, v_k + a_k\Delta t)
\]

\[
x_{k+1} = x_k + v_{k+1}\Delta t
\]

A configurable time step allows the vehicle state to be advanced through the simulation.

## Simulation Scenarios

The simulation compares two vehicles with identical masses and applied engine forces.

**Ideal Vehicle**

- Mass: 1600 kg
- Applied force: 4000 N
- No aerodynamic drag
- No rolling resistance

**Realistic Vehicle**

- Mass: 1600 kg
- Applied force: 4000 N
- Drag coefficient: 0.28
- Frontal area: 2.2 m²
- Rolling resistance coefficient: 0.01
- Air density: 1.225 kg/m³

Both scenarios run for 30 seconds using a time step of 0.01 seconds.

The simulation generates three graphs:

1. Velocity versus time
2. Position versus time
3. Acceleration versus time

The graphs are saved in the `results/` directory.

## Installation

Clone the repository and navigate to the project directory.

Create a Python virtual environment:

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Simulation

From the project root, run:

```bash
python -m scripts.run_vehicle
```

The program prints the final velocities and positions of the ideal and realistic vehicles and saves the simulation plots.

## Automated Verification

The vehicle dynamics model is tested using PyTest.

The verification tests cover:

- Ideal vehicle velocity under constant acceleration
- Reduced velocity due to aerodynamic drag and rolling resistance
- Stationary vehicle behaviour
- Invalid vehicle mass
- Invalid simulation time steps

Additional tests cover position and acceleration calculations and resistance effects once implemented.

Run the tests using:

```bash
python -m pytest -v
```

## Project Structure

```text
vehicle-spacecraft-controls/
├── vehicle/
│   ├── __init__.py
│   └── model.py
├── scripts/
│   └── run_vehicle.py
├── tests/
│   └── test_vehicle.py
├── results/
│   ├── velocity.png
│   ├── position.png
│   └── acceleration.png
├── requirements.txt
└── README.md
```

## Planned Development

The next phases will expand the project into a more complete controls and verification platform.

**C++17 and Linux Integration**
- Implement vehicle dynamics in C++17
- Configure builds using CMake
- Compare C++ and Python simulation results

**Feedback Control**
- Develop a PID speed controller
- Implement reference tracking and disturbance scenarios
- Measure overshoot, settling time, and steady-state error

**Spacecraft Dynamics**
- Develop a simplified spacecraft attitude dynamics model
- Implement attitude-control algorithms
- Simulate disturbances and evaluate control performance

**Verification and Automation**
- Expand automated test coverage
- Add simulation telemetry and performance metrics
- Integrate automated builds and tests using GitHub Actions
- Document reproducible verification results

## Technologies

**Currently used:** Python, PyTest, Matplotlib, Git

**Planned:** C++17, CMake, Linux, GitHub Actions

## Project Status

Python vehicle dynamics simulation and visualization implemented. Automated verification and additional simulation features are being developed.