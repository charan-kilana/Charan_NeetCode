from stack.daily_temperatures import Solution

sol = Solution()

def test_basic():
    assert sol.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]

def test_increasing():
    assert sol.dailyTemperatures([30,40,50,60]) == [1,1,1,0]

def test_decreasing():
    assert sol.dailyTemperatures([60,50,40,30]) == [0,0,0,0]

def test_same_temperature():
    assert sol.dailyTemperatures([70,70,70]) == [0,0,0]

def test_single_day():
    assert sol.dailyTemperatures([80]) == [0]