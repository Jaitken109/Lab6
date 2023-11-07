import math
from render import InitRender, Render

G = 6.67408e-11

# Define the bodies
central_body = (1e12, (400.0, 400.0), (0.0, 0.0))  # Central body with large mass, positioned at the origin, stationary
planet1 = (1e4, (360.0, 400.1), (0.0001, 1.5))   # Planet 1 starting at (1000, 0) with a velocity vector giving it a circular orbit
planet2 = (1e3, (400.1, 280.0), (-0.5, 0.0001))  # Planet 2 starting at (0, -500) with a velocity vector giving it a circular orbit

# Define the system
system = [central_body, planet1, planet2]

def calculate_distance(body1, body2):
    x1, y1 = body1[1]
    x2, y2 = body2[1]
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance
    pass


def calculate_force(body1, body2):
    m1, (x1, y1), _ = body1
    m2, (x2, y2), _ = body2
    distance = calculate_distance(body1, body2)
    if distance == 0:
        return (0, 0)
    else:
        force_magnitude = G * m1 * m2 / (distance ** 2)
        force_x = force_magnitude * (x2 - x1) / distance
        force_y = force_magnitude * (y2 - y1) / distance

        return (force_x, force_y)
    pass

def calculate_net_force_on(body, system):
    net_force_x = 0
    net_force_y = 0
    for other_body in system:
        if other_body != body:
            force_x, force_y = calculate_force(body, other_body)
            net_force_x += force_x
            net_force_y += force_y
    return (net_force_x, net_force_y)
    pass

def calculate_acceleration(body, system):
    net_force_x, net_force_y = calculate_net_force_on(body, system)
    mass = body[0]
    acceleration_x = net_force_x / mass
    acceleration_y = net_force_y / mass
    return (acceleration_x, acceleration_y)
    pass

def update_velocity(system, dt):
    updated_system = []
    for body in system:
        acceleration_x, acceleration_y = calculate_acceleration(body, system)
        old_velocity_x, old_velocity_y = body[2]
        new_velocity_x = old_velocity_x + acceleration_x * dt
        new_velocity_y = old_velocity_y + acceleration_y * dt
        updated_body = (body[0], body[1], (new_velocity_x, new_velocity_y))
        updated_system.append(updated_body)
    return updated_system
    pass
   

def update(system, dt):
    updated_velocities = update_velocity(system, dt)
    updated_system = []
    for i, body in enumerate(system):
        position_x, position_y = body[1]
        old_velocity_x, old_velocity_y = body[2]
        new_velocity_x, new_velocity_y = updated_velocities[i][2]
        new_position_x = position_x + new_velocity_x * dt
        new_position_y = position_y + new_velocity_y * dt
        updated_body = (body[0], (new_position_x, new_position_y), (new_velocity_x, new_velocity_y))
        updated_system.append(updated_body)
    return updated_system
    pass

def simulate(system, dt, num_steps):
    current_system_state = system
    for step in range(num_steps):
        current_system_state = update(current_system_state, dt)
    return current_system_state
    pass

def simulate_with_visualization(system, dt, num_steps):
    """Simulates the motion of a system of bodies for a given number of time steps, and visualizes the motion"""
    pass

if __name__ == '__main__':
    pass





