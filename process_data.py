sales_data_paths = [
    "./data/daily_sales_data_0.csv",
    "./data/daily_sales_data_1.csv",
    "./data/daily_sales_data_2.csv",]

processed_data = []

def process_data(data):
    raw_data = {}
    processed_data = []

    for line in data[1:]: # Skip the header line
        parts = line.strip().split(",")
        product = parts[0]
        if "pink morsel" not in product:
            continue
        formatted_price = (parts[1])[1:].strip() # Remove the "$" sign
        price = float(formatted_price)
        quantity = int(parts[2])
        date = parts[3]
        region = parts[4]
        total = price * quantity

        if(date, region) not in raw_data:
            raw_data[(date, region)] = {
                "date": date,
                "total_sales": total,
                "region": region,
            }
        else:
            raw_data[(date, region)]["total_sales"] += total

    raw_data = dict(sorted(raw_data.items(), key=lambda item: item[0][0])) # Sort by date

    header = "date,region,total_sales"
    processed_data.append(header)
    for key, value in raw_data.items():
        string_value = f"{value['date']},{value['region']},{value['total_sales']:.2f}"
        processed_data.append(string_value)


    return processed_data


for path in sales_data_paths:
    with open(path, "r") as f:
        print(f"Processing {path}...")
        data = f.readlines()
        processed_data.append(process_data(data))

    
with open("./data/processed_sales_data.csv", "w") as f:
    for data in processed_data:
        for line in data:
            f.write(line + "\n")