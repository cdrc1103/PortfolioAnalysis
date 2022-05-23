# Project Structure

## Main
- Runs the dashboard app
- Constructs instances of the classes defined in `lib`
- Runs class methods
## Lib
### 1. Dashboard
### 2. Data Sources
- Downloader Class
    - Connects to API
- Functions: 
### 3. Portfolio
- Portfolio Class
    - Connects to `portfolio.db`
    - Loads `depot` data
- Functions: Perform analytics operations on portfolio data
    - triggers fetching of portfolio data from data sources based on depot
    - save downloaded data to a data base
    - returns the analytics results
## Parameters
- stores static configuration data