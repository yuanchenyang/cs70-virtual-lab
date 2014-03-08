PYTHON = python
PYPY = pypy

all: data.pkl
	$(PYTHON) plot.py

data.pkl: questions.py
	$(PYPY) questions.py

part_%.pdf: plot.py questions.py
	$(PYPY) questions.py part_$*
	$(PYTHON) plot.py part_$*

clean:
	$(RM) part_*.pdf *~ data.pkl *.pyc
