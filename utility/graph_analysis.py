from utility.tools import *

def relative_min_max(pts):
    relative_min = []
    relative_max = []
    prev_pts = [(0, pts[0]), (1, pts[1])]
    for i in range(1, len(pts) - 1):
        append_to = ''
        if pts[i-1] > pts[i] < pts[i+1]:
            append_to = 'min'
        elif pts[i-1] < pts[i] > pts[i+1]:
            append_to = 'max'
        if append_to:
            if relative_min or relative_max:
                prev_distance = pythagorean_distance(prev_pts[0], prev_pts[1]) * 0.5
                curr_distance = pythagorean_distance(prev_pts[1], (i, pts[i]))
                if curr_distance >= prev_distance:
                    prev_pts[0] = prev_pts[1]
                    prev_pts[1] = (i, pts[i])
                    if append_to == 'min':
                        relative_min.append((i, pts[i]))
                    else:
                        relative_max.append((i, pts[i]))
            else:
                prev_pts[0] = prev_pts[1]
                prev_pts[1] = (i, pts[i])
                if append_to == 'min':
                    relative_min.append((i, pts[i]))
                else:
                    relative_max.append((i, pts[i]))
    return relative_min, relative_max