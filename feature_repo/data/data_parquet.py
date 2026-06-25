import pandas as pd
from datetime import datetime

df = pd.DataFrame({
    "user_id":         [1, 2, 3],
    "score":           [0.9, 0.4, 0.7],
    "event_timestamp": [datetime.now()] * 3,
})
df.to_parquet("data/dati.parquet")
