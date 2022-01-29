def intersection_area(rectangles):
    n_m = []
    repeated_area = 0
    repeated_rec = []
    try:
        for n in range(3):
            for m in range(1,4):
                if n != m:
                    inter_x = list(set(rectangles[n][0]).intersection(rectangles[m][0]))
                    inter_y = list(set(rectangles[n][1]).intersection(rectangles[m][1]))
                    if inter_x and inter_y:
                        if not (m, n) in n_m:
                            repeated_area += (max(inter_x) - min(inter_x)) * (max(inter_y) - min(inter_y))
                            n_m.append((n,m))
                            repeated_rec.append([inter_x, inter_y])
    except:
        pass
    if intersection_area(repeated_rec) > 0:
        repeated_area += intersection_area(repeated_rec)
    return repeated_area






rectangles = []
rectangle_area = 0
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    rectangle_area += (x2 - x1) * (y2 - y1)

    rectangles.append([list(range(x1,x2+1)), list(range(y1, y2+1))])
intersection_area(rectangles)




