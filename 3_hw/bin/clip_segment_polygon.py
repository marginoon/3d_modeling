import numpy as np

def clip_segment_cyrus_beck(polygon, segment_start, segment_end):
    d = segment_end - segment_start
    t_start = 0
    t_end = 1
    for i in range(len(polygon)):
        edge_start = polygon[i]
        edge_end = polygon[(i + 1) % len(polygon)]
        edge_vector = edge_end - edge_start
        normal = np.array([-edge_vector[1], edge_vector[0]])
        numerator = np.dot(normal, edge_start - segment_start)
        denominator = np.dot(normal, d)
        if denominator == 0:
            if numerator < 0:
                return None
        else:
            t = numerator / denominator
            if denominator > 0:
                if t > 1:
                    return None
                else:
                    t_start = max(t_start, t)
            else:
                if t < 0:
                    return None
                else:
                    t_end = min(t_end, t)
    if t_start <= t_end:
        intersection_start = segment_start + t_start * d
        intersection_end = segment_start + t_end * d

        return intersection_start, intersection_end
    else:
        return None

polygon = np.array([(1, 1), (4, 1), (4, 4), (1, 4)])
segment_start = np.array([2, 2])
segment_end = np.array([3, 3])
clipped_segment = clip_segment_cyrus_beck(polygon, segment_start, segment_end)
if clipped_segment:
    print("Отрезок от {} до {} отсечен многоугольником.".format(clipped_segment[0], clipped_segment[1]))
else:
    print("Отрезок не пересекает многоугольник.")
