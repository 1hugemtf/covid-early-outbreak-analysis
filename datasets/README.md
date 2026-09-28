# Source data

Six CSVs are preserved unchanged from the supplied DataCamp R project archive.

| File | Role |
|---|---|
| confirmed_cases_worldwide.csv | Worldwide cumulative snapshot, 22 January to 17 March 2020 |
| confirmed_cases_china_vs_world.csv | China and outside-China daily/cumulative series |
| confirmed_cases_by_country.csv | Outside-China province rows; aggregate daily cases before accumulating |
| who_events.csv | Archived contextual event labels |
| confirmed_cases_top7_outside_china.csv | Legacy precomputed table; audited but not used for plotting |
| coronavirus_dataset.csv | Broader archive ending 16 March; used only for snapshot comparison |

The analysis files reconcile with one another. The broader raw archive differs by 15 cases in the worldwide total on 16 March and lacks 17 March. It is not merged into the analysis snapshot. Geographic labels are retained as supplied. The notebook documents opening balances, negative corrections and repeated country-date records. Source-data rights remain with their respective owners.
