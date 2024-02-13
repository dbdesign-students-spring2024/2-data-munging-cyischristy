import os
platform_agnostic_file_path = os.path.join("data", "GLB.Ts+dSST.txt")
with open(platform_agnostic_file_path, "r") as file:
    data = file.readlines()

clean_data = []
is_data = False

# Remove all the spaces
for line in data:
    line = line.strip()

# Remove all lines with notes
    if line.startswith("Year"):
        is_data = True
        header = line  
        continue
    if is_data and line:
        values = line.split()

# Handle the missing data
        if values[0].isdigit():
            for index, value in enumerate(values):
                if value in ('***', '****'):
                    values[index] = 'nan'
            
# Convert temperature to Fahrenheit
            for i in range(1, len(values) - 1):
                if values[i] != 'nan':
                    values[i] = "{:.1f}".format(float(values[i]) * 0.018)
            clean_data.append(values)

new_filename = "data/clean_data.csv"

# Write the data into the CSV file
with open(new_filename, "w") as csv_file:
    header_values = header.split()
    csv_file.write(",".join(header_values) + "\n")

    for row in clean_data:
        csv_file.write(",".join(row) + "\n")
