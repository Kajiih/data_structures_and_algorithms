"""Count Rectangles."""

from collections import defaultdict
from enum import unique


def count_rectangles(points: list[tuple[int, int]]) -> int:
    """
    Given a list of points on a 2d plan, count the nb of rectangles (4 sides of area > 0, opposite sides equal) parallel to the x axis.

    Inputs: list[tuple[int,int]]: [(1, 1) (2, 2) (3 2) (1 5) (-1 2)]
    Outputs: int: 0,1,2,3,..
    Edge cases:
    - duplicate points
    - empty points/single point
    - no rectangle
    Assumptions:
    - only integer coordinates


    .   .   .
    .   .   .
    .   .   .
    3 rectangles



    Duplicates:
    - Count the nb of points at a given coord + take it into account when considering this coord
    Counting each rectangle only once:
    - Count rectangle only when the first point considered is on the top left


    Solution:
    - Count the nb of points at a given coord in a hash map
    - For every 2 points with both different coord:
        - Check if they can make a rectangle (as top left and bottom right corners) -> point 1 is strictly above and to the left
            -> check if the points to the top right and bottom left exist
    - Take Multiplicity into account
        -> multiply by the nb of points with the given coordinate


    Complexity:
    - O(n^2) time, O(n) space

    Test case:
    [(0, 0) (2, 0) (0, 1) (2 1) (0 0) (0 3)] -> 2
    """
    # 1. Count the points
    nb_points: dict[tuple[int, int], int] = defaultdict(lambda: 0)
    for x, y in points:
        nb_points[x, y] += 1

    # 2. Count rectangles
    res = 0

    unique_points = list(nb_points.keys())
    for p1 in unique_points:
        for p2 in unique_points:
            x1, y1 = p1
            x2, y2 = p2
            # Check if they can be opposite corners of a rectangle
            if x1 >= x2 or y1 <= y2:
                continue

            p3 = (x1, y2)
            p4 = (x2, y1)

            res += nb_points[p1] * nb_points[p2] * nb_points[p3] * nb_points[p4]

    return res

# WIP
def count_rectangles_2(points: list[tuple[int, int]]) -> int:
    """
    Given a list of points on a 2d plan, count the nb of rectangles (4 sides of area > 0, opposite sides equal) not necessarily parallel to the x axis.

    Inputs: list[tuple[int,int]]: [(1, 1) (2, 2) (3 2) (1 5) (-1 2)]
    Outputs: int: 0,1,2,3,..
    Edge cases:
    - duplicate points
    - empty points/single point
    - no rectangle
    Assumptions:
    - only integer coordinates


    .   1   .
    1   .   1
    2   1   1
    3 rectangles + 1



    Duplicates points:
    - Count the nb of points at a given coord + take it into account when considering this coord
    Counting each rectangle only once:
    - TODO


    Solution:
    - Count the nb of points at a given coord in a hash map
    - For every 2 points not necessarily different coordinates:
        - Check if they can make a rectangle (as top left and bottom right corners) -> point 1 is strictly above and to the left
            -> we need 2 points at equal distance from the center of the first 2 points
            -> If we consider 2 points on the same side instead of in diagonal: we look at other pairs of points with the same distance, the same angle compared to the x axis and with a right angle between 3 points
            -> with diagonal, we need 2 diags equal diags (parallelogram) + 1 rect angle (rectangle) I believe
    - Take Multiplicity into account
        -> multiply by the nb of points with the given coordinate


    Complexity:
    - O(n^2) time, O(n) space

    Test case:
    [(0, 0) (2, 0) (0, 1) (2 1) (0 0) (0 3)] -> 2
    """
    # 1. Count the points
    nb_points: dict[tuple[int, int], int] = defaultdict(lambda: 0)
    for x, y in points:
        nb_points[x, y] += 1

    # 2. Count rectangles
    res = 0

    unique_points = list(nb_points.keys())
    for p1 in unique_points:
        for p2 in unique_points:
            x1, y1 = p1
            x2, y2 = p2
            # Check if they can be opposite corners of a rectangle
            if x1 >= x2 or y1 <= y2:
                continue

            p3 = (x1, y2)
            p4 = (x2, y1)

            res += nb_points[p1] * nb_points[p2] * nb_points[p3] * nb_points[p4]

    return res




def test_empty_list():
    assert count_rectangles([]) == 0


def test_single_point():
    assert count_rectangles([(1, 1)]) == 0


def test_two_points():
    assert count_rectangles([(0, 0), (1, 1)]) == 0


def test_four_points_form_rectangle():
    points = [(0, 0), (0, 1), (1, 0), (1, 1)]
    assert count_rectangles(points) == 1


def test_three_columns_two_rows():
    points = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
    assert count_rectangles(points) == 3


def test_duplicate_points():
    points = [(0, 0)] * 2 + [(0, 1)] * 2 + [(1, 0)] * 2 + [(1, 1)] * 2
    # Each corner has 2 points, so 2^4 = 16 combinations
    assert count_rectangles(points) == 16


def test_sample_input():
    points = [(1, 1), (2, 2), (3, 2), (1, 5), (-1, 2)]
    assert count_rectangles(points) == 0


def test_rectangle_with_1_duplicate():
    points = [(0, 0), (2, 0), (0, 1), (2, 1), (0, 0), (0, 3)]
    assert count_rectangles(points) == 2
