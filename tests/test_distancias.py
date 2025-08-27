from nombre_proyecto.utils.distancias import manhattan, euclidea

def test_manhattan():
    assert manhattan((0,0),(3,4)) == 7

def test_euclidea():
    assert euclidea((0,0),(3,4)) == 5.0
