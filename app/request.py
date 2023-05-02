import requests

URL = "http://127.0.0.1:8000/v1/predict/"
data = {
    "data": [
        {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        },
        {
            "sepal_length": 6.2,
            "sepal_width": 3.4,
            "petal_length": 5.4,
            "petal_width": 2.3,
        },
    ]
}

x = requests.post(URL, json=data, timeout=1)
print(x.status_code)
print(x.text)
