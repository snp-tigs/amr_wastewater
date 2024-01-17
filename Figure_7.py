import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns  # Import seaborn for color palettes

# Read the CSV file into a DataFrame
data = pd.read_csv('/home/manas/Documents/who_circular_plot/7NOV/WHO_eskape_pathogens_for plotting.csv')

# Sorting the data by group
df_sorted = (
    data
    .groupby(["Pathogens"])
    .apply(lambda x: x.sort_values(["RPM"], ascending=False))
    .reset_index(drop=True)
)
VALUES = df_sorted["RPM"].values
LABELS = df_sorted["Drug Class"].values
GROUP = df_sorted["Pathogens"].values

# Specify constants
PAD = 2
OFFSET = np.pi / 2
ANGLES_N = len(VALUES) + PAD * len(np.unique(GROUP))
ANGLES = np.linspace(0, 2 * np.pi, num=ANGLES_N, endpoint=False)
WIDTH = (2 * np.pi) / len(ANGLES)  #width between each drug class

GROUPS_SIZE = [len(i[1]) for i in data.groupby("Pathogens")]

offset = 0
IDXS = []
for size in GROUPS_SIZE:
    IDXS += list(range(offset + PAD, offset + size + PAD))
    offset += size + PAD

# Create the figure and axis
fig, ax = plt.subplots(figsize=(100,100), subplot_kw={"projection": "polar"})
ax.set_theta_offset(OFFSET)
ax.set_ylim(-200, 500)  #We limit the RPM of drug class for a better visualisation,
#ax.set_ylim(-200, 194000) #one can use this parameter for getting the upper limit of RPM of Drug class
ax.set_frame_on(False)
ax.xaxis.grid(False)
ax.yaxis.grid(False)
ax.set_xticks([])
ax.set_yticks([])

custom_colors = [
    "#6b0c00", "#691f01", "#594411", "#2b3f2b", "#29413b",
    "#b21400", "#af3502", "#95721d", "#486a48", "#456d63",
    "#61988b", "#659465", "#d1a028", "#f64a03", "#f91c00",
    "#ff5842", "#fc7a45", "#e0bb61", "#8eb28e", "#8bb5ab",
    "#ff9789", "#fdac8b", "#ebd59c", "#b9cfb9", "#b7d1cb",
    "#4b261f", "#7e4034", "#b05a49", "#c78679", "#dcb3ac",
    "#292248", "#443a78", "#6051a8", "#8a7fc1", "#b6afd8",
    "#006b3a", "#00b261", "#00f988", "#42ffa9", "#89ffc9",
    "#00506b", "#0085b2", "#00bbf9", "#42cfff", "#89e1ff",
    "#004F88", "#006B79", "#007F6D", "#008DB2", "#0099A3",
    "#00A5A6", "#005F8F", "#006B81", "#007A75", "#008FA1",
    "#009A98", "#00A6A6", "#00488A", "#006C92", "#007F99"
]





# Ensure the custom_colors list is long enough for all unique LABELS
unique_labels = np.unique(LABELS)

if len(custom_colors) < len(unique_labels):
    # Extend the custom_colors list with repeated colors or generate more colors
    num_additional_colors = len(unique_labels) - len(custom_colors)
    repeated_colors = custom_colors[:num_additional_colors]
    custom_colors.extend(repeated_colors)

# Assign colors to LABELS values
labels_colors = {label: color for label, color in zip(unique_labels, custom_colors)}

# Add bars with assigned colors
bar_colors = [labels_colors[label] for label in LABELS]
ax.bar(
    ANGLES[IDXS], VALUES, width=WIDTH, color=bar_colors,
    edgecolor="white", linewidth=2
)

# Add labels
def get_label_rotation(angle, offset):
    rotation = np.rad2deg(angle + offset)
    if angle <= np.pi:
        alignment = "right"
        rotation = rotation + 180
    else:
        alignment = "left"
    return rotation, alignment

def add_labels(angles, values, labels, offset, ax):
    padding = 4
    for angle, value, label in zip(angles, values, labels):
        angle = angle
        rotation, alignment = get_label_rotation(angle, offset)
        ax.text(
            x=angle,
            y=value + 3,
            s=label,
            ha=alignment,
            va="center",
            rotation=rotation,
            rotation_mode="anchor",
            fontsize=30,
            fontweight="medium",
            fontstyle= "italic"
        )

add_labels(ANGLES[IDXS], VALUES, LABELS, OFFSET, ax)

# Adding customization to show group names and reference lines
offset = 0
for group, size, color in zip(np.unique(GROUP), GROUPS_SIZE, custom_colors):
    # Add line below bars
    x1 = np.linspace(ANGLES[offset + PAD], ANGLES[offset + size + PAD - 1], num=50)
    ax.plot(x1, [-5] * 50, color=color)

    # Add text to indicate group
    ax.text(
        np.mean(x1), -10, group, color=color, fontsize=20,
        fontweight="bold", ha="center", va="center"
    )

    # Add reference lines
    x2 = np.linspace(ANGLES[offset], ANGLES[offset + PAD - 1], num=50)
    for y in [150000]:
        ax.plot(x2, [y] * 50, color="#bebebe", lw=0.8)

    x2 = np.linspace(ANGLES[offset], ANGLES[offset + PAD - 1], num=50)
    for y in [100, 200, 300, 400, 500]:
        ax.plot(x2, [y] * 50, color="#bebebe", lw=0.8)

    offset += size + PAD

plt.savefig('/home/manas/Downloads/circular_plot_WHO_RPM_NORMAISED_without pathogens name.png', dpi=200)