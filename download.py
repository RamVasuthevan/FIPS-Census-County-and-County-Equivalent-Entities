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

OUTPUT_FILE_NAMES = {2010: "fips_2010.tsv", 2020: "fips_2020.tsv"}

FILE_PATTERNS = {2010: r"st.*cou\.txt$", 2020: r"st.*cou2020\.txt$"}

# The 2020 files already include headers, so we set it to None.
HEADERS = {2010: "STATE\tSTATEFP\tCOUNTYFP\tCOUNTYNAME\tCLASSFP", 2020: None}

# The delimiters used in the files for each year
DELIMITER = {2010: ",", 2020: "|"}


def download_data():
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

            # Replace the appropriate character with tabs
            file_content = file_response.text.strip().replace(DELIMITER[year], "\t")
            lines = file_content.split("\n")

            with open(
                os.path.join(OUTPUT_DIRS[year], link.replace(".txt", ".tsv")), "w"
            ) as state_file:
                # Add headers to the individual state files
                if HEADERS[year]:
                    state_file.write(HEADERS[year] + "\n")
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
            outfile.write("\n")  # Make sure the file ends with a newline


if __name__ == "__main__":
    download_data()
