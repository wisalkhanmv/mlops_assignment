# MLOps Assignment 1

## Group members:

- i200697 Muhammad Wisal

### How to Install

1. Clone the repository: `git clone https://github.com/i200844/mlops_task4`
2. Navigate to the cloned repository: `cd mlops_task4`
3. Install the requirements: `pip install -r requirements.txt`
4. Run the app: `python app.py`
5. Open your browser and go to `http://localhost:5000/`

### Endpoint Usage

- **Endpoint URL**: `http://localhost:5000/predict`
- **Method**: POST
- **Input Data Format**: JSON

Example input data for prediction:

```json
{
  "alcohol": 13.72,
  "malic_acid": 1.43,
  "ash": 2.5,
  "alcalinity_of_ash": 16.7,
  "magnesium": 108,
  "total_phenols": 3.4,
  "flavanoids": 3.67,
  "nonflavanoid_phenols": 0.19,
  "proanthocyanins": 2.04,
  "color_intensity": 6.8,
  "hue": 0.89,
  "od280/od315_of_diluted_wines": 2.87,
  "proline": 1285
}
```
