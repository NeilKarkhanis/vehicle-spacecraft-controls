class Vehicle:
    def __init__(self, mass):
        self.mass = mass
        self.velocity = 0.0

    def update(self, force, dt):
        acceleration = force/self.mass
        self.velocity = self.velocity + acceleration * dt
        return self.velocity 