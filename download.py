import requests
from bs4 import BeautifulSoup
import os
import re

YEARS = [2010, 2020]

URLS = {
    2010: "https://www2.census.gov/geo/docs/reference/codes/files/",
    2020: "https://www2.census.gov/geo/docs/reference/codes2020/cou/",
}

OUTPUT_DIRS = {2010: "fips_2010/", 2020: "fips_2020/"}

OUTPUT_FILE_NAMES = {2010: "fips_2010.txt", 2020: "fips_2020.txt"}

FILE_PATTERNS = {2010: r"st.*cou\.txt$", 2020: r"st.*cou2020\.txt$"}

# The 2020 files already include headers, so we set it to None.
HEADERS = {2010: "STATE,STATEFP,COUNTYFP,COUNTYNAME,CLASSFP", 2020: None}

for year in YEARS:
    os.makedirs(OUTPUT_DIRS[year], exist_ok=True)

    response = requests.get(URLS[year])
    soup = BeautifulSoup(response.text, "html.parser")

    pattern = re.compile(FILE_PATTERNS[year])
    links = [
        link.get("href")
        for link in soup.find_all("a")
        if link.get("href") and pattern.match(link.get("href"))
    ]

    all_lines = []
    write_headers = True

    for link in links:
        file_url = URLS[year] + link
        file_response = requests.get(file_url)

        file_content = file_response.text.strip()
        lines = file_content.split("\n")

        with open(os.path.join(OUTPUT_DIRS[year], link), "w") as state_file:
            state_file.write(file_content + "\n")

        if write_headers:
            if HEADERS[year]:
                all_lines.append(HEADERS[year])
            else:
                all_lines.append(lines[0])
            write_headers = False

        all_lines.extend(lines[1:])

    with open(OUTPUT_FILE_NAMES[year], "w") as outfile:
        outfile.write("\n".join(all_lines))
