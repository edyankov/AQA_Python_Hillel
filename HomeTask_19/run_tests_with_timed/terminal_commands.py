#plugin-pytest-xdist
pytest -m timed -v -n=12

#plugin-pytest-html run report
pytest -m timed -v --html=report.html
