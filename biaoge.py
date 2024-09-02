import matplotlib.pyplot as plt
import pandas as pd

# Data for the table
data = {
    "Encrypt": ["✔", "✔", "✔"],
    "Security protocols": ["✔", "✔", "✔"],
    "Firewalls": ["✔", "✔", "✔"],
    "Automatic": ["✔", "✔", "✔"],
    "Proactive discovery": ["✔", "", "✔"],
    "Wide coverage": ["", "✔", "✔"],
    "Flow analysis": ["✔", "", "✔"],
    "Vulnerability scan": ["", "✔", "✔"],
    "System maintenance": ["", "", "✔"]
}

index = ["CAMHuNTER", "Automated Penetration Testing", "Comprehensive framework"]

# Create DataFrame
df = pd.DataFrame(data, index=index)

# Plot the table
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, rowLabels=df.index, cellLoc='center', loc='center')

# Formatting table
table.auto_set_font_size(False)
table.set_fontsize(12)
table.auto_set_column_width(col=list(range(len(df.columns))))

# Display the plot
plt.show()
