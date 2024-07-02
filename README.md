# Demand Forecaster
Demand Forecaster is a project aimed at predicting sales demand using RandomForestRegressor based on historical sales data for various products.
## Installation

1. Clone the repository 
```bash 
git clone <repository-url>
cd <repository-directory>
```

2. To install the required dependencies, run the following command:
```bash
pip install -r requirements.txt
```

3. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```
## How It Works

### Algorithms Used
The project utilizes RandomForestRegressor for predicting sales demand based on historical data.

### Model Training
The model is trained on a dataset of sales data, incorporating features such as lagged sales, differences, and rolling averages.

### Example Usage
To run the application and predict sales demand:

Open Streamlit Application:
```bash
streamlit run main.py
```

### Upload Sales Data:
Upload your sales data in CSV format through the interface.



### View Predictions:
Explore the predicted sales for each product for the upcoming weeks.
Find the forecasted results here https://sales-demand-forecaster.onrender.com/ for the dataset i've used.

### Screenshots
<br><br><br>
![UI Page](https://github.com/Coolcoder009/Sales-Demand-Forecaster/blob/main/Screenshot%202024-04-23%20123308.jpg?raw=true)
![Image Description](https://github.com/Coolcoder009/Machine-Learning-Projects/blob/main/Sales_Demand_Forecaster/Screenshot%202024-04-23%20123336.jpg?raw=true)

