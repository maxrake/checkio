def determinant(a, b, c, d, e, f, g, h, i):
    """Calculate the determinant of a three by three matrix.
    
    Where the matrix contents match the parameters, like so:
        |a b c|
        |d e f|
        |g h i|
    """
    return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)


def checkio(data):
    """Provide the formula for a circle given three points on that circle.
    
    This determinant based method was inspired by:
    http://mathforum.org/library/drmath/view/55239.html
    """
    points = data.replace('(', '').replace(')', '').split(',')
    x1, y1, x2, y2, x3, y3 = map(int, points)
    
    denominator = 2 * determinant(x1, y1, 1, x2, y2, 1, x3, y3, 1)
    h = determinant(x1**2 + y1**2, y1, 1, x2**2 + y2**2, y2, 1,
                    x3**2 + y3**2, y3, 1) / denominator
    k = determinant(x1, x1**2 + y1**2, 1, x2, x2**2 + y2**2, 1,
                    x3, x3**2 + y3**2, 1) / denominator
    r = ((x1 - h)**2 + (y1 - k)**2) ** 0.5

    return "(x-{:g})^2+(y-{:g})^2={:g}^2".format(
        round(h, 2), round(k, 2), round(r, 2))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
    assert checkio("(1,1),(2,1),(1,2)") == "(x-1.5)^2+(y-1.5)^2=0.71^2"
    print(" [+] All asserts passed.")
