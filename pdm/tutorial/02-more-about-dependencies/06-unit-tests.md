# Unit tests

An essential part of writing robust software is testing it, preferably with an automated test suite.
The typical way of doing this in Python these days is with [pytest](https://docs.pytest.org/en/stable/).
With pytest, we can create simple tests that use assertions to check if the code behaves as it should.
For example, we created a test for the API wrapper that you can copy.
It checks that `get_future_sessions` gets all future sessions:

```python
import packaging_tutorial.pycon as pycon
from datetime import datetime, timedelta


def test_get_future_sessions() -> None:
    now = datetime.fromisoformat("20250512T12:00Z")
    past_sessions = [
        pycon.Session(start=now - timedelta(hours=2)),
        pycon.Session(start=now - timedelta(hours=1)),
        pycon.Session(start=now - timedelta(hours=22)),
    ]
    future_sessions = [
        pycon.Session(start=now + timedelta(hours=1)),
        pycon.Session(start=now + timedelta(hours=21)),
    ]
    sessions = past_sessions + future_sessions

    assert list(pycon.get_future_sessions(sessions, now=now)) == future_sessions
```

We will not go into details on testing in this tutorial, but if you're interested, then Ned Batchelder  (who, among other things, maintains [coverage.py](https://coverage.readthedocs.io/)) had a presentation about testing with the [materials online](https://nedbatchelder.com/text/test3.html) and we've heard good things about Brian Okken's [tutorials](https://courses.pythontest.com).
Still, we will need some tests to get through the entire packaging process.

## Exercises
1. There should be a folder `tests/` in your project root (i.e. not in the `src` or `src/{package_name}` folder) that contains a `__init__.py`-file. Discuss with your neighbour: What do you think this folder should contain? and why is it not inside the `src/{package_name}` directory?
2. Add a `test_pycon.py`-file to the `tests/`-directory and populate it with the test above (you may need to update the import).
3. Add pytest as a dependency to your project using whichever method you prefer.
4. Run pytest by running `pdm run pytest`.

<img src="../../../assets/post_it_yellow.svg" alt="Illustration of a pink post it note" width="50px" />

## Reflection
We have now added our first test to our package.
To do that, we first created a `tests`-folder with a `__init__.py` file in it.
By including this file, we make it possible to do relative imports in the tests (we're not doing that here, but it's good practice to include it).
Also, we kept the tests separated from the rest of our source code for several reasons.
First, we don't want the tests to be importable from our module.
They are not runnable -- they just contain simple assertions and require pytest to run, so it would be kind of strange to make the tests importable (but it's not unheard of to bundle them with the code either, especially if you're using other test frameworks).

Also, the tests may require dependencies that the package doesn't need, such as pytest.
We need pytest to run the tests, but not to use our library.
Isn't it then kind of odd to add pytest as a dependency, when it's only required for the tests?
It is, and instead of using a normal dependency, we should use *optional dependencies* or *development dependencies*.

## Next up
[Optional dependencies and package extras](./07-package-extras.md)
