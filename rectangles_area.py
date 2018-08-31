from itertools import islice
import random


def rects_gen(width, height):
    while True:
        x1 = random.randint(0, width - 1)
        y1 = random.randint(1, height)
        x2 = random.randint(x1 + 1, width)
        y2 = random.randint(0, y1 - 1)
        yield(x1, y1, x2, y2)


def bounding_box(rects):
    return (min(r[0] for r in rects),
            max(r[1] for r in rects),
            max(r[2] for r in rects),
            min(r[3] for r in rects))


def area(rect):
    a, b, c, d = rect
    return (c - a) * (b - d)


def clip(bb, rects):
    if not rects:
        return []

    (x1, y1, x2, y2) = rects[0]
    rs = rects[1:]
    (a1, b1, a2, b2) = bb

    if a1 == a2 or b1 == b2:
        return []

    if a1 >= x2 or a2 <= x1 or y1 <= b2 or y2 >= b1:
        return clip(bb, rs)

    result = [(max(a1, x1), min(b1, y1), min(a2, x2), max(b2, y2))]
    return result + clip(bb, rs)


def cover(bb, rects):

    if not rects:
        return 0
    rc = rects[0]
    rs = rects[1:]

    (a1, b1, a2, b2) = bb
    (x1, y1, x2, y2) = rc

    top = (a1, b1, a2, y1)
    bottom = (a1, y2, a2, b2)
    left = (a1, y1, x1, y2)
    right = (x2, y1, a2, y2)

    sum_area = sum(cover(x, clip(x, rs)) for x in [top, bottom, left, right])
    return area(rc) + sum_area


def main():
    width_canvas = 10
    height_canvas = 10
    rects_num = 5

    rs = list(islice(rects_gen(width_canvas, height_canvas), 0, rects_num))

    painted_area = cover(bounding_box(rs), rs)
    canvas_area = width_canvas * height_canvas
    unpainted_area = canvas_area - painted_area

    print("Canvas area:", canvas_area)
    print("Painted area:", painted_area)
    print("Unpainted area:", unpainted_area)


if __name__ == '__main__':
    main()
