"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet."""
    
    eat_ghost = power_pellet_active and touching_ghost
    return eat_ghost

def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten."""

    score = touching_power_pellet or touching_dot
    return score

def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet."""

    lose = not power_pellet_active and touching_ghost
    return lose

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten."""

    win = has_eaten_all_dots and (power_pellet_active or not touching_ghost)
    return win