class rec_area:
    def __init__(self, rectangles):
        self.rectangles = rectangles
    
    def rec_area_sum(self):
        area =0
        for rec in self.rectangles:
            area += (max(rec[0]) - min(rec[0])) * (max(rec[1]) -min(rec[1]))
        return area

    def repeated_rec(self):
        n_m = []
        repeated_rec = []
        for n in range(3):
            for m in range(1,4):
                if n != m:
                    try:
                        inter_x = list(set(self.rectangles[n][0]).intersection(self.rectangles[m][0]))
                        inter_y = list(set(self.rectangles[n][1]).intersection(self.rectangles[m][1]))
                        if inter_x and inter_y:
                            if not (m, n) in n_m:
                                n_m.append((n,m))
                                repeated_rec.append([inter_x, inter_y])

                    except:
                        pass

        return repeated_rec


    def intersection_area(self):
        n_m = []
        repeated_area = 0

        for n in range(3):
            for m in range(1,4):
                if n != m:
                    try:
                        inter_x = list(set(self.rectangles[n][0]).intersection(self.rectangles[m][0]))
                        inter_y = list(set(self.rectangles[n][1]).intersection(self.rectangles[m][1]))
                        if inter_x and inter_y:
                            if not (m, n) in n_m:
                                repeated_area += (max(inter_x) - min(inter_x)) * (max(inter_y) - min(inter_y))
                                n_m.append((n,m))
                    except: 
                        pass

        return repeated_area






rectangles = []
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    rectangles.append([list(range(x1,x2+1)), list(range(y1, y2+1))])


r1 = rec_area(rectangles)
rectangle_area = r1.rec_area_sum()
rectangle_area -= r1.intersection_area()
re1 = rec_area(r1.repeated_rec())

if re1.repeated_rec():
    set_plus_rec = []
    for rect in re1.repeated_rec():
        if not rect in set_plus_rec:
            set_plus_rec.append(rect)
    
    for r in set_plus_rec:
        rectangle_area += (max(r[0]) - min(r[0])) * (max(r[1]) -min(r[1]))
    
    if len(set_plus_rec) > 1:        
        re2 = rec_area(re1.repeated_rec())
        if re2.repeated_rec():
            set_plus_rec = []
            for rect in re2.repeated_rec():
                if not rect in set_plus_rec:
                    set_plus_rec.append(rect)
            for r in set_plus_rec:
                rectangle_area += (max(r[0]) - min(r[0])) * (max(r[1]) -min(r[1]))

print(rectangle_area)