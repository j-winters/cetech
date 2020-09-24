# Is the cultural evolution of technology cumulative or combinatorial?

This repository contains data and code from [Winters (2020)](https://repo). It includes the Python code used for running the model, the data generated for Winters (2020), and the R code used for producing the graphs.

The top-level folder structure is as follows:

* `analysis/`: Contains R code for producing all graphs in the paper.
* `data/`:  All data generated for Winters (2020) in `.csv` formats.
* `model/`: The ABM used for generating the data. Requires Python 3 with [NumPy](https://numpy.org/) and [Editdistance](https://github.com/aflc/editdistance) packages installed.

## Running the model
The actual simulation runs reported in the paper were parallelized using the [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) package.

Below is a simple version of the model for performing a single run:
```python
>>> import ABM *
>>> simulation(run=0,n=100,generations=2000,TS=10,local=True,combine=True,loss=0.5)
```
The parameters correponds to the following:
* `run`: The specific simulation run. The default is `run=0`.
* `n`: Number of individuals in a population. The default is `n=100`.
* `generations`: Number of generations for a given run. The default is `generations=2000`.
* `TS`: Number of timesteps per generation. The default is `TS=10`.
* `local`: Whether the ability to perform single-edit modifications to existing solutions is present (`True`) or absent (`False`). The default is `local=True`.
* `combine`: Whether the ability to combine existing solutions is present (`True`) or absent (`False`). The default is `combine=True`.
* `loss`: The level of information loss. This parameter takes a range of values from `0` to `1`. The default is `loss=0.5`.

## References
Winters, J. (2020). Is the cultural evolution of technology cumulative or combinatorial? Repo. [Doi]()

License
-------

Except where otherwise noted, this repository is licensed under a Creative Commons Attribution 4.0 license. You are free to share and adapt the material for any purpose, even commercially, as long as you give appropriate credit, provide a link to the license, and indicate if changes were made. See LICENSE.md for full details.


