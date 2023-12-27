import numpy as np
from PIL import Image


def draw_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy > dx

    if slope:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    error = dx // 2
    y = y1
    y_step = 1 if y1 < y2 else -1

    points = []

    for x in range(x1, x2 + 1):
        coord = (y, x) if slope else (x, y)
        points.append(coord)
        error -= dy
        if error < 0:
            y += y_step
            error += dx

    return points

def draw(image, points, color):
    for point in points:
        image.putpixel(point, color)

def fill2D(vertexes):
	points = dict()
	for i in range(len(vertexes)):
		x1, y1 = vertexes[i].x, vertexes[i].y
		x2 = vertexes[(i + 1) % len(vertexes)].x
		y2 = vertexes[(i + 1) % len(vertexes)].y

		if y2 == y1:
			continue

		line = draw_line(x1, y1, x2, y2)
		if y2 > y1:
			line.remove((x1, y1))
		else:
			line.remove((x2, y2))

		for point in line:
			if point[1] in points:
				points[point[1]].append(point[0])
			else:
				points[point[1]] = [point[0]]

	line = []
	for y in points:
		points[y].sort()
		if len(points[y]) % 2 == 1:
			points[y] = del_seq(points[y])
		for i in range(len(points[y]) // 2):
			line += [(k, y) for k in range(points[y][2 * i], points[y][2 * i + 1] + 1)]
	return line

class point3:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z


def fill3D(vertexes):
	points = fill2D(vertexes)
	A, B, C, D = get_plane(vertexes[0], vertexes[1], vertexes[2])
	find_z = lambda x, y: int((-D - A*x - B*y) / C)

	new_points = []
	for point in points:
		z = find_z(point[0], point[1])
		new_points.append(point3(point[0], point[1], z))
	return new_points

def update_buffer(points, z_buffer):
	for point in points:
		if point.z < z_buffer[800 * point.y + point.x]:
			z_buffer[800 * point.y + point.x] = point.z

def draw_buffer(image, points, z_buffer, color):
	for point in points:
		if point.z <= z_buffer[800 * point.y + point.x]:
			image.putpixel((int(point.x), int(point.y)), color)
def to_numpy(points):
	new_points = []
	for point in points:
		new_points.append(np.array([[point.x, point.y, point.z, 1]]))
	return new_points

def to_point3(points):
	new_points = []
	for point in points:
		new_points.append(point3(int(point[0][0]), int(point[0][1]), int(point[0][2])))
	return new_points

def rotate3D(points, angle, axis=1): # 1-z, 2-x, 3-y
	new_points = to_numpy(points)
	if axis == 1:
		M = np.array([
			[np.cos(angle), -np.sin(angle), 0, 0],
			[np.sin(angle),  np.cos(angle), 0, 0],
			[0, 0, 1, 0],
			[0, 0, 0, 1]
		])
	elif axis == 2:
		M = np.array([
			[1, 0, 0, 0],
			[0, np.cos(angle), -np.sin(angle), 0],
			[0, np.sin(angle),  np.cos(angle), 0],
			[0, 0, 0, 1]
		])
	elif axis == 3:
		M = np.array([
			[np.cos(angle), 0, -np.sin(angle), 0],
			[0, 1, 0, 0],
			[np.sin(angle), 0,  np.cos(angle), 0],
			[0, 0, 0, 1]
		])

	for i in range(len(points)):
		new_points[i] = new_points[i] @ M.T

	return to_point3(new_points)

def shift3D(points, dx, dy, dz):
	new_points = to_numpy(points)
	M = np.array([
			[1, 0, 0, dx],
			[0, 1, 0, dy],
			[0, 0, 1, dz],
			[0, 0, 0, 1]
		])

	for i in range(len(points)):
		new_points[i] = new_points[i] @ M.T

	return to_point3(new_points)

def scale3D(points, sx, sy, sz):
	new_points = to_numpy(points)
	M = np.array([
			[sx, 0, 0, 0],
			[0, sy, 0, 0],
			[0, 0, sz, 0],
			[0, 0, 0, 1]
		])

	for i in range(len(points)):
		new_points[i] = new_points[i] @ M.T

	return to_point3(new_points)

def reflect3D(points, line, axis=1): # 1-z, 2-x, 3-y
	new_points = to_numpy(points)
	if axis == 1:
		M = np.array([
				[1, 0, 0, 0],
				[0, 1, 0, 0],
				[0, 0, -1, 2 * line],
				[0, 0, 0, 1]
			])
	elif axis == 2:
		M = np.array([
				[-1, 0, 0, 2 * line],
				[0, 1, 0, 0],
				[0, 0, 1, 0],
				[0, 0, 0, 1]
			])
	elif axis == 3:
		M = np.array([
				[1, 0, 0, 0],
				[0, -1, 0, 2 * line],
				[0, 0, 1, 0],
				[0, 0, 0, 1]
			])

	for i in range(len(points)):
		new_points[i] = new_points[i] @ M.T

	return to_point3(new_points)

if __name__ == '__main__':
	vertexes1 = [
		point3(300, 300, 100),
		point3(350, 400, 100),
	 	point3(500, 150, 300)
	]

	vertexes2 = [
		point3(200, 100, 0),
		point3(400, 400, 200),
		point3(500, 200, 200)
	]

	with Image.open('3D.png') as im:
		im.paste((0, 0, 0), (0, 0, im.size[0], im.size[1]))

		z_buffer = [1000] * 800 * 600

		points1 = fill3D(vertexes1)
		points2 = fill3D(vertexes2)

		points1 = reflect3D(points1, 400, 2)
		points2 = reflect3D(points2, 400, 2)

		update_buffer(points1, z_buffer)
		update_buffer(points2, z_buffer)

		draw_buffer(im, points2, z_buffer, (0, 0, 255))
		draw_buffer(im, points1, z_buffer, (255, 0, 0))


		im.save('3D.png')
