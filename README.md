<p align="center">
  <a href="https://mich1803.github.io/the-stochastic-fly/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/masthead-dark.svg">
      <img src="site/assets/mosca_halftone_panoramica.svg" alt="A fruit fly between two flight trails" width="640">
    </picture>
  </a>
</p>

<h1 align="center">The Stochastic Fly</h1>
<p align="center"><em>From Detailed Balance to Irreversible Dynamics</em></p>
<p align="center">
  <a href="https://mich1803.github.io/the-stochastic-fly/"><strong>Read the paper</strong></a>
  ·
  <a href="./notebooks/">Open the research notebooks</a>
</p>

Can spontaneous fluctuations in a neural network predict how it responds to a weak stimulus? The Stochastic Fly studies this question in a binary stochastic model constrained by the MaleCNS fruit fly connectome. A symmetric coupling matrix provides an equilibrium reference. Restoring the antisymmetric part lets us test how the accuracy of the fluctuation–response prediction changes in the directed model.

Michele Magrini · Mathematical Models for Neural Networks · Sapienza University of Rome

## Research notebooks

| Notebook | Exercise |
| --- | --- |
| [01 · From MaleCNS to detailed balance](notebooks/assignments/01_from_malecns_to_detailed_balance.ipynb) | Build signed couplings from contact counts, solve the finite-state dynamics, and compare stationary currents and cycle affinities. |
| [02 · Can spontaneous fluctuations predict a response?](notebooks/assignments/02_fluctuations_and_step_response.ipynb) | Compare an exact response to a weak field with the prediction from resting covariance. |

The first notebook includes a completed three-cell validation. The second contains a runnable setup and open exercises. Both use exact finite-state calculations to establish a reference for later trajectory-based experiments on larger circuits. See the [notebook setup](notebooks/README.md) for dependencies and data files.

## Local preview

From the repository root, serve the paper with Python and open the [local preview](http://127.0.0.1:8765/).

```powershell
python -m http.server 8765 --bind 127.0.0.1 --directory site
```

The site is plain HTML, CSS and JavaScript. The Pages workflow publishes [`site/`](site/) on updates to `main`.

## Data and figures

- The [MaleCNS v1.0 release](https://male-cns.janelia.org/download/) provides contact counts, annotations, transmitter predictions, and skeletons. See [Berg et al. (2026)](https://doi.org/10.1016/j.cell.2026.08.015) for the acquisition and reconstruction methods.
- Figure 3 uses MaleCNS skeletons and cell positions to illustrate the LPLC2 and DNp01 populations. [`scripts/render_anatomy.py`](scripts/render_anatomy.py) regenerates it from the morphology exports using NumPy and Matplotlib. Pass the folder containing `anatomy.json` and `full-cns.json` as its positional argument.
- Figure 1 is an illustrative micrograph. Figure 2 shows the public Stonkfly and Doomfly interfaces. The composite images were supplied with the draft. Original image credits and reuse terms remain to be verified.
