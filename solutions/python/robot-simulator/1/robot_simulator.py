# Globals for the directions
# Change the values as you see fit
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"
DIRECTIONS = [EAST, NORTH, WEST, SOUTH]
MOVEMENT_VECTORS = {
    "NORTH": (0, 1),   # x stays same, y increases
    "EAST":  (1, 0),   # x increases, y stays same
    "SOUTH": (0, -1),  # x stays same, y decreases
    "WEST":  (-1, 0)   # x decreases, y stays same
}
#east +x, west -x, north +y, south -y

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)
    
    def move(self, instructions):

        for instruction in list(instructions):
            match instruction:
                case "R":
                    self.direction = DIRECTIONS[(DIRECTIONS.index(self.direction) + 3) % 4]
                case "L":
                    self.direction = DIRECTIONS[(DIRECTIONS.index(self.direction) + 1) % 4]
                case "A":
                    dx, dy = MOVEMENT_VECTORS[self.direction]
                    current_x, current_y = self.coordinates
                    self.coordinates = (current_x + dx, current_y + dy)

        return self.coordinates, self.direction