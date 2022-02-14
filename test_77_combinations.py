import code_77_combinations as c

def test_example_1():
    s = c.Solution()
    assert s.combine(4, 2) == sorted([
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
])

def test_example_2():
    s = c.Solution()
    assert s.combine(1,1) == [[1]]