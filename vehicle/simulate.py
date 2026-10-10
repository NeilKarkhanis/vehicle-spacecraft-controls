from model import Vehicle
import matplotlib.pyplot as plt

MASS = 1600.0
FORCE = 4000.0
DT = 0.1
TOTAL_TIME = 10.0

vehicle = Vehicle(MASS)
times = [0.0]
velocities = [vehicle.velocity]

total_steps = int(TOTAL_TIME/DT)

for step in range(1, total_steps + 1):
    velocity = vehicle.update(FORCE, DT)
    times.append(step * DT)
    velocities.append(velocity)

print(f"Final velocity {vehicle.velocity:.2f} m/s")

plt.plot(times, velocities)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Electric Vehicle Acceleration Simulation")
plt.grid(True)
plt.show()