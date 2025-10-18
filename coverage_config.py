# pyright: ignore[reportUnusedExpression, reportUndefinedVariable]  # noqa: F821

run = {
    "branch": True,
    "omit": [
        "venv/*",
        "manage.py",
        "*/core/*",
        "*/migrations/*",
        "*/__init__.py",
        "*/admin.py",
        "run_coverage.py",
        "coverage_config.py",
    ],
}
