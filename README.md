# The Stochastic Fly

*From Detailed Balance to Irreversible Dynamics*

A study of whether spontaneous fluctuations predict the response to weak fields in a stochastic neural network constrained by MaleCNS. The static article under `site/` contains the theoretical foundations, related work and the research question. It uses plain HTML, CSS and JavaScript.

## Local preview

From this repository, serve the article with Python's standard library.

```powershell
python -m http.server 8765 --bind 127.0.0.1 --directory site
```

Open [the local article](http://127.0.0.1:8765/). The figure and illustration are bundled with the page.

## Anatomy figure

Figure 1 uses the SWC trace sample and cell locations from the previous project's MaleCNS v1.0 exports. It highlights an example visual pathway. The LPLC2 traces and DNp01 positions are anatomical annotations.

To regenerate the figure, run `python scripts/render_anatomy.py` with NumPy and Matplotlib installed. The script defaults to the exports in the sibling `repo_malecns_legacy` checkout. Pass the export folder as a positional argument to use another location. The source exports and original MaleCNS data remain in the legacy checkout.

Data source: [MaleCNS v1.0, FlyEM and collaborators](https://male-cns.janelia.org/download/).
