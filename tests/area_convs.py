import numpy as np

def m2_km2(area_m2):
    return area_m2/1e6

def test_m2_km2():
    in_out_expected = {
        1: 1e-6,
        1e6: 1,
        0: 0,
    }
    in_out_actual = dict()

    for val in in_out_expected:
        actual_retail_price = m2_km2(val)
        in_out_actual[val] = actual_retail_price
    
    assert in_out_actual == in_out_expected
    
