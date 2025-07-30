import pandas as pd

# Sample data
data = {
    "user_id": range(1, 11),
    "treatment": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    "pre_spend": [100, 120, 90, 110, 95, 130, 85, 125, 80, 135],
    "post_spend": [105, 145, 92, 150, 98, 160, 88, 155, 83, 165]
}

df = pd.DataFrame(data)

# Save to Downloads folder
import os
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "pre_post_events.csv")
df.to_csv(downloads_path, index=False)

print(f"CSV saved to: {downloads_path}")
