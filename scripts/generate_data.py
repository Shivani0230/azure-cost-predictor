import pandas as pd
import numpy as np
from datetime import timedelta, datetime

np.random.seed(42)
start_date = datetime(2024, 1, 1)
days = 100

dates = [start_date + timedelta(days=i) for i in range(days)]
costs = np.random.normal(loc=50, scale=10, size=days).round(2)
resource_types = np.random.choice(['VM', 'Storage', 'Database', 'AI'], size=days)

df = pd.DataFrame({
    'date': dates,
    'resource_type': resource_types,
    'cost': costs
})

df.to_csv('data/simulated_cost_data.csv', index=False)
print("Simulated data saved.")