# Kidney Pairing Optimization Project

This repository contains a Python implementation of a kidney paired donation optimization model using Gurobi Optimizer.

## Files

proj.py: The main Python script that implements the KPD optimization model using Gurobi and processes the input data.
The_Match_Team.json: Input data file containing patient-donor compatibility information, including blood types and potential matches.

## How It Works

Input Data: The input data is provided in a JSON file format and includes details about patients and donors, including their blood types and compatibility information.
Optimization Model:
Uses Gurobi to solve a matching problem that maximizes the number of transplants.
Considers constraints like blood type compatibility and the feasibility of pairing.
Output: The solver provides the number of successful matches along with detailed results, such as the number of matches by blood type.

## How to Run

1. Install Python dependencies (`networkx`, `matplotlib`, `gurobipy`).
2. Use a Python 3.x environment to execute `proj.py`.
3. Ensure the `The_Match_Team.json` file is in the same directory as `proj.py`.

## Dependencies

- Python 
- Gurobi Optimizer
- NetworkX
- Matplotlib

## Future Work

Incorporating additional constraints such as geographic proximity or medical urgency.
Extending the model to handle larger datasets efficiently.
Adding visualizations for match results.
