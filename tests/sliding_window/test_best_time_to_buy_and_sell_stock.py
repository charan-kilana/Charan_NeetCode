from sliding_window.best_time_to_buy_and_sell_stock import Solution

sol = Solution()

def test_basic_profit():
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5

def test_no_profit():
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0

def test_two_days_profit():
    assert sol.maxProfit([1, 5]) == 4

def test_two_days_no_profit():
    assert sol.maxProfit([5, 1]) == 0

def test_same_prices():
    assert sol.maxProfit([3, 3, 3, 3]) == 0

def test_profit_at_end():
    assert sol.maxProfit([2, 4, 1, 10]) == 9