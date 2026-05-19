from stack.car_fleet import Solution

sol = Solution()

def test_basic_one_fleet():
    assert sol.carFleet(10, [1, 4], [3, 2]) == 1

def test_multiple_fleets():
    assert sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3

def test_two_fleets():
    assert sol.carFleet(12, [10, 8, 3], [1, 2, 3]) == 2

def test_single_car():
    assert sol.carFleet(10, [3], [3]) == 1

def test_no_catch():
    assert sol.carFleet(10, [6, 8], [3, 2]) == 2