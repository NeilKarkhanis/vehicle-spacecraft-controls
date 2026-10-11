import pytest
from vehicle.model import Vehicle

def test_ideal_vehicle_acceleration():
    car = Vehicle(1600.0)
    dt = 0.1
    force = 4000.0
    for step in range(100):
        car.update(force, dt)

    assert car.velocity == pytest.approx(25.0)

def test_resistance_reduces_velocity():
    ideal_car = Vehicle(1600.0)
    
    realistic_car = Vehicle(
        1600.0, 
        drag_coefficient=0.28,
        rolling_resistance_coefficient = 0.01
    )

    for step in range(100):
        ideal_car.update(4000.0, 0.1)
        realistic_car.update(4000.0, 0.1)

    assert realistic_car.velocity < ideal_car.velocity

def test_stationary_vehicle_stays_stopped():
    car = Vehicle(
        1600.0,
        drag_coefficient = 0.28,
        rolling_resistance_coefficient = 0.01
    )

    velocity = car.update(0.0, 0.1)

    assert velocity == 0.0

def test_invalid_vehicle_mass():
    with pytest.raises(ValueError):
        car = Vehicle(0.0)

def test_invalid_time_steps():
    car = Vehicle(1600.0)

    with pytest.raises(ValueError):
        car.update(4000.0, -0.1)