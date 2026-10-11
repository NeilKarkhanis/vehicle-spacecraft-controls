from model import Vehicle
import matplotlib.pyplot as plt

MASS = 1600.0
DRIVING_FORCE = 4000.0
DT = 0.1
TOTAL_TIME = 10.0

ideal_car = Vehicle(MASS)

realistic_car = Vehicle(
    MASS, 
    drag_coefficient = 0.28,
    rolling_resistance_coefficient = 0.01
)

times = [0.0]
ideal_velocities = [ideal_car.velocity]
realistic_velocities = [realistic_car.velocity]

total_steps = int(TOTAL_TIME/DT)

for step in range(1, total_steps + 1):
    ideal_velocity = ideal_car.update(DRIVING_FORCE, DT)
    realistic_velocity = realistic_car.update(DRIVING_FORCE, DT)

    times.append(step * DT)
    ideal_velocities.append(ideal_velocity)
    realistic_velocities.append(realistic_velocity)

print(f"Ideal final velocity {ideal_car.velocity:.2f} m/s")
print(f"Realistic final velocity {realistic_car.velocity:.2f} m/s")

plt.plot(times, ideal_velocities, label="Ideal Vehicle")
plt.plot(times, realistic_velocities, label="Realistic Vehicle")

plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Electric Vehicle Acceleration Simulation")

plt.legend()
plt.grid(True)
plt.show()