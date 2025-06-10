"""
Test script to verify alumath functionality
"""
from alumath import Matrix, create_matrix, identity_matrix

def test_basic_multiplication():
    # Test case 1: Basic 2x2 multiplication
    m1 = create_matrix([[1, 2], [3, 4]])
    m2 = create_matrix([[5, 6], [7, 8]])
    result = m1 * m2
    expected = [[19, 22], [43, 50]]
    assert result.to_list() == expected
    print("✓ Basic 2x2 multiplication passed")

def test_different_dimensions():
    # Test case 2: Different dimensions
    m1 = create_matrix([[1, 2, 3]])  # 1x3
    m2 = create_matrix([[4], [5], [6]])  # 3x1
    result = m1 * m2  # Should be 1x1
    expected = [[32]]
    assert result.to_list() == expected
    print("✓ Different dimensions multiplication passed")

def test_identity_multiplication():
    # Test case 3: Identity matrix
    m1 = create_matrix([[1, 2], [3, 4]])
    identity = identity_matrix(2)
    result = m1 * identity
    assert result.to_list() == m1.to_list()
    print("✓ Identity multiplication passed")

if __name__ == "__main__":
    test_basic_multiplication()
    test_different_dimensions()
    test_identity_multiplication()
    print("All tests passed! ✓")