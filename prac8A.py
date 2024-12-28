import math

def ball_collide(ball1, ball2):
    # Unpack the balls into (x, y, r) format
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2
    
    # Calculate the distance between the centers of the balls
    distance = math.sqrt((x2 - x1)*2 + (y2 - y1)*2)
    
    # Check if the distance is less than or equal to the sum of the radii
    return distance <= (r1 + r2)

# Example usage
ball1 = (0, 0, 5)  # Ball 1 at (0, 0) with radius 5
ball2 = (3, 4, 3)  # Ball 2 at (3, 4) with radius 3
print(ball_collide(ball1, ball2))  # Output: True or False
