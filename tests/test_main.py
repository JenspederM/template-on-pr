from template_on_pr.main import myfunc, pr_func


def test_myfunc():
    assert myfunc() == "Hello World!"


def test_pr_func():
    assert pr_func() == "This is a function that will be called on PRs"
