def eat_ghost(power_pill_active, touching_ghost):
    """Defines if pac-man can eat the ghost or not"""
    return power_pill_active and touching_ghost

def score(touching_power_pill, touching_point):
    """Defines if pac-man scores"""
    return touching_power_pill or touching_point

def lose(power_pill_active, touching_ghost):
    """Defines if pac-man loses"""
    return not power_pill_active and touching_ghost

def win(ate_all_points, power_pill_active, touching_ghost):
    """Defines if pac-man wins"""
    return ate_all_points and not lose(power_pill_active, touching_ghost)