#plugin-pytest-xdist
pytest -m timed -v -n=16

#plugin-pytest-html run report
pytest -m timed -v --html=report.html
