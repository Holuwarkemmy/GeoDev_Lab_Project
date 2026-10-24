import csv

file = "data/processed/Eti_Osa_settlement_extents.csv"

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return{
        "Minimun":min(values),
        "maximum":max(values),
        "Count":len(values)
    }

first_result = inspect_column(file, "block_area_sqm")
print ("Block area in sqm: ", first_result)

second_result = inspect_column(file, "building_count")
print ("Building Count: ", second_result)