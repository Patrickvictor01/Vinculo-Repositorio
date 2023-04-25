#Pandas Básico
import pandas as pd
dict = {"país": ["Brasil", "Russia", "Índia", "China", "Africa do Sul"], "capital": ["Brasília", "Moscou", "New Dehli", "Pequim", "Pretóeia"],
        "área": [8.516, 17.10, 3.286, 9.597, 1.221],
        "população": [200.4, 143.5, 1252, 1357, 52.98]}
brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)