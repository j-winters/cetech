# Is the cultural evolution of technology cumulative or combinatorial?

# fidelitycombo
This repository contains data and code from [Winters (2020)](https://repo). It includes the Python code used for running the model, the data generated for Winters (2020), and the R code used for producing the graphs.

The top-level folder structure is as follows:

* `analysis/`: Contains R code for producing all graphs in the paper.
* `data/`:  All data generated for Winters (2020) in `.csv` formats.
* `model/`: The ABM used for generating the data. Requires Python 3 with [NumPy](https://numpy.org/) and [Editdistance](https://github.com/aflc/editdistance) packages installed.

## Running the model
The actual simulation runs reported in the paper were parallelized using the [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) package.

Below is a simple version of the model for performing a single run:
```python
>>> import model *
>>> simulation(directory=True,run=0,n=100,generations=1000,tradeoff=0.5,e=0.05,combine=True)
```
The parameters correponds to the following:
* `directory`: If `directory=True`, a single simulation will run and output a `.csv` in the current directory of model.py, else if `directory=False` then the output will print in your console.
* `run`: The specific simulation run.
* `n`: Number of individuals in a population. The default is `n=100`.
* `generations`: Number of generations for a given run. The default is `generations=1000`.
* `tradeoff`: Proportion with which individuals either optimize or repurpose. The default is `tradeoff=0.5`.  
* `e`: The level of transmission error. This parameter takes a range of values from `0` to `1`. The default is `e=0.05`.
* `combine`: Whether the ability to combine existing solutions is present (`True`) or absent (`False`). The default is `combine=True`.

## References
Winters, J. (2020). Re-evaluating transmission fidelity and combinatorial innovation as drivers of technological evolution. Repo. [Doi]()

License
-------

Except where otherwise noted, this repository is licensed under a Creative Commons Attribution 4.0 license. You are free to share and adapt the material for any purpose, even commercially, as long as you give appropriate credit, provide a link to the license, and indicate if changes were made. See LICENSE.md for full details.


