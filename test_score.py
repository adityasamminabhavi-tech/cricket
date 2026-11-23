from score import run_rate, strike_rate, required_rate

def test_run_rate_case1():
    assert run_rate(120, 20) == 6.0

def test_run_rate_case2():
    assert run_rate(90, 15) == 6.0

def test_strike_rate_case1():
    assert strike_rate(50, 25) == 200.0

def test_strike_rate_case2():
    assert strike_rate(45, 30) == 150.0

def test_required_rate_case1():
    assert required_rate(200, 120, 10) == 8.0

def test_required_rate_case2():
    assert required_rate(250, 150, 20) == 5.0