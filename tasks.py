from invoke import task


@task
def test(c):
    c.run("pytest")


@task
def lint(c, tests=False):
    if tests:
        # When linting the tests, these rules are disabled:
        #   W0621 - Redefining names, because of Pytest fixtures.
        #   R0201 - No self use, to group tests in classes.
        c.run("pylint tests -d W0621,R0201")
    else:
        c.run("pydocstyle backer --convention=google")
        c.run("pylint backer")


@task
def format(c):
    c.run("black backer tests tasks.py")
