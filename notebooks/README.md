# Research notebooks

Each assignment combines study notes, a runnable setup, and exercises. Keep the assignment prompts when submitting your work so the code and written answers can be reviewed together.

| Notebook | Focus |
| --- | --- |
| [01 · From MaleCNS to detailed balance](assignments/01_from_malecns_to_detailed_balance.ipynb) | Build effective weights from contact counts and verify reversibility exactly on a small network. |
| [02 · Can spontaneous fluctuations predict a response?](assignments/02_fluctuations_and_step_response.ipynb) | Reuse the completed first assignment to compare exact step responses with the equilibrium prediction from spontaneous covariance. |

The [professional notebooks](professional/) will hold reviewed implementations and research figures.

## Local setup

From the repository root, use one Python environment. If `.venv` already exists, start at the second command.

```powershell
uv venv .venv --python 3.11
uv pip install --python .venv/Scripts/python.exe -r notebooks/requirements.txt
```

Open the notebook in VS Code or another Jupyter-compatible editor and select `.venv/Scripts/python.exe` as the kernel. Place the following files from the [MaleCNS v1.0 release](https://male-cns.janelia.org/download/) in the repository's `data/` directory.

- `body-annotations-male-cns-v1.0-minconf-0.5.feather`
- `body-neurotransmitters-male-cns-v1.0.feather`
- `connectome-weights-male-cns-v1.0-minconf-0.5.feather`

The setup can also use the same files from a sibling `repo_malecns_legacy/data` directory. For another location, set `MALECNS_DATA_DIR` or change `DATA_DIR_OVERRIDE` in Notebook 01.
