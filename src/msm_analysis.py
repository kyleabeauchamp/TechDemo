"""
Extract biologically relevant states from alanine dipeptide data.
"""
import seaborn as sns
import pandas as pd
from msmbuilder import example_datasets, cluster, msm, featurizer, lumping
from sklearn.pipeline import make_pipeline

sns.set(style="white")

# Load an example dataset from the cloud
dataset = example_datasets.alanine_dipeptide.fetch_alanine_dipeptide()  # From Figshare!
trajectories = [t[::50] for t in dataset["trajectories"]]  # List of MDTraj Trajectory Objects

# Instantiate the objects in our data analysis pipeline
clusterer = cluster.MiniBatchKMedoids(n_clusters=50, metric="rmsd")
msm_model = msm.MarkovStateModel()
lumper = lumping.PCCA(n_macrostates=2)

# Build the pipeline from the individual steps and fit the model with our data
pipeline = make_pipeline(clusterer, msm_model, lumper)
labels = pipeline.fit_transform(trajectories)



# Extract some features: dihedral angles and state labels
dih_featurizer = featurizer.DihedralFeaturizer(["phi", "psi"], sincos=False)
X = dih_featurizer.transform(trajectories)
phi, psi = np.rad2deg(np.concatenate(X).T)
flat_labels = np.concatenate(labels)


# Move data into pandas for exploring with seaborn
data = pd.DataFrame(dict(phi=phi, psi=psi, state=flat_labels))
data.state = data.state.apply(lambda x: {0:"A", 1:"B"}[x])

g = sns.PairGrid(data, diag_sharey=False, hue="state")
g.map_lower(plt.scatter)
g.map_diag(plt.hist, lw=3)
g.set(xlim=(-180, 180), ylim=(-180, 180));
