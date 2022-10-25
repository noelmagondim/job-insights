from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    word = "PyThOn"
    assert (count_ocurrences(path, word) == 1639)
