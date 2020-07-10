from terminus import Pipeline


def test_pipeline():
    """
    Test the correct execution of our pipeline
    By adding 2 generators `doubles()` and `upper()`
    What we expect is a call like this `upper(doubles([1, 5, 10]))`
    """

    def doubles(data):
        for i in data:
            yield i * 2

    def upper(data):
        for i in data:
            yield i + 1

    pipeline = Pipeline()
    pipeline.add_step(doubles)
    pipeline.add_step(upper)
    result = pipeline.run([1, 5, 10])
    assert list(result) == [3, 11, 21]
