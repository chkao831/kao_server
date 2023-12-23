from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
from src import REPO
from tqdm import tqdm


class DataPreprocessor:
    def __init__(self):
        pass

    def check_na(self):
        root_folder = Path(REPO + "./stock_raw_data")
        for file in tqdm(root_folder.iterdir()):
            df = pd.read_csv(str(file))
            if len(df) < 1073:
                print(str(file))
                file.unlink()

    def check_row(self):
        tar_folder = Path(REPO + "./stock_raw_data")
        c = -1
        for file in tqdm(tar_folder.iterdir()):
            df = pd.read_csv(str(file))
            if c == -1:
                c = len(df)
            else:
                if c != len(df):
                    print(str(file))
                    print(c)
                    c = len(df)

    def remove_too_short(self):
        from collections import Counter
        from datetime import datetime

        base_date = datetime.strptime("2021-01-04", "%Y-%m-%d")
        root_folder = Path("./stock_raw_data")
        c = []
        for file in tqdm(root_folder.iterdir()):
            if file.suffix != ".csv":
                continue
            df = pd.read_csv(str(file))
            date = datetime.strptime(df.iloc[0, 0], "%Y-%m-%d")
            if base_date < date:
                file.unlink()
                print(f"Removed {str(file)}")
            c.append(len(df.index))
        count = Counter(c)
        print(count)

    def pick_top500_independent(self):
        def func(row):
            all_vector[row.name].append(row.iloc[2:8].to_numpy().astype(np.float32))

        root_folder = Path(REPO + "./stack_fetch_data")
        num_row = 1073
        all_vector = [[] for _ in range(num_row)]
        for file in tqdm(root_folder.iterdir()):
            # if len(all_vector[0])>10:
            #     break
            if file.suffix != ".csv":
                continue
            df = pd.read_csv(str(file))
            df.apply(func, axis=1)

        var_score = defaultdict(int)
        for i in tqdm(range(num_row - 1, -1, -1)):
            try:
                x = np.array(all_vector[i])
                x = (x - x.mean(axis=0)) / x.std(axis=0)

                from sklearn.decomposition import PCA

                pca = PCA(n_components=5)
                pca.fit_transform(x.T)
                loadings = pca.components_.T * np.sqrt(pca.explained_variance_)
                var_order = np.argsort(-loadings[:, 0])

                for idx, v in enumerate(var_order):
                    var_score[v] += idx

            except Exception as e:
                print(f"Error on {i}th row!")
                print(e)
                continue

        with open("v_order.txt", "w") as f:
            writting_str = ", ".join(
                [str(x) for x in sorted(var_score.items(), key=lambda x: x[1])]
            )
            f.write(f"{writting_str}\n")
        return

    def remove_other_top500_stock_id(self):
        with open("v_order.txt") as f:
            line = f.readline()

        pairs = line.split("), (")
        pairs = [tuple(p.strip("()\n").split(", ")) for p in pairs]
        pairs = [int(p[0]) for p in pairs][:500]
        pairs = set(pairs)

        root_folder = Path("./stack_fetch_data")
        cnt = 0

        for file in tqdm(root_folder.iterdir()):
            if cnt not in pairs:
                file.unlink()
            cnt += 1

        return
