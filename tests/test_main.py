from template_on_pr.main import myfunc


def test_myfunc():
    assert myfunc() == "Hello World!"
