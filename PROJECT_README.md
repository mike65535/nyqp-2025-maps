# NYQP 2025 Interactive County Map Project

## Project Overview
This project visualizes ham radio activity from the 2025 New York QSO Party contest by parsing Cabrillo log files and displaying county-level activity on an interactive map of New York State.

## Directory Structure
```
/home/mgilmer/Downloads/QSO_PARTIES/NYQP-2025/
├── logs/                          # 516 Cabrillo format .log files
│   ├── wb0cjb.log
│   ├── wa9ley.log
│   └── ... (514 more)
└── analysis/                      # Processed data and visualizations
    ├── tx_from_counties.csv       # QSOs transmitted FROM each county
    ├── rx_to_counties.csv         # QSOs received TO each county
    ├── total_counties.csv         # Combined TX + RX activity
    ├── unique_callsigns_per_county.csv  # Unique callsigns per county
    ├── nyqp_interactive_map.html  # Interactive Leaflet/Folium map
    ├── NYQP_2025_Analysis_Summary.txt
    └── junk/                      # Static map variations (PNG files)
```

## Data Files

### Input Data
- **Location**: `/home/mgilmer/Downloads/QSO_PARTIES/NYQP-2025/logs/`
- **Format**: Cabrillo ASCII text files (.log extension)
- **Count**: 516 contest submissions
- **Coverage**: Worldwide submissions (99% US-based)
- **Content**: Each log contains:
  - Header metadata (callsign, location, category, etc.)
  - QSO records with frequency, mode, timestamp, and county exchanges

### Processed Data (CSV files)

#### tx_from_counties.csv
- QSOs transmitted FROM each county
- Columns: `County`, `TX_Count`
- 111 unique locations (includes non-NY locations)
- 60 NY counties with activity

#### rx_to_counties.csv
- QSOs received TO each county
- Columns: `County`, `RX_Count`
- 178 unique locations

#### total_counties.csv
- Combined transmit + receive activity
- Columns: `County`, `Total_Count`
- Primary data source for map visualization

#### unique_callsigns_per_county.csv
- Lists unique callsigns worked from each county
- Columns: `County`, `Unique_Callsigns`, `Callsigns` (comma-separated list)

## Interactive Map

### File
`nyqp_interactive_map.html` (1.4 MB)

### Technology Stack
- **Leaflet.js** - Interactive mapping library
- **Folium** - Python library that generated the HTML (likely)
- **D3.js** - Data visualization
- **Bootstrap** - UI framework
- **OpenStreetMap** - Base map tiles

### Features
- County boundaries with 3-character NYQP county abbreviations
- Color-coded by activity level (choropleth visualization)
- Interactive tooltips/popups on hover/click
- Zoom levels: 6-10 (focused on NY state)
- Responsive design

### Map Configuration
- Base tiles: OpenStreetMap
- Coordinate system: EPSG:3857 (Web Mercator)
- Initial view: Centered on New York State
- County data embedded directly in HTML (no external file dependencies)

## Key Statistics

### Top 10 Most Active NY Counties
1. **ERI** (Erie) - 5,823 QSOs
2. **ONO** (Onondaga) - 4,910 QSOs
3. **MON** (Monroe) - 3,692 QSOs
4. **NIA** (Niagara) - 3,232 QSOs
5. **RIC** (Richmond) - 2,800 QSOs
6. **SUF** (Suffolk) - 2,449 QSOs
7. **ORA** (Orange) - 2,084 QSOs
8. **ULS** (Ulster) - 1,866 QSOs
9. **STE** (Steuben) - 1,767 QSOs
10. **NAS** (Nassau) - 1,494 QSOs

### Overall Stats
- Total NY counties with activity: 60 out of 62 possible
- Total QSOs from NY counties: 57,885
- Most active region: Western NY (Erie, Monroe, Niagara)
- Strong NYC metro activity: Richmond, Suffolk, Nassau

## NY County Abbreviations (NYQP Standard)
The map uses standard 3-character NYQP county codes:
- ALB (Albany), ALL (Allegany), BRO (Bronx), BRX (Bronx alt)
- CAT (Cattaraugus), CAY (Cayuga), CHA (Chautauqua)
- CHE (Chemung), CLI (Clinton), COL (Columbia)
- COR (Cortland), DEL (Delaware), DUT (Dutchess)
- ERI (Erie), ESS (Essex), FRA (Franklin)
- FUL (Fulton), GEN (Genesee), GRE (Greene)
- HAM (Hamilton), HER (Herkimer), JEF (Jefferson)
- KIN (Kings/Brooklyn), LEW (Lewis), LIV (Livingston)
- MAD (Madison), MON (Monroe), MTG (Montgomery)
- NAS (Nassau), NEW (New York/Manhattan), NIA (Niagara)
- ONE (Oneida), ONO (Onondaga), ONT (Ontario)
- ORA (Orange), ORL (Orleans), OSW (Oswego)
- OTS (Otsego), PUT (Putnam), QUE (Queens)
- REN (Rensselaer), RIC (Richmond/Staten Island), ROC (Rockland)
- SAR (Saratoga), SCH (Schenectady), SCO (Schoharie)
- SCU (Schuyler), SEN (Seneca), STE (Steuben)
- STL (St. Lawrence), SUF (Suffolk), SUL (Sullivan)
- TIO (Tioga), TOM (Tompkins), ULS (Ulster)
- WAR (Warren), WAS (Washington), WAY (Wayne)
- WES (Westchester), WYO (Wyoming), YAT (Yates)

## Source Code

**GitHub Repository**: https://github.com/mike65535/nyqp-log-analyzer

The Python scripts that process the logs and generate visualizations are available on GitHub:

### Scripts

#### process_logs.py
Parses Cabrillo format log files and generates CSV statistics:
1. Reads all .log files from specified directory
2. Extracts QSO records and county exchange information
3. Aggregates data by county (TX, RX, totals, unique callsigns)
4. Generates the 4 CSV files

**Usage:**
```bash
python3 process_logs.py
# Enter path when prompted: /home/mgilmer/Downloads/QSO_PARTIES/NYQP-2025/logs
```

#### create_map_final.py
Generates static PNG choropleth maps with multiple color schemes:
- Uses geopandas with US Census TIGER/Line shapefiles
- Creates 6 map variations (viridis, plasma, cividis, inferno, YlGnBu, PuBu)
- Handles NYC metro area labels with leader lines
- Colorblind-accessible palettes

**Usage:**
```bash
python3 create_map_final.py
```

**Note**: The interactive HTML map (`nyqp_interactive_map.html`) was likely generated using Folium, but that script may be a separate version or manual creation.

## How to Use

### View the Interactive Map
```bash
# Open in browser
firefox /home/mgilmer/Downloads/QSO_PARTIES/NYQP-2025/analysis/nyqp_interactive_map.html

# Or
xdg-open /home/mgilmer/Downloads/QSO_PARTIES/NYQP-2025/analysis/nyqp_interactive_map.html
```

### Analyze the Data
```bash
cd /home/mgilmer/Downloads/QSO_PARTIES/NYQP-2025/analysis

# View top counties by activity
head -20 total_counties.csv

# Count unique callsigns in a specific county
grep "^ERI," unique_callsigns_per_county.csv
```

## Future Enhancements
- [ ] Add the Python processing script to repository
- [ ] Add time-based analysis (QSOs per hour)
- [ ] Add band/mode breakdown per county
- [ ] Add operator category analysis
- [ ] Create comparison with previous years
- [ ] Add DX (non-NY) activity visualization
- [ ] Generate summary statistics dashboard

## Dependencies (for regenerating)
If recreating the processing script, you'll need:
```bash
pip install folium pandas geopandas matplotlib
```

## Contact
Project for analyzing NYQP 2025 contest results.
Processing date: November 21, 2025
