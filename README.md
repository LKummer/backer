# Backer

File archving command line utility.

## Development Guide

Make sure to install the dependencies before development.

```
$ poetry install
```

### Running

Run the Backer CLI:

```
$ poetry run backer
```

### Testing

Run the unit tests:

```
$ inv test
```

### Linting

Lint the backer module files:

```
$ inv lint
```

Lint the tests:

```
$ inv lint -t
```

### Formatting

Format all source files:

```
$ inv format
```

## Style Guide

Please follow the style guide when contributing.

### Commit Messages

Start the message with a verb in present form, for example; add, fix, improve,
refactor.

Limit the first line to 50 characters, as it is the subject line Github will
truncate it when viewing the log.

Leave a blank line between the subject line and the text body if a text body is
used.

Write concisely and accurately.

### Docstrings

Follow the
[Google Napoleon docstring style.](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

The docstrings are written in Markdown.

### Testing

Tests reside in the `/tests` folder. Test file names follow the pattern
`test_*.py`.

Tests are to be grouped by classes.

Example unit test:

``` py
class TestSomething
    """Tests for something."""
    def test_one_thing(self):
        """Ensure one thing works."""
        assert True
    def test_another_thing(self):
        """Ensure another thing works."""
        assert True
```

### Linting and Formatting

Make sure to run the linter and formatter before pushing.

Later on a CI pipeline will be configured to force this step.
