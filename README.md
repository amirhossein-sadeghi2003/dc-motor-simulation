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
- simulate current, speed, and position response
- analyze the effect of inertia
- analyze the effect of friction
- understand the relation between electrical input and mechanical output

## Parameters

The base simulation uses:

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

## Simulations

### 1. Current Response

The simulation plots the armature current over time.

This shows the electrical transient behavior of the motor.

### 2. Speed Response

The simulation plots the angular velocity of the motor over time.

The speed starts from zero and gradually approaches a steady value.

### 3. Position Response

The simulation also plots the angular position of the motor.

Since position is the integral of angular velocity, it increases over time as the motor rotates.

### 4. Effect of Inertia

The project compares different values of inertia:

- `J = 0.01`
- `J = 0.02`
- `J = 0.05`

This comparison shows that lower inertia gives a faster speed response, while higher inertia makes the motor respond more slowly.

### 5. Effect of Friction

The project compares different values of friction:

- `b = 0.05`
- `b = 0.2`
- `b = 0.5`

This comparison shows that lower friction allows the motor to reach a higher speed, while higher friction reduces the response and steady-state speed.

## Results

This project shows important aspects of DC motor dynamics:

- a constant voltage produces time-varying current and speed response
- angular velocity approaches a steady value
- angular position increases continuously over time
- inertia affects how fast the motor accelerates
- friction affects both transient and steady-state behavior

## Output

Saved figures:

- `results/current_response.png`
- `results/speed_response.png`
- `results/position_response.png`
- `results/inertia_effect.png`
- `results/friction_effect.png`

## Run

From the project root:

```bash
python3 src/main.py
