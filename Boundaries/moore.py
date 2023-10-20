import numpy as np

def moore_boundary(image):
    height, width = image.shape
    boundary_image = np.zeros((height, width), dtype=int)

    def is_boundary_pixel(x, y):
        if image[x][y] == 0:
            return False
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if image[i][j] == 0:
                    return True
        return False

    for x in range(1, height - 1):
        for y in range(1, width - 1):
            if is_boundary_pixel(x, y):
                boundary_image[x][y] = 1

    return boundary_image