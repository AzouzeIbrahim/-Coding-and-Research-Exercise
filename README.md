# NumPy Development Activity Analysis

This repository contains data, scripts, and visualizations for analyzing the evolution of development activity in the NumPy project from 2001 to 2025.

## 📊 Research Question

**RQ1:** How does development activity evolve over time?

Analyze how monthly commit counts and code churn (lines added/removed) fluctuate across the project's lifetime, identifying long-term trends and notable spikes.

## 📁 Repository Structure
```
.
├── commit_visualizations/        # Visualizations for commit analysis
├── code_churn_visualizations/    # Visualizations for code churn analysis
├── scripts/                      # Data extraction scripts
│   ├── commits.py
│   └── code_churn.py
├── data/                         # Generated CSV files
│   ├── monthly_commits.csv
│   ├── yearly_commits.csv
│   ├── monthly_code_churn.csv
│   └── yearly_code_churn.csv
└── README.md
```

## 🔧 Scripts

### 1. commits.py

Extracts commit data from the NumPy repository using PyDriller.

**What it does:**
- Traverses all commits in the NumPy repository
- Counts commits per month and per year
- Generates `monthly_commits.csv` and `yearly_commits.csv`

**Usage:**
```bash
python scripts/commits.py
```

### 2. code_churn.py

Extracts code churn data (lines added/deleted) from the NumPy repository.

**What it does:**
- Traverses all commits in the NumPy repository
- Calculates lines added and deleted per modified file
- Aggregates churn metrics by month and year
- Generates `monthly_code_churn.csv` and `yearly_code_churn.csv`

**Usage:**
```bash
python scripts/code_churn.py
```

**Dependencies:**
```bash
pip install pydriller
```

**Note:** Both scripts may take several hours to complete as they analyze the entire NumPy repository history.

## 🛠️ Tools and Technologies

- **PyDriller:** Python framework for mining Git repositories
- **Python 3.x:** Primary programming language
- **CSV format:** Data storage for portability and analysis
- **Google Sheets:** Data visualization and chart generation
- **NumPy Repository:** Data source (https://github.com/numpy/numpy)
