"""A Python script to analyze the temperature data."""

import csv
import os

def calculate_decadal_average(cleaned_data: str) -> None:
    """Calculate the decadal average temperature."""
    cleaned_data = os.path.join("data", "clean_data.csv")
    with open(cleaned_data, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        clean_data = list(reader)[1:]

    annual_temp = list(zip(*clean_data))[13]

    for i in range(0, len(annual_temp), 10):
        if i + 10 > len(annual_temp):
            temps = annual_temp[i:]
            print(
                f"Average temperature after {1880+i}: {sum(map(float, temps))/len(temps):.2f} °F"
            )
        else:
            temps = annual_temp[i : i + 10]
            print(
                f"Average temperature for {1880+i}-{1890+i}: "
                f"{sum(map(float, temps))/len(temps):.2f} °F"
            )


if __name__ == "__main__":
    calculate_decadal_average("data/clean_data.csv")
