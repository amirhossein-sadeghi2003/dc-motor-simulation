# DC Motor Simulation

This project simulates the dynamic behavior of a DC motor using a simple electromechanical model.

## Description

A DC motor is a common electromechanical system that converts electrical energy into rotational motion.

This project models the motor using differential equations and studies how the motor responds to a constant voltage input.

The model includes:

- electrical dynamics
- mechanical dynamics
- angular position

## Equations

The system is described by:

di/dt = (V - R i - Ke w) / L

dw/dt = (Kt i - b w) / J

dtheta/dt = w

where:

- `V` is the input voltage
- `i` is the armature current
- `w` is the angular velocity
- `theta` is the angular position
- `R` is the resistance
- `L` is the inductance
- `Ke` is the back EMF constant
- `Kt` is the torque constant
- `J` is the moment of inertia
- `b` is the damping/friction coefficient

## Goal

The goal of this project is to:

- model a simple DC motor
- simulate its speed response
- simulate its position response
- understand the relation between electrical input and mechanical output

## Parameters

The simulation uses:

- `R = 2.0`
- `L = 0.5`
- `Ke = 0.1`
- `Kt = 0.1`
- `J = 0.02`
- `b = 0.2`
- `V = 12.0`

Initial conditions:

- `i0 = 0.0`
- `omega0 = 0.0`
- `theta0 = 0.0`

## Results

The simulation generates two outputs:

- speed response
- position response

The speed starts from zero and gradually approaches a steady value.

The position increases over time as the motor rotates.

## Output

Saved figures:

- `results/speed_response.png`
- `results/position_response.png`

## Run

From the project root:

```bash
python3 src/main.py
