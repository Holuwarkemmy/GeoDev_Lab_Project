with open('wards.csv') as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area = float(parts[1])

    if area > 9:
        size = "large"
    else:
        size = "small"
    print (ward, "is", size)