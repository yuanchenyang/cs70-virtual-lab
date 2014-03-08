CS70 Virtual Lab
================

Dependencies
-------------
 - pypy (For faster data generation)
 - numpy, scipy, matplotlib (For plotting)

How to run
-------------
To create the all plots, run:
```
make
```

To create the plot for a specific part (for example part a), run:
```
make part_a.pdf
```

To clean all generated files, run:
```
make clean
```

How it works
-------------
questions.py generates the data, and writes it into data.pkl. 

plot.py reads the data and plots it.