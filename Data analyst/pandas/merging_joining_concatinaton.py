import numpy as np
import pandas as pd

# merging 2 dataframes:

import pandas as pd

employee = pd.DataFrame({
    "id": [101],
    "name": ["Satyam"],
    "age": [22],
    "department": ["IT"]
})

print(employee)


#     id    name  age department
# 0  101  Satyam   22         IT

salary = pd.DataFrame({
    "id": [101],
    "basic": [25000],
    "hra": [8000],
    "ta": [2000],
    "gross": [35000]
})

print(salary)

#     id  basic   hra    ta  gross
# 0  101  25000  8000  2000  35000

print(pd.merge(employee,salary))

#     id    name  age department  basic   hra    ta  gross
# 0  101  Satyam   22         IT  25000  8000  2000  35000
