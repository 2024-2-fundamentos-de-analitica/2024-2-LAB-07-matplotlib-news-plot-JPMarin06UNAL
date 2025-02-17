"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():

    plt.figure()

    colors_plt = {"Television":"dimgray",
            "Newspaper": "grey",
            "Internet": "tab:blue",
            "Radio": "Lightgrey",
            }
    
    zorder = {"Television": 1,
            "Newspaper": 1,
            "Internet": 2,
            "Radio": 1,
            }
    
    linewidths_plt = {"Television": 2,
            "Newspaper": 2,
            "Internet": 4,
            "Radio": 2,
            }

    df = pd.read_csv("files/input/news.csv", index_col=0)

    for col in df.columns:

        plt.plot(
            df[col], 
            color=colors_plt[col],
            label=col,
            zorder=zorder[col],
            linewidth=linewidths_plt[col],
            )

    plt.title("How people get their news", fontsize=16)

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in df.columns:

        first_year = df[col].index[0]
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors_plt[col],
            zorder=zorder[col],
        )

        plt.text(
            first_year -0.2,
            df[col][first_year],
            col + " "+ str(df[col][first_year]) + "%",
            ha = "right",
            va = "center",
            color = colors_plt[col],
        )


        last_year = df[col].index[-1]
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors_plt[col],
            zorder=zorder[col],
        )

        plt.text(
            last_year + 0.2,
            df[col][last_year],
            str(df[col][last_year]) + "%",
            ha = "left",
            va = "center",
            color = colors_plt[col],
        )

    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha = "center",
    )

    os.makedirs(os.path.dirname("files/plots/news.png"), exist_ok=True)
    plt.savefig("files/plots/news.png")
    plt.show()
    
pregunta_01()