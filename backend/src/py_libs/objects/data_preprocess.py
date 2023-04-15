from src import REPO
import pandas as pd
import numpy as np

from tqdm import tqdm
from pathlib import Path
from collections import defaultdict



class DataPreprocessor:
    def __init__(self):
        pass

    def remove_too_short(self):
        from datetime import datetime
        from collections import Counter
        base_date = datetime.strptime('2021-01-04', '%Y-%m-%d')
        root_folder = Path('./stock_raw_data')
        c = []
        for file in tqdm(root_folder.iterdir()):
            if file.suffix != '.csv':
                continue
            df = pd.read_csv(str(file))
            date = datetime.strptime(df.iloc[0, 0], '%Y-%m-%d')
            if base_date < date:
                file.unlink()
                print(f"Removed {str(file)}")
            c.append(len(df.index))
        count = Counter(c)
        print(count)

    def pick_top500_independent(self):
        def func(row):
            all_vector[row.name].append(row.iloc[1:7].to_numpy().astype(np.float32))

        root_folder = Path('./stock_raw_data')
        num_row = 568
        all_vector = [[] for _ in range(num_row)]
        for file in tqdm(root_folder.iterdir()):
            # if len(all_vector[0])>10:
            #     break
            if file.suffix != '.csv':
                continue
            df = pd.read_csv(str(file))
            df.apply(func, axis=1)

        var_score = defaultdict(int)
        for i in tqdm(range(num_row - 1, -1, -1)):
            try:
                X = np.array(all_vector[i])
                X = (X - X.mean(axis=0)) / X.std(axis=0)

                from sklearn.decomposition import PCA
                pca = PCA(n_components=5)
                pca.fit_transform(X.T)
                loadings = pca.components_.T * np.sqrt(pca.explained_variance_)
                var_order = np.argsort(-loadings[:, 0])

                for idx, v in enumerate(var_order):
                    var_score[v] += idx

            except Exception as e:
                print(f"Error on {i}th row!")
                print(e)
                continue

        with open('v_order.txt', 'a') as f:
            f.write(f"{', '.join([str(x) for x in sorted(list(var_score.items()), key=lambda x: x[1])])}\n")
        return

    def remove_other_top500_stock_id(self):
        with open('v_order.txt', 'r') as f:
            line = f.readline()

        pairs = line.split('), (')
        pairs = [tuple(p.strip('()\n').split(', ')) for p in pairs]
        pairs = [int(p[0]) for p in pairs][:500]
        pairs = set(pairs)

        root_folder = Path('./stock_raw_data')
        cnt = 0

        for file in tqdm(root_folder.iterdir()):
            if cnt not in pairs:
                file.unlink()
            cnt += 1

        return