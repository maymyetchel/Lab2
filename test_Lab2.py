import Lab2

def test_calc_min_max_temperature():
    print("Test_calc_min_max_temperature")
    #arrange
    result = []
    input_list = [5, 67, 32, 15, 89, 23, 41]
    expected_result = [5, 89]
    #act
    result = Lab2.calc_min_max_temperature(input_list)
    #assert 
    assert result == expected_result


def test_calc_average_temperature():
    #arrange
    result = 0
    input_list = [10, 20, 30, 40, 50]
    expected_result = 30.0
    #act
    result = Lab2.calc_average_temperature(input_list)
    #assert
    assert result == expected_result


def test_calc_median_temperature():
    #arrange
    result = 0
    #test
    input_list = [5, 15, 25, 35, 45]
    expected_result = 25
    #act 
    result = Lab2.calc_median_temperature(input_list)
    #asssert 
    assert result == expected_result