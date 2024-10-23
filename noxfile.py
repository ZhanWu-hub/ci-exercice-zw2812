import nox


@nox.session
def tests(session):
    """Run the test suite."""
    session.install(".[tests]")
    session.run("pytest")

@nox.session
def docs(session):
    """Build the documentation."""
    session.install(".[docs]")
    session.run("sphinx-build", "docs", "docs/_build")
    # Optionally open the docs in a browser
    session.run("python", "-m", "webbrowser", "docs/_build/html/index.html")

