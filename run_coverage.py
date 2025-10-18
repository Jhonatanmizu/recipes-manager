import coverage
import pytest

from coverage_config import run


def main():
    cov = coverage.Coverage(**run)
    cov.start()

    # Run pytest (returns 0 if tests pass)
    exit_code = pytest.main(["-v", "--disable-warnings"])

    cov.stop()
    cov.save()
    cov.report(show_missing=True)
    cov.html_report(directory="htmlcov")

    exit(exit_code)


if __name__ == "__main__":
    main()
