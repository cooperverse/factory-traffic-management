PHASES = {
    "NORTH_SOUTH": ["NORTH", "SOUTH"],
    "EAST_WEST": ["EAST", "WEST"],
}

def get_phase_for_direction(direction):
    for phase, directions in PHASES.items():
        if direction in directions:
            return phase

    return None
def is_safe_green_configuration(green_directions):
    green_directions = set(green_directions)

    north_south_green = bool(
        green_directions & set(PHASES["NORTH_SOUTH"])
    )
    east_west_green = bool(
        green_directions & set(PHASES["EAST_WEST"])
    )

    return not (north_south_green and east_west_green)