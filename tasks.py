from invoke import task


@task
def test(c):
    c.run("pytest")


@task
def lint(c, tests=False):
    if tests:
        # When linting the tests, these rules are disabled:
        #   W0621 - Redefining names, because of Pytest fixtures.
        #   C0116 - Function docstring.
        c.run("pylint tests -d W0621,C0116")
    else:
        c.run("pydocstyle backer --convention=google")
        c.run("pylint backer")


@task
def format(c):
    c.run("black backer tests tasks.py")
