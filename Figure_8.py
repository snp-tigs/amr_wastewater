import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Load GeoJSON data
hyderabad_data = gpd.read_file('/home/manas/Downloads/Downloads/sorted_hyd_wards_coordinates.geojson')

# Load population data
population_data = pd.read_csv('/home/manas/Downloads/Downloads/sorted wards hyd - Sheet2.csv')

# Merge the GeoJSON data with the population data
merged_data = hyderabad_data.merge(population_data, on='Ward Number')

# Calculate the area of each ward in square meters
merged_data['ward_area'] = merged_data.geometry.to_crs('EPSG:3395').area

# Calculate population density
merged_data['population_density'] = merged_data['Total Population'] / merged_data['ward_area'] * 1000000

# Set a finite aspect ratio
fig, ax = plt.subplots(figsize=(50, 30))

# Set the highest population count as the upper limit for color scale
vmax = merged_data['population_density'].max()

# Existing color values
colors = ['#ccece6', '#99d8c9', '#66c2a4', '#41ae76', '#238b45', '#006d2c', '#00441b']

# Number of interpolated colors between each pair of existing colors
num_interpolated_colors = 10

# Create a new colormap with interpolated colors
new_colors = []
for i in range(len(colors) - 1):
    for j in range(num_interpolated_colors + 1):
        color_i = mcolors.hex2color(colors[i])
        color_j = mcolors.hex2color(colors[i + 1])
        # Interpolate between color_i and color_j
        interpolated_color = [color_i[k] + (color_j[k] - color_i[k]) * (j / num_interpolated_colors) for k in range(3)]
        new_colors.append(interpolated_color)

# Create the new colormap
new_cmap = mcolors.ListedColormap(new_colors)


# Plot the population density
merged_data.plot(column='population_density', cmap=new_cmap, linewidth=0.8, edgecolor='0.8',
                 legend=True, ax=ax, vmin=0, vmax=vmax )

# Add your own coordinates
custom_coordinates = [
    {'latitude': 17.37100, 'longitude': 78.52981, 'label': '', 'value': 208, 'radius': 10},#cp
    {'latitude': 17.37166354, 'longitude': 78.52945604, 'label': ''},
    {'latitude': 17.3710752, 'longitude': 78.53041057, 'label': ''},
    {'latitude': 17.37066812, 'longitude': 78.53228442, 'label': ''},
    {'latitude': 17.3697624, 'longitude': 78.53195276, 'label': ''},
    {'latitude': 17.37009974, 'longitude': 78.53157493, 'label': ''},
    {'latitude': 17.36974496, 'longitude': 78.52924704, 'label': ''},
    {'latitude': 17.37134633, 'longitude': 78.53049351, 'label': ''},
    {'latitude': 17.36977944, 'longitude': 78.53101571, 'label': ''},
    {'latitude': 17.37141751, 'longitude': 78.53077214, 'label': ''},
    {'latitude': 17.36945245, 'longitude': 78.53140055, 'label': ''},
    {'latitude': 17.36961942, 'longitude': 78.53020507, 'label': ''},
    {'latitude': 17.3693291, 'longitude': 78.53040146, 'label': ''},
    {'latitude': 17.36912028, 'longitude': 78.5301517, 'label': ''},
    {'latitude': 17.36886663, 'longitude': 78.53001508, 'label': ''},
    {'latitude': 17.36978512, 'longitude': 78.53338564, 'label': ''},
    {'latitude': 17.36924754, 'longitude': 78.53447461, 'label': ''},
    {'latitude': 17.36890963, 'longitude': 78.53469455, 'label': ''},
    {'latitude': 17.36876628, 'longitude': 78.53438878, 'label': ''},
    {'latitude': 17.37207365, 'longitude': 78.53587473, 'label': ''},
    {'latitude': 17.36878684, 'longitude': 78.5205992, 'label': ''},
    {'latitude': 17.37193282, 'longitude': 78.5205992, 'label': ''},
    {'latitude': 17.37233875, 'longitude': 78.52410818, 'label': ''},
    {'latitude': 17.36953105, 'longitude': 78.52513606, 'label': ''},
    {'latitude': 17.35559342, 'longitude': 78.53257935, 'label': ''},
    {'latitude': 17.36936192, 'longitude': 78.53417434, 'label': ''},
    {'latitude': 17.34686494, 'longitude': 78.5395973, 'label': ''},
    {'latitude': 17.36990316, 'longitude': 78.53484778, 'label': ''},
    {'latitude': 17.35988984, 'longitude': 78.54484304, 'label': ''},
    {'latitude': 17.36880662, 'longitude': 78.52585037, 'label': ''},
    {'latitude': 17.34995768, 'longitude': 78.54849712, 'label': ''},
    {'latitude': 17.37260868, 'longitude': 78.52077381, 'label': ''},
    {'latitude': 17.34858441, 'longitude': 78.51952097, 'label': ''},
    {'latitude': 17.369852, 'longitude': 78.471160, 'label': '', 'value': 161, 'radius': 10},#pp
    {'latitude': 17.3747980219173, 'longitude': 78.4749719373047, 'label': ''},
    {'latitude': 17.3709526785877, 'longitude': 78.47154788, 'label': ''},
    {'latitude': 17.37308248, 'longitude': 78.47569994, 'label': ''},
    {'latitude': 17.36065542, 'longitude': 78.47474872, 'label': ''},
    {'latitude': 17.37214608, 'longitude': 78.47161361, 'label': ''},
    {'latitude': 17.36571749, 'longitude': 78.46265471, 'label': ''},
    {'latitude': 17.36629847, 'longitude': 78.4587112, 'label': ''},
    {'latitude': 17.37416, 'longitude': 78.4834086, 'label': ''},
    {'latitude': 17.37512038, 'longitude': 78.48434056, 'label': ''},
    {'latitude': 17.37321053, 'longitude': 78.48466074, 'label': ''},
    {'latitude': 17.37013836, 'longitude': 78.48566704, 'label': ''},
    {'latitude': 17.36763366, 'longitude': 78.48253381, 'label': ''},
    {'latitude': 17.36292975, 'longitude': 78.47621589, 'label': ''},
    {'latitude': 17.35874961, 'longitude': 78.47800549, 'label': ''},
    {'latitude': 17.35647941, 'longitude': 78.47403749, 'label': ''},
    {'latitude': 17.36852313, 'longitude': 78.46718784, 'label': ''},
    {'latitude': 17.36496522, 'longitude': 78.46269955, 'label': ''},
    {'latitude': 17.37199867, 'longitude': 78.4697479, 'label': ''},
    {'latitude': 17.37302449, 'longitude': 78.46729752, 'label': ''},
    {'latitude': 17.37340469, 'longitude': 78.46747792, 'label': ''},
    {'latitude': 17.366623, 'longitude': 78.457590, 'label': '', 'value': 151, 'radius': 10},#bp
    {'latitude': 17.36662061, 'longitude': 78.45794492, 'label': ''},
    {'latitude': 17.36571951, 'longitude': 78.46191459, 'label': ''},
    {'latitude': 17.3703888, 'longitude': 78.45848136, 'label': ''},
    {'latitude': 17.37009074, 'longitude': 78.44766601, 'label': ''},
    {'latitude': 17.35540362, 'longitude': 78.45289552, 'label': ''},
    {'latitude': 17.37986, 'longitude': 78.49301, 'label': '', 'value': 150, 'radius': 10},#ch
    {'latitude': 17.37700975, 'longitude': 78.49072838, 'label': ''},
    {'latitude': 17.37962449, 'longitude': 78.49787955, 'label': ''},
    {'latitude': 17.37270609, 'longitude': 78.50059842, 'label': ''},
    {'latitude': 17.37179676, 'longitude': 78.50057195, 'label': ''},
    {'latitude': 17.37080282, 'longitude': 78.48723147, 'label': ''},
    {'latitude': 17.37527355, 'longitude': 78.48428482, 'label': ''},
    {'latitude': 17.38536833, 'longitude': 78.48668369, 'label': ''},
    {'latitude': 17.38978462, 'longitude': 78.49541032, 'label': ''},
    {'latitude': 17.37482288, 'longitude': 78.5013414, 'label': ''},
    {'latitude': 17.3732728, 'longitude': 78.50343109, 'label': ''},
   {'latitude': 17.376398, 'longitude': 78.433508, 'label': '', 'value': 149, 'radius': 10},#mn
    {'latitude': 17.38399579, 'longitude': 78.43015563, 'label': ''},
    {'latitude': 17.38071046, 'longitude': 78.43011053, 'label': ''},
    {'latitude': 17.36801124, 'longitude': 78.42960127, 'label': ''},
    {'latitude': 17.36362783, 'longitude': 78.43624684, 'label': ''},
    {'latitude': 17.37099986, 'longitude': 78.45653149, 'label': ''},
    {'latitude': 17.3921513, 'longitude': 78.42667861, 'label': ''},
    {'latitude': 17.39440908, 'longitude': 78.4267482, 'label': ''},
    {'latitude': 17.39533875, 'longitude': 78.43078425, 'label': ''},
    {'latitude': 17.38813371, 'longitude': 78.44417978, 'label': ''},
    {'latitude': 17.38969427, 'longitude': 78.44230092, 'label': ''},
    {'latitude': 17.38019089, 'longitude': 78.42334096, 'label': ''},
    {'latitude': 17.521502, 'longitude': 78.29131, 'label': '', 'value': 144, 'radius': 10},#rp
    {'latitude': 17.53153804, 'longitude': 78.29807974, 'label': ''},
    {'latitude': 17.50666637, 'longitude': 78.28433386, 'label': ''},
    {'latitude': 17.49583743, 'longitude': 78.32148082, 'label': ''},
    {'latitude': 17.52177546, 'longitude': 78.28794423, 'label': ''},
    {'latitude': 17.51368793, 'longitude': 78.30203349, 'label': ''},
    {'latitude': 17.50654573, 'longitude': 78.28425666, 'label': ''},
    {'latitude': 17.50253292, 'longitude': 78.28703492, 'label': ''},
    {'latitude': 17.52463805, 'longitude': 78.28526965, 'label': ''},
    {'latitude': 17.52056205, 'longitude': 78.28382723, 'label': ''},
    {'latitude': 17.51874486, 'longitude': 78.28340377, 'label': ''},
    {'latitude': 17.52188708, 'longitude': 78.28691057, 'label': ''},
    {'latitude': 17.52439829, 'longitude': 78.28659298, 'label': ''},
    {'latitude': 17.52531948, 'longitude': 78.28738697, 'label': ''},
    {'latitude': 17.52001942, 'longitude': 78.28463446, 'label': ''},
    {'latitude': 17.526329, 'longitude': 78.28131291, 'label': ''},
    {'latitude': 17.52345186, 'longitude': 78.27988372, 'label': ''},
   {'latitude': 17.501354, 'longitude': 78.315272, 'label': '', 'value': 127, 'radius': 10},#kc
    {'latitude': 17.49839051, 'longitude': 78.31458465, 'label': ''},
    {'latitude': 17.49560909, 'longitude': 78.32127722, 'label': ''},
    {'latitude': 17.50480789, 'longitude': 78.30889614, 'label': ''},
    {'latitude': 17.50845173, 'longitude': 78.3029437, 'label': ''},
    {'latitude': 17.51353934, 'longitude': 78.3022672, 'label': ''},
    {'latitude': 17.51013052, 'longitude': 78.2998088, 'label': ''},
    {'latitude': 17.50707454, 'longitude': 78.28472576, 'label': ''},
    {'latitude': 17.377516, 'longitude': 78.366172, 'label': '', 'value': 115, 'radius': 10},#ta
    {'latitude': 17.36144721, 'longitude': 78.3890612, 'label': ''},
    {'latitude': 17.371554, 'longitude': 78.423584, 'label': '', 'value': 115, 'radius': 10},#k
    {'latitude': 17.37052509, 'longitude': 78.42403937, 'label': ''},
    {'latitude': 17.36701186, 'longitude': 78.42783455, 'label': ''},
    {'latitude': 17.37713738, 'longitude': 78.42726327, 'label': ''},
    {'latitude': 17.37663891, 'longitude': 78.42034264, 'label': ''},
    {'latitude': 17.37614043, 'longitude': 78.41903686, 'label': ''},
    {'latitude': 17.37367919, 'longitude': 78.41608253, 'label': ''},
    {'latitude': 17.38023723, 'longitude': 78.4210445, 'label': ''},
    {'latitude': 17.36895912, 'longitude': 78.43194776, 'label': ''},
    {'latitude': 17.36479975, 'longitude': 78.43630579, 'label': ''},
    {'latitude': 17.371469, 'longitude': 78.404719, 'label': '', 'value': 114, 'radius': 10},#bgr
    {'latitude': 17.37609742, 'longitude': 78.39344716, 'label': ''},
    {'latitude': 17.37357855, 'longitude': 78.41466879, 'label': ''},
    {'latitude': 17.3606765, 'longitude': 78.40329623, 'label': ''},
    {'latitude': 17.36114754, 'longitude': 78.38915562, 'label': ''},
    {'latitude': 17.3804388, 'longitude': 78.42099881, 'label': ''},
    {'latitude': 17.38949, 'longitude': 78.50476, 'label': '', 'value': 108, 'radius': 10},#gn
    {'latitude': 17.39344501, 'longitude': 78.49750672, 'label': ''},
    {'latitude': 17.39673291, 'longitude': 78.50292104, 'label': ''},
    {'latitude': 17.39442356, 'longitude': 78.51038624, 'label': ''},
    {'latitude': 17.38698646, 'longitude': 78.51391375, 'label': ''},
    {'latitude': 17.38017538, 'longitude': 78.49758876, 'label': ''},
    {'latitude': 17.39951192, 'longitude': 78.49438939, 'label': ''},
    {'latitude': 17.39661548, 'longitude': 78.52326576, 'label': ''},
    {'latitude': 17.40154, 'longitude': 78.58124, 'label': '', 'value': 111, 'radius': 10},#ubc
    {'latitude': 17.40280613, 'longitude': 78.58261955, 'label': ''},
    {'latitude': 17.40303873, 'longitude': 78.58278409, 'label': ''},
    {'latitude': 17.40094377, 'longitude': 78.57966995, 'label': ''},
    {'latitude': 17.40195764, 'longitude': 78.57633018, 'label': ''},
    {'latitude': 17.40101813, 'longitude': 78.57233121, 'label': ''},
    {'latitude': 17.371057, 'longitude': 78.411769, 'label': '', 'value': 90, 'radius': 10},#bgl
    {'latitude': 17.37337052, 'longitude': 78.41445993, 'label': ''},
    {'latitude': 17.37443865, 'longitude': 78.41345216, 'label': ''},
    {'latitude': 17.36081218, 'longitude': 78.40374539, 'label': ''},
    {'latitude': 17.42080, 'longitude': 78.55109, 'label': '', 'value': 74, 'radius': 10},#pc
    {'latitude': 17.42297924, 'longitude': 78.5469408, 'label': ''},
    {'latitude': 17.42491296, 'longitude': 78.54839343, 'label': ''},
    {'latitude': 17.42692967, 'longitude': 78.54901101, 'label': ''},
    {'latitude': 17.4275687, 'longitude': 78.55213374, 'label': ''},
    {'latitude': 17.42830732, 'longitude': 78.55171621, 'label': ''},
    {'latitude': 17.42671389, 'longitude': 78.55516078, 'label': ' '},
    {'latitude': 17.41514466, 'longitude': 78.54642363, 'label': ''},
    {'latitude': 17.4025044, 'longitude': 78.56677739, 'label': ''},
    {'latitude': 17.40431691, 'longitude': 78.58238689, 'label': ''},
    {'latitude': 17.35456, 'longitude': 78.53013, 'label': '', 'value': 69, 'radius': 10},#pd
    {'latitude': 17.35492762, 'longitude': 78.53240658, 'label': ''},
    {'latitude': 17.35148552, 'longitude': 78.53166582, 'label': ''},
    {'latitude': 17.35210749, 'longitude': 78.52658685, 'label': ''},
    {'latitude': 17.36155487, 'longitude': 78.52123132, 'label': ''},
    {'latitude': 17.35842129, 'longitude': 78.51616359, 'label': ''},
    {'latitude': 17.35930835, 'longitude': 78.51421727, 'label': ''},
    {'latitude': 17.35673498, 'longitude': 78.51326414, 'label': ''},
    {'latitude': 17.35307022, 'longitude': 78.51308744, 'label': ''},
    {'latitude': 17.35025046, 'longitude': 78.51199739, 'label': ''},
    {'latitude': 17.34864203, 'longitude': 78.51113377, 'label': ''},
    {'latitude': 17.36141044, 'longitude': 78.53869187, 'label': ''},
    {'latitude': 17.36768044, 'longitude': 78.53583561, 'label': ''},
    {'latitude': 17.3691152, 'longitude': 78.53010805, 'label': ''},
    {'latitude': 17.36980387, 'longitude': 78.52869495, 'label': ''},
    {'latitude': 17.36849825, 'longitude': 78.52205039, 'label': ''},
    {'latitude': 17.36826869, 'longitude': 78.52048696, 'label': ''},
    {'latitude': 17.34754967, 'longitude': 78.51988564, 'label': ''},
    {'latitude': 17.34452197, 'longitude': 78.52669557, 'label': ''},
    {'latitude': 17.3403606, 'longitude': 78.52190006, 'label': ''},
    {'latitude': 17.34632999, 'longitude': 78.53992457, 'label': ''},
    {'latitude': 17.34327357, 'longitude': 78.5415331, 'label': ''},
    {'latitude': 17.35356506, 'longitude': 78.53032946, 'label': ''},
    {'latitude': 17.509587, 'longitude': 78.295077, 'label': '', 'value': 37, 'radius': 10},#rrc
    {'latitude': 17.5101362, 'longitude': 78.29989216, 'label': ''},
    {'latitude': 17.50899027, 'longitude': 78.30016495, 'label': ''},
    {'latitude': 17.50832748, 'longitude': 78.30286694, 'label': ''},
    {'latitude': 17.5081974, 'longitude': 78.29924264, 'label': ''},
    {'latitude': 17.51157325, 'longitude': 78.29309172, 'label': ''},
    {'latitude': 17.51181171, 'longitude': 78.2888934, 'label': ''},
    {'latitude': 17.51251732, 'longitude': 78.29935158, 'label': ''},
    {'latitude': 17.50896547, 'longitude': 78.30242182, 'label': ''},
    {'latitude': 17.50250073, 'longitude': 78.28695061, 'label': ''},
    {'latitude': 17.50384835, 'longitude': 78.28444074, 'label': ''},
    {'latitude': 17.50652469, 'longitude': 78.28442098, 'label': ''},
    {'latitude': 17.51129768, 'longitude': 78.28482073, 'label': ''},
    {'latitude': 17.51681102, 'longitude': 78.29391842, 'label': ''},
    {'latitude': 17.49859361, 'longitude': 78.31432163, 'label': ''},
    {'latitude': 17.50501942, 'longitude': 78.31183254, 'label': ''},
    {'latitude': 17.49488, 'longitude': 78.32169836, 'label': ''},
    {'latitude': 17.53275609, 'longitude': 78.29770059, 'label': ''},
    {'latitude': 17.370999, 'longitude': 78.352569, 'label': ' ', 'value': 24, 'radius': 10},#aa
    {'latitude': 17.38605485, 'longitude': 78.35721939, 'label': ''},
    {'latitude': 17.36135385, 'longitude': 78.38947416, 'label': ''},
    {'latitude': 17.37629703, 'longitude': 78.39323186, 'label': ''},
    {'latitude': 17.3856276, 'longitude': 78.40311324, 'label': ''},

  #{'latitude': 17.50234534076864, 'longitude':  78.46080862222544, 'label': '50', 'value': 50, 'radius': 10},
  #{'latitude': 17.51547722158582, 'longitude':  78.45761591915468, 'label': '100', 'value': 100, 'radius': 10},
  #{'latitude': 17.490079479351042, 'longitude':  78.50647009730324, 'label': '150', 'value': 150, 'radius': 10},
  #{'latitude': 17.486650258620482, 'longitude':  78.46693846888839, 'label': '200', 'value': 200, 'radius': 10},
  #{'latitude': 17.438974685887136, 'longitude':  78.56793277717509, 'label': '250', 'value': 250, 'radius': 10},
  #{'latitude': 17.468554296951954, 'longitude':  78.43896743264463, 'label': '500', 'value': 500, 'radius': 10},#a
]

#---------------------Calculate circle size to 2kms radius (outer red circle)-------------------------#

# Function to calculate circle size based on values
def calculate_circle_size(radius):
    # Adjust the scaling factor to control the size of circles
    scaling_factor = 0.05
    return np.sqrt(radius) * scaling_factor

# Find the maximum 'value' in samples_coordinates
max_value = max(point.get('radius', 0) for point in custom_coordinates)

# Define the desired diameter for the largest circle (e.g., 5 cm)
desired_diameter_cm = 0.04  #adjusted the value taking a point on the map having a distance from the sample site of 2kms

# Calculate the scaling factor
scaling_factor = desired_diameter_cm / (2.0 * np.sqrt(max_value))  # Divide by 2 for radius


# Plot circles at sample_coordinates
for point in custom_coordinates:
    latitude = point['latitude']
    longitude = point['longitude']
    label = point['label']


   # Check if 'value' key exists in the dictionary
    if 'radius' in point:
        radius = point['radius']
    else:
        radius = 0

   # Calculate the circle size based on the scaling factor
    circle_size = np.sqrt(radius) * scaling_factor

    #circle_size = calculate_circle_size(value)


    ax.add_patch(plt.Circle((longitude, latitude), circle_size, edgecolor='#FF0000',
                            facecolor="None", alpha=0.5, linewidth=2.5))
print(scaling_factor)

#-----------Calculate circle size a/c ARO values----------------------------------

# Function to calculate circle size based on values
def cal_circle_size(value):
    # Adjust the scaling factor to control the size of circles
    scaling_factor = 0.05
    return np.sqrt(value) * scaling_factor

# Find the maximum 'value' in custom_coordinates
max_value = max(point.get('value', 0) for point in custom_coordinates)

# Define the desired diameter for the largest circle (e.g., 5 cm)
desired_diameter_cm = 0.02  # Adjust this value as needed

# Calculate the scaling factor
scaling_factor = desired_diameter_cm / (2.0 * np.sqrt(max_value))  # Divide by 2 for radius


# Plot circles at custom coordinates
for point in custom_coordinates:
    latitude = point['latitude']
    longitude = point['longitude']
    label = point['label']


# Check if 'value' key exists in the dictionary
    if 'value' in point:
        value = point['value']
    else:
        value = 0

# Calculate the circle size based on the scaling factor
    circle_size = np.sqrt(value) * scaling_factor

#circle_size = calculate_circle_size(value)


    ax.add_patch(plt.Circle((longitude, latitude), circle_size, color='#191970', alpha=0.4, linewidth=2.5))

#Annotaion of sample sites

    ax.text(longitude, latitude, label, fontsize=25, ha='left', va='bottom', fontweight='bold', color='#000080',
            rotation=45)

#Hospitals markers

    ax.plot(longitude, latitude, '.', color='#8B0000', markeredgecolor='#8B0000',
                markeredgewidth=2, markersize=18)

#--------------------------------square point at sample sites-----------------------------------------------

    ax.plot(78.352569, 17.370999,  's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12) #A
    ax.plot(78.471160, 17.369852, 's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12) #pp
    ax.plot(78.457590, 17.366623, 's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12)#bp
    ax.plot(78.49301, 17.37986, 's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12) #ch
    ax.plot(78.433508, 17.376398,  's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12)#mn
    ax.plot(78.29131, 17.521502, 's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12)#r
    ax.plot(78.315272, 17.501354, 's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12)#kc
    ax.plot(78.366172, 17.377516, 's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12)#t
    ax.plot(78.423584, 17.371554,  's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12)#k
    ax.plot(78.404719, 17.371469, 's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12)#bgr
    ax.plot(78.50476, 17.38949, 's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12)#gn
    ax.plot(78.58124, 17.40154, 's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12)#ubc
    ax.plot(78.411769, 17.371057,  's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12)#bgl
    ax.plot(78.55109, 17.42080, 's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12)#pc
    ax.plot(78.53013, 17.35456, 's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12)#pd
    ax.plot(78.295077, 17.509587, 's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12)#rrc
    ax.plot(78.52981, 17.37100, 's', color='#191970', markeredgewidth=1, markeredgecolor= 'black',markersize=12)  #cp

# Plot the population density with an outer boundary stroke line
merged_data.boundary.plot(ax=ax, color='black', linewidth=0.6)

# Add a basemap using contextily
#ctx.add_basemap(ax, crs='EPSG:4326', source=ctx.providers.Stamen.TonerLite)

# Add population counts as labels
#-------------------Ward annotation----------------------------------
for idx, row in merged_data.iterrows():
    population_count = row['population_density']
    ward_name = row['Ward Number']
    centroid = row['geometry'].centroid
    if population_count > 70000:
        ax.annotate(text=str(population_count), xy=(centroid.x, centroid.y), xytext=(18, 18), textcoords='offset points')
        ax.text(centroid.x, centroid.y, ward_name, fontsize=15, ha='center', va='center')

#plt.title('Population Density Map of Hyderabad with Custom Circles', fontsize= 25, color= 'black')
plt.xlabel('Longitude', fontsize= 25, color= 'black')
plt.ylabel('Latitude', fontsize= 25, color= 'black')

# Save the plot
#plt.savefig('/home/manas/Downloads/map_hyderabad___.png', dpi=300)

# Show the plot
plt.show()

