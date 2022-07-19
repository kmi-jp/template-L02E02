import pytest

@pytest.fixture
def output():
    return """1
-2
5
20
0
2
3
400
100
2
3
4
"""

def test_output(script_runner, output):
    ret = script_runner.run("matrix_print.py")

    assert ret.success
    assert output == ret.stdout
    assert ret.stderr == ""
