import pandas as pd
from fastapi import FastAPI
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,f1_score,recall_score
from collections import Counter

class AppService():
    # Loading dataset
    dataset = pd.read_csv("./sample/dataset_normalized.csv")
    dataset.columns = [i.strip() for i in dataset.columns]

    abc = "teste"
    X = dataset.iloc[:,0:-1]
    y = dataset.iloc[:,-1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)
    X_val, X_test, y_val, y_test = train_test_split(X_test,y_test,test_size=0.5,stratify=y_test)

    # Dados de frequência das classes
    datasets = {
        "TOTAL": Counter(y),
        "TREINO": Counter(y_train),
        "TESTE": Counter(y_test),
        "VALIDAÇÃO": Counter(y_val)
    }

    # Iterar sobre os datasets
    # for dataset, counter in datasets.items():
    #     print(f"Frequência das classes no dataset {dataset}:")
    #     for classe, frequencia in sorted(counter.items()):
    #         print(f"Classe {classe}: {frequencia}")
    #     print()

    # KNN - ALGORITHM
    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(X_train, y_train)

    # MLP - ALGORITHM
    mlp_model = MLPClassifier(hidden_layer_sizes=(2000,100,10),max_iter=1000)
    mlp_model.fit(X_train,y_train)

    # DECISION THREE - ALGORITHM
    tree_model = DecisionTreeClassifier()
    tree_model.fit(X_train,y_train)

    def __init__(self):
        self.app = FastAPI()

    def get_status(self):
        return {"status": "ok"}
    
    def check_game(self, game):
        # 0 = x loses
        # 1 = x wins
        # 2 = draw
        # 3 = in game

        game_status = game.status.split(", ")
        game_status = [eval(i) for i in game_status]

        result = {
            "game_knn": self.knn_model.predict([game_status]).tolist(),
            "game_mlp": self.mlp_model.predict([game_status]).tolist(),
            "game_tree": self.tree_model.predict([game_status]).tolist()
        }
        return result