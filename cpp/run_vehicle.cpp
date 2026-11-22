#include <algorithm>
#include <iomanip>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string_view>

class Vehicle {
public:
    explicit Vehicle(
        double mass, 
        double drag_coefficient = 0.0, 
        double frontal_area = 2.2, 
        double rolling_resistance_coefficient = 0.0,
        double air_density = 1.225)
    : mass_(mass),
    drag_coefficient_(drag_coefficient), 
    frontal_area_(frontal_area),
    rolling_resistance_coefficient_(rolling_resistance_coefficient),
    air_density_(air_density){
    
        if (mass <= 0.0){
            throw std::invalid_argument("Vehicle mass must be positive.");
        }
    }

    void update(double force, double dt){
        if (dt <= 0.0){
            throw std::invalid_argument("Time step must be positive");
        }

        const double drag_force = 0.5 * air_density_ * drag_coefficient_ * frontal_area_ * (velocity_ * velocity_);
        const double rolling_force = rolling_resistance_coefficient_ * mass_ * 9.81;

        acceleration_ = (force - drag_force - rolling_force)/mass_;
        velocity_ = std::max(0.0, velocity_ + acceleration_ * dt);
        position_ += velocity_ * dt;
    }

    double velocity() const {
        return velocity_;
    }

    double position() const {
        return position_;
    }

private:
    double mass_;
    double drag_coefficient_;
    double frontal_area_;
    double rolling_resistance_coefficient_;
    double air_density_;

    double velocity_ = 0.0;
    double position_ = 0.0;
    double acceleration_ = 0.0;
};

void run_scenario(std::string_view name, Vehicle vehicle){
    constexpr double force = 4000.0;
    constexpr double dt = 0.01;
    constexpr int steps = 3000;

    for(int step = 0; step < steps; ++step){
        vehicle.update(force,dt);
    }
    std::cout << name <<','<<vehicle.velocity() << ',' <<vehicle.position()<<'\n';
}

int main() {
    std::cout << std::setprecision(std::numeric_limits<double>::max_digits10);
    std::cout << "scenario,velocity_m_s,position_m\n";

    run_scenario("ideal", Vehicle(1600.0));
    run_scenario("realistic", Vehicle(1600.0, 0.28, 2.2, 0.01));
}
