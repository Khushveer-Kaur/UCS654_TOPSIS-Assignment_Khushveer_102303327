import pandas as pd
import numpy as np
import os

def run_topsis(input_file, weights, impacts, output_file):
    df = pd.read_csv(input_file)

    if df.shape[1] < 3:
        raise Exception("Input file must contain at least three columns")

    data = df.iloc[:, 1:].values.astype(float)

    weights = [float(w) for w in weights.split(",")]
    impacts = impacts.split(",")

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        raise Exception("Weights and impacts must match number of criteria")

    norm = data / np.sqrt((data ** 2).sum(axis=0))
    weighted = norm * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(weighted[:, i].max())
            ideal_worst.append(weighted[:, i].min())
        elif impacts[i] == "-":
            ideal_best.append(weighted[:, i].min())
            ideal_worst.append(weighted[:, i].max())
        else:
            raise Exception("Impacts must be + or -")

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)
    df["Topsis Score"] = score
    df["Rank"] = df["Topsis Score"].rank(ascending=False)

    df.to_csv(output_file, index=False)
