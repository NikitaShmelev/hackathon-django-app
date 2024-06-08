from GTFS import *
import os


files: list[str] = [
    "transfers.txt",
    "agency.txt",
    "calendar_dates.txt",
    "stop_times.txt",
    "shapes.txt",
    "trips.txt",
    "feed_info.txt",
    "stops.txt",
    "calendar.txt",
    "routes.txt",
]

dir_name: str = "GTFS"


parsed_data: dict[str, list[dict[str, str]]] = {}

for file_name in files:
    file = open(f"{dir_name}/{file_name}")
    parsed_data[file_name] = []
    headers: None | list[str] = None
    for line_num, line in enumerate(file.readlines()):
        if line_num == 0:
            headers = line.strip().split(",")
        else:
            line_data = line.strip().split(",")
            breakpoint()
            print()

    break
