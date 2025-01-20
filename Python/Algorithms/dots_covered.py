import math


def covered_dots(width, height, angle):
    angle_rad = math.radians(angle)

    half_width = width / 2
    half_height = height / 2

    cos_theta = math.cos(angle_rad)
    sin_theta = math.sin(angle_rad)

    def is_inside(x, y):

        x_prime = x * cos_theta + y * sin_theta
        y_prime = -x * sin_theta + y * cos_theta
        return (-half_width <= x_prime <= half_width and
                -half_height <= y_prime <= half_height)

    corners = [
        (half_width, half_height),
        (half_width, -half_height),
        (-half_width, half_height),
        (-half_width, -half_height)
    ]
    rotated_corners = [
        (x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta)
        for x, y in corners
    ]

    min_x = math.floor(min(c[0] for c in rotated_corners))
    max_x = math.ceil(max(c[0] for c in rotated_corners))
    min_y = math.floor(min(c[1] for c in rotated_corners))
    max_y = math.ceil(max(c[1] for c in rotated_corners))

    count = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if is_inside(x, y):
                count += 1

    return count


# Example test case
width = 6
height = 4
angle = 45

# Running the test case
print(covered_dots(width, height, angle))
