from random import randint, choices
import pprint

point = open("C:\\Users\\HP\\Desktop\\data\\point.txt")
print(point.read())



def remove_missing_values(point):
    with open(point,'r') as f, open('./point.txt','w') as f_out:
        for line in f:
            if not any(value == "" for value in line.strip().split(',')):
                f_out.write(line)

remove_missing_values("point.txt")

POINT = tuple[float, float, float]
def distance(p1: POINT, p2: POINT) -> float:
  return (abs (p1[0] - p2[0]) + abs (p1[1] - p2[1]) + abs (p1[2] - p2[2]))


k = int(input("K = "))
centers = [(randint(-10, 10), randint(-10, 10), randint(-10, 10)) for _ in range(k)]

def k_means(points: list[POINT], centers: list[POINT]):
    result = [
        {
            "center": center,
            "points": [],
        }
        for center in centers
    ]
    for point in points:
        index, minimum = 0, distance(point, centers[0])

        i = 1
        # for i, center in enumerate(centers):
        while i < len(centers):
            d = distance(point, centers[i])
            if d < minimum:
                index, minimum = i, d

            i += 1

        result[index]["points"].append(point)

    return result

while True:
    clusters = k_means(points, centers)
    new_centers = []
    for cluster in clusters:
        x, y, z = zip(*cluster["points"])
        new_centers.append(
            (
                sum(x) / len(x),
                sum(y) / len(y),
                sum(z) / len(z),
            )
        )

    if new_centers == centers:
        break

    centers = new_centers


pprint.pprint(clusters)
