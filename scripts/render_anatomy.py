"""Render the anatomical example from the legacy MaleCNS exports."""

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
BACKGROUND = "#090e14"
COLORS = {"context": "#8999aa", "LPLC2": "#82baff", "DNp01": "#f6c77d"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "exports",
        nargs="?",
        type=Path,
        default=ROOT.parent / "repo_malecns_legacy" / "explorer" / "data",
        help="Folder containing anatomy.json and full-cns.json",
    )
    source = parser.parse_args().exports
    anatomy = json.loads((source / "anatomy.json").read_text(encoding="utf-8"))
    bundle = json.loads((source / "full-cns.json").read_text(encoding="utf-8"))
    body_types = {node[0]: node[1] for node in bundle["nodes"]}
    scale = anatomy["scale"]

    traces = {"context": [], "LPLC2": []}
    for body_id, _, _, coordinates in anatomy["skeletons"]:
        cell_type = body_types[body_id]
        group = "LPLC2" if cell_type == "LPLC2" else "context"
        traces[group].append(np.asarray(coordinates).reshape(-1, 2, 2))
    readout = np.array([node[5][:2] for node in bundle["nodes"] if node[1] == "DNp01"])
    if len(traces["LPLC2"]) != 60 or len(readout) != 2:
        raise ValueError("The anatomy and caption require 60 LPLC2 traces and two DNp01 positions.")

    fig, ax = plt.subplots(figsize=(9, 5.2), facecolor=BACKGROUND)
    fig.subplots_adjust(left=.015, right=.985, top=.99, bottom=.01)
    ax.set(xlim=(0, 98_000 / scale), ylim=(0, 56_000 / scale), aspect="equal")
    ax.set_axis_off()
    for group, alpha, width in [("context", .28, .45), ("LPLC2", .58, .62)]:
        segments = np.concatenate(traces[group])
        ax.add_collection(LineCollection(segments, colors=COLORS[group], linewidths=width, alpha=alpha))
    ax.scatter(*(readout / scale).T, s=210, facecolors="none",
               edgecolors=COLORS["DNp01"], linewidths=1, alpha=.66, zorder=3)
    ax.scatter(*(readout / scale).T, s=54, c=COLORS["DNp01"],
               edgecolors=BACKGROUND, linewidths=1.2, zorder=4)

    path = ROOT / "site" / "assets" / "malecns-perturbation.png"
    fig.savefig(path, dpi=190, facecolor=BACKGROUND)
    plt.close(fig)
    print(f"{path} · {len(traces['context'])} context traces, {len(traces['LPLC2'])} input traces, {len(readout)} readout positions")


if __name__ == "__main__":
    main()
