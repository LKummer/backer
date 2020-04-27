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
        #   R0903 - Too few public methods.
        c.run("pylint tests -d W0621,R0201,R0903")
    else:
        c.run("pydocstyle backer --convention=google")
        # When linting, these rules are disabled:
        #   W1202 - Use % formatting in logging functions, to use f strings for
        #           logging.
        #   R0903 - Too few public methods.
        c.run("pylint backer -d R0903,W1202")


@task
def format(c):
    c.run("black backer tests tasks.py")
