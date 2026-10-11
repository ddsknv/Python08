import sys
import importlib.util
from importlib.metadata import version, PackageNotFoundError

print("\nLOADING STATUS: Loading programs...\n")
print("Checking dependencies:")

def get_library_version(library_name: str) -> str:
    try:
        return version(library_name)
    except PackageNotFoundError:
        return "Not installed"

def check_library(library_name: str) -> bool:
    spec = importlib.util.find_spec(library_name)
    descriptions: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
    }
    if spec is not None:

        library_version = get_library_version(library_name)
        print(f"[OK] {library_name} {library_version} - {descriptions[library_name]}")
        return True
    else:
        print(f"[MISSING] {library_name} not found")
        return False

numpy_ok = check_library("numpy")
pandas_ok = check_library("pandas")
matplotlib_ok = check_library("matplotlib")

if not numpy_ok or not pandas_ok or not matplotlib_ok:
    print("Cannot continue: required libraries are missing")
    sys.exit()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("\nAnalyzing Matrix data...")
print("Processing 1000 data points...\n")
energy_levels = np.random.randint(0, 101, 1000)


df = pd.DataFrame(energy_levels, columns = ["energy"])
print(df.head())
average_energy = df["energy"].mean()
print(f"Average energy: {average_energy}")
min_energy = df["energy"].min()
max_energy = df["energy"].max()
print(f"Minimum energy: {min_energy}")
print(f"Maximum energy: {max_energy}\n")
print(f"Generating visualization...\n")

plt.plot(energy_levels)
plt.title("Matrix Energy Levels")
plt.xlabel("Observation")
plt.ylabel("Energy Level")
print("Analysis complete!")
plt.savefig("matrix_analysis.png")
print("Results saved to: matrix_analysis.png")
plt.close()

# with open("requirements.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         line = line.strip()
#         parts = line.split("==")
#         if len(parts) != 2:
#             print("Error: invalid line")
#             continue
#         required_version = parts[1]
#         library_name = parts[0]
#         installed_version = get_library_version(library_name)
#         print(f"{library_name}: required={required_version}, installed={installed_version}")
#         if installed_version == required_version:
#             print("Version matches")
#         else:
#             print("Version mismatch")
