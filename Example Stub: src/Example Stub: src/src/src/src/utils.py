import pandas as pd
from pathlib import Path

def make_tables():
    resdir = Path("results")
    tables_tex = resdir/"tables.tex"

    with open(tables_tex, "w") as f:
        # Spectral gap
        df = pd.read_csv(resdir/"spectral_gap.csv")
        f.write("\\subsection*{Spectral Gap Test}\\n")
        f.write("\\begin{tabular}{c c}\\n$k$ & Error \\\\ \\hline\\n")
        for _, row in df.iterrows():
            f.write(f"{int(row.k)} & {row.error:.2e} \\\\\\n")
        f.write("\\end{tabular}\\n\\n")

        # Bridge error
        df = pd.read_csv(resdir/"bridge.csv")
        f.write("\\subsection*{Bridge Lemma Error}\\n")
        f.write("\\begin{tabular}{c c}\\n$j$ & Error \\\\ \\hline\\n")
        for _, row in df.iterrows():
            f.write(f"{int(row.j)} & {row.bridge_error:.2e} \\\\\\n")
        f.write("\\end{tabular}\\n\\n")

        # Enstrophy decay
        df = pd.read_csv(resdir/"enstrophy.csv")
        f.write("\\subsection*{Enstrophy Decay}\\n")
        f.write("\\begin{tabular}{c c}\\n$j$ & Half-life (t units) \\\\ \\hline\\n")
        for _, row in df.iterrows():
            f.write(f"{int(row.j)} & {row.half_life:.2e} \\\\\\n")
        f.write("\\end{tabular}\\n\\n")

        # JHTDB alignment
        df = pd.read_csv(resdir/"jhtdb.csv")
        f.write("\\subsection*{JHTDB Alignment}\\n")
        f.write("\\begin{tabular}{c c}\\nTrial & $A_{est}$ \\\\ \\hline\\n")
        for _, row in df.iterrows():
            f.write(f"{int(row.trial)} & {row.A_est:.3f} \\\\\\n")
        f.write("\\end{tabular}\\n")

    print(f"LaTeX tables written to {tables_tex}")

if __name__ == "__main__":
    make_tables()
