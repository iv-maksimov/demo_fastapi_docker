from pydantic import BaseModel
from typing import List

class Sample(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class Data(BaseModel):
    data: List[Sample]
    class Config:
        schema_extra = {
            "example":{"data": [{ "sepal_length": 5.1,
                        "sepal_width": 3.5,
                        "petal_length": 1.4,
                        "petal_width": 0.2
                        },
                        { "sepal_length": 6.2,
                         "sepal_width": 3.4,
                         "petal_length": 5.4,
                         "petal_width": 2.3
                         }, 
                         ]}
        }

