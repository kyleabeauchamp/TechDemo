% title: Tech Demo
% author: Kyle A. Beauchamp

---
title: Molecular dynamics as Data Science
subtitle:  Predict physical properties, learn interesting biology

<center>
<video id="sampleMovie" src="movies/shaw-dasatanib-2.mov" loop=\"true\ autoPlay=\"true\  width="512" height="384"></video>
</center>

<footer class="source">
Movie Credit: DE Shaw Research
</footer>

---
title: MSMBuilder: Design

<div style="float:right; margin-top:-100px">
<img src="figures/flow-chart.png" height="600">
</div>

Builds on [scikit-learn](http://scikit-learn.org/stable/) idioms:

- Everything is a `Model`.
- Models are `fit()` on data.
- Models learn `attributes_`.
- `Pipeline()` concatenate models.
- Use best-practices (cross-validation)


---
title: Data capture at NIST: ThermoML


<center>
<img height=540 src="figures/pipeline.png"/>
</center>
