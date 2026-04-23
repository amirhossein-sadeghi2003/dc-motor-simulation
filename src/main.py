import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

R = 2.0
L = 0.5
Ke = 0.1
Kt = 0.1
J = 0.02
b = 0.2

V = 12.0

t = np.linspace(0, 5, 1000)

i0 = 0.0
omega0 = 0.0
theta0 = 0.0


def dc_motor(time, y):
    i = y[0]
    omega = y[1]
    theta = y[2]

    didt = (V - R * i - Ke * omega) / L
    domegadt = (Kt * i - b * omega) / J
    dthetadt = omega

    return [didt, domegadt, dthetadt]


sol = solve_ivp(dc_motor, [0, 5], [i0, omega0, theta0], t_eval=t)

current = sol.y[0]
omega = sol.y[1]
theta = sol.y[2]

plt.figure(figsize=(10, 6))
plt.plot(sol.t, omega)
plt.title("DC Motor Speed Response")
plt.xlabel("Time")
plt.ylabel("Angular Velocity")
plt.grid(True)
plt.tight_layout()
plt.savefig("results/speed_response.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(sol.t, theta)
plt.title("DC Motor Position Response")
plt.xlabel("Time")
plt.ylabel("Angular Position")
plt.grid(True)
plt.tight_layout()
plt.savefig("results/position_response.png", dpi=300)
plt.show()

# Effect of inertia
J_values = [0.01, 0.02, 0.05]

plt.figure(figsize=(10, 6))

for J_value in J_values:
    def motor_with_inertia(time, y):
        i = y[0]
        omega = y[1]
        theta = y[2]

        didt = (V - R * i - Ke * omega) / L
        domegadt = (Kt * i - b * omega) / J_value
        dthetadt = omega

        return [didt, domegadt, dthetadt]

    sol_J = solve_ivp(motor_with_inertia, [0, 5], [i0, omega0, theta0], t_eval=t)
    plt.plot(sol_J.t, sol_J.y[1], label=f"J = {J_value}")

plt.title("Effect of Inertia on Speed Response")
plt.xlabel("Time")
plt.ylabel("Angular Velocity")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("results/inertia_effect.png", dpi=300)
plt.show()
