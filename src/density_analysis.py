"""
Plot the predicted and measured densities of neat liquids.  Simulations were
performed using an automated pipeline, while experimental data was
munged using the ThermoML IUPAC standard XML schema.
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


expt = pd.read_csv("./tables/data_with_metadata.csv")
expt["temperature"] = expt["Temperature, K"]

pred = pd.read_csv("./tables/predictions.csv")

expt = expt.set_index(["cas", "temperature"])
pred = pred.set_index(["cas", "temperature"])

pred["expt_density"] = expt["Mass density, kg/m3"]
pred["expt_density_std"] = expt["Mass density, kg/m3_uncertainty_bestguess"]

for (formula, grp) in pred.groupby("formula"):
    x, y = grp["density"], grp["expt_density"]
    xerr = grp["density_sigma"]
    yerr = grp["expt_density_std"].replace(np.nan, 0.0)
    plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='o', label=formula)

plt.plot([600, 1400], [600, 1400], 'k')
plt.xlim((600, 1400))
plt.ylim((600, 1400))
plt.xlabel("Predicted (GAFF)")
plt.ylabel("Experiment (ThermoML)")
plt.gca().set_aspect('equal', adjustable='box')
plt.draw()
x, y = pred["density"], pred["expt_density"]
relative_rms = (((x - y) / x)**2).mean()** 0.5
plt.title("Density [kg / m^3] (relative rms: %.3f)" % (relative_rms))
