from vehicle.model import Vehicle
import matplotlib.pyplot as plt

def simulate_vehicle(vehicle, force, duration, dt):
    if duration <= 0 or dt <= 0:
        raise ValueError("Duration and dt must both be posuitive")
    
    steps = round(duration/dt)
    if abs(steps * dt - duration) > 1e-9:
        raise ValueError("Duration must be divisible by dt")
    
    times = [0.0]
    positions = [vehicle.position]
    velocities = [vehicle.velocity]
    accelerations = []
    for i in range(steps):
        vehicle.update(force, dt)

        times.append((i+1)*dt)
        positions.append(vehicle.position)
        velocities.append(vehicle.velocity)
        accelerations.append(vehicle.acceleration)

    return {
        "time":times,
        "position": positions,
        "velocity": velocities,
        "acceleration": accelerations
    }

def plot_velocity(ideal, realistic):
    plt.figure(figsize=(10,6))

    plt.plot(ideal["time"], ideal["velocity"], label = "Ideal Vehicle")
    plt.plot(realistic["time"], realistic["velocity"], label = "Realistic Vehicle")

    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.title("Vehicle Velocity vs Time")
    plt.legend()
    plt.grid(True)

    plt.savefig("results/velocity.png")
    plt.close()

def plot_position(ideal, realistic):
    plt.figure(figsize=(10,6))

    plt.plot(ideal["time"], ideal["position"], label = "Ideal Vehicle")
    plt.plot(realistic["time"], realistic["position"], label = "Realistic Vehicle")

    plt.xlabel("Time (s)")
    plt.ylabel("Position (m)")
    plt.title("Vehicle Position vs Time")
    plt.legend()
    plt.grid(True)

    plt.savefig("results/position.png")
    plt.close()

def plot_acceleration(ideal, realistic):
    plt.figure(figsize=(10,6))

    plt.plot(ideal["time"][:-1], ideal["acceleration"], label = "Ideal Vehicle")
    plt.plot(realistic["time"][:-1], realistic["acceleration"], label = "Realistic Vehicle")

    plt.xlabel("Time (s)")
    plt.ylabel("Acceleration (m/s²)")
    plt.title("Vehicle Acceleration vs Time")
    plt.legend()
    plt.grid(True)

    plt.savefig("results/acceleration.png")
    plt.close()

def main():
    ideal_car = Vehicle(1600.0)

    realistic_car = Vehicle(
        1600.0, 
        drag_coefficient = 0.28,
        rolling_resistance_coefficient = 0.01
    )

    ideal_results = simulate_vehicle(ideal_car, 4000.0, 30.0, 0.01)
    realistic_results = simulate_vehicle(realistic_car, 4000.0, 30.0, 0.01)

    plot_velocity(ideal_results, realistic_results)
    plot_position(ideal_results, realistic_results)
    plot_acceleration(ideal_results, realistic_results)

    print(
        f"Ideal final velocity: "
        f"{ideal_car.velocity:.2f} m/s"
    )

    print(
        f"Realistic final velocity: "
        f"{realistic_car.velocity:.2f} m/s"
    )

    print(
        f"Ideal final position: "
        f"{ideal_car.position:.2f} m"
    )

    print(
        f"Realistic final position: "
        f"{realistic_car.position:.2f} m"
    )


if __name__ == "__main__":
    main()