def tally(rows):
    points = {}
    for line in rows:
        if ';' not in line:
            continue
        line = line.split(';')
        if line[0] not in points:
            points[line[0]] = {'MP' : 0, 'W' : 0, 'D' : 0, 'L' : 0, 'P': 0}
        if line[1] not in points:
            points[line[1]] = {'MP' : 0, 'W' : 0, 'D' : 0, 'L' : 0, 'P': 0}
        match line[2]:
            case 'win':
                points[line[0]]['MP'] += 1
                points[line[1]]['MP'] += 1
                points[line[0]]['W'] += 1
                points[line[0]]['P'] += 3
                points[line[1]]['L'] += 1
                continue
            case 'loss':
                points[line[0]]['MP'] += 1
                points[line[1]]['MP'] += 1
                points[line[1]]['W'] += 1
                points[line[1]]['P'] += 3
                points[line[0]]['L'] += 1
                continue
            case 'draw':
                points[line[0]]['MP'] += 1
                points[line[1]]['MP'] += 1
                points[line[0]]['D'] += 1
                points[line[0]]['P'] += 1
                points[line[1]]['D'] += 1
                points[line[1]]['P'] += 1
                continue

    sorted_points = list(points.items())
    sorted_points.sort(key= lambda point:  point[0])
    sorted_points.sort(key= lambda point:  point[1]['P'], reverse=True)
    sorted_points = dict(sorted_points)
    table = ["Team                           | MP |  W |  D |  L |  P"]
    for key in sorted_points:
        table.append(f"{key:<30} | {sorted_points[key]['MP']:>2} | {sorted_points[key]['W']:>2} | {sorted_points[key]['D']:>2} | {sorted_points[key]['L']:>2} | {sorted_points[key]['P']:>2}"
        )
    return table




