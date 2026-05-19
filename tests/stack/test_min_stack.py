from src.stack.min_stack import MinStack

stack = MinStack()


def test_push_and_top():
    stack.push(1)
    stack.push(2)

    assert stack.top() == 2


def test_get_min():
    stack.push(0)

    assert stack.getMin() == 0


def test_pop():
    stack.pop()

    assert stack.top() == 2


def test_get_min_after_pop():
    assert stack.getMin() == 1


def test_negative_numbers():
    stack.push(-5)
    stack.push(-10)

    assert stack.getMin() == -10


def test_top_after_multiple_pushes():
    stack.push(50)

    assert stack.top() == 50