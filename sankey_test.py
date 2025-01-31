import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import os

# Change directory if necessary
os.chdir("/path/your/folder/hulabor_stat_sankey")


# Excel file reading
excel_path = 'data/munka.xlsx'
df = pd.read_excel(excel_path, "Sheet1")

# Prepare data
labels = df['status_en'].tolist()
source = df['source_id'].tolist()
target = df['target_id'].tolist()
value = df['value'].tolist()
node_colors = df['hexa'].tolist()

# Create Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=node_colors  # Node colors
    ),
    link=dict(
        source=source,
        target=target,
        value=value,
        color="rgba(0, 0, 255, 0.08)",  # Link color
    )
)])

# Update layout
fig.update_layout(
    title="Hungarian Labor Market Status Q1 2024",
    title_font_size=24,  # Title font size
    font_size=13,  # General text font size
    plot_bgcolor='white',  # Background color
    hoverlabel=dict(
        bgcolor='white',
        font_size=14,
    ),
    margin=dict(l=50, r=50, t=50, b=50),  # Margins around the plot
    width=1200,  # Diagram width in pixels
    height=800,  # Diagram height in pixels
    
)


# Show the diagram in the default browser
pio.renderers.default = 'browser'
fig.show()

# Save the diagram as an HTML file
html_file_path = os.path.join('output', 'sankey_diagram.html')
fig.write_html(html_file_path)

# Generate image file path
image_file_path = os.path.join('output', 'sankey_diagram.png')

# Save the diagram as an image file
fig.write_image(image_file_path, format="png", engine="kaleido", scale=5)  # Scale set to 5 for higher resolution

print(f"Sankey diagram saved as {image_file_path}")









