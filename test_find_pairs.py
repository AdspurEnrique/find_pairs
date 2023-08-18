from finds_pairs import find_pairs

def test_find_pairs():
    assert find_pairs([1, 9, 5, 0, 20, -4, 12, 16, 7], 12) == [(5, 7), (12, 0), (16, -4)]
    assert find_pairs([1, 2, 3, 4, 5], 9) == [(4, 5)]
    assert find_pairs([], 10) == []
    assert find_pairs([10], 10) == []
    assert find_pairs([10, -10], 0) == [(-10, 10)]
    assert find_pairs([5, 7, 2, 4], 9) == [(5, 4), (7, 2)]
    
test_find_pairs()
