class Vehicle:
    def __init__(self, mass, drag_coefficient = 0.0, frontal_area = 2.2, rolling_resistance_coefficient = 0.0, air_density = 1.225):
        if mass <= 0:
            raise ValueError("Vehicle mass must be positive")
            
        self.mass = mass
        self.velocity = 0.0

        self.drag_coefficient = drag_coefficient
        self.frontal_area = frontal_area
        self.rolling_resistance_coefficient = rolling_resistance_coefficient
        self.air_density = air_density

    def update(self, force, dt):
        if dt <= 0:
            raise ValueError("Time step must be positive")
        
        drag_force = (
            0.5 *
            self.air_density *
            self.drag_coefficient *
            self.frontal_area *
            self.velocity **2
        )

        rolling_force = (
            self.rolling_resistance_coefficient *
            self.mass *
            9.81
        )
        
        net_force = force - drag_force - rolling_force

        acceleration = net_force/self.mass
        
        self.velocity = max(0, self.velocity + acceleration * dt)
        
        return self.velocity 