# FIPS Cenus County and County Equivalent Entities

2010 and 2020 Census codes for Counties and County Equivalent Entities sorted by "STATEFP" then "COUNTYFP"

| Field Name | Field Description | Example |
| --- | --- | --- |
| STATE | State postal abbreviation | TX |
| STATEFP | State FIPS code | 48 |
| COUNTYFP | County FIPS code | 041 |
| COUNTYNS | County NS code | 01383806 |
| COUNTYNAME | County name and legal/statistical area description | Brazos County |
| CLASSFP | FIPS class code | H1 |
| FUNCSTAT | Functional status (*Only available for 2020*) | A |

### FIPS Class Codes (CLASSFP)

- **H1:** Identifies an active county or statistically equivalent entity that does not qualify under subclass C7 or H6.
- **H4:** Identifies a legally defined inactive or nonfunctioning county or statistically equivalent entity that does not qualify under subclass H6.
- **H5:** Identifies census areas in Alaska, a statistical county equivalent entity.
- **H6:** Identifies a county or statistically equivalent entity that is coextensive in area or governmentally consolidated with an incorporated place, part of an incorporated place, or a consolidated city.
- **C7:** Identifies an incorporated place that is an independent of any county.

### Functional Status Codes (FUNCSTAT) 

- **A:** Identifies an active government providing primary general-purpose functions.
- **B:** Identifies an active government that is partially consolidated with another government but with separate officials providing primary general-purpose functions.
- **C:** Identifies an active government consolidated with another government with a single set of officials.
- **F:** Identifies a fictitious entity created to fill the Census Bureau's geographic hierarchy.
- **G:** Identifies an active government that is subordinate to another unit of government.
- **N:** Identifies a nonfunctioning legal entity.
- **S:** Identifies a statistical entity.
