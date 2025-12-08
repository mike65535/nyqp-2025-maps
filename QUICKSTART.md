# Quick Start: From Cabrillo Logs to Interactive Maps

Complete workflow to generate animated and static maps from contest log files.

## Prerequisites

- Python 3.6+
- Folder of Cabrillo `.log` files
- County boundary GeoJSON file for your state

## Step-by-Step Process

### 1. Organize Your Files

```bash
mkdir -p ~/contest-maps
cd ~/contest-maps

# Create directory structure
mkdir logs
mkdir output

# Copy your Cabrillo logs
cp /path/to/your/*.log logs/
```

### 2. Get County Boundaries

Download GeoJSON for your state's counties:

**Option 1: US Census Bureau (Most Reliable)**
```bash
# Download 500k resolution (good balance of detail/size)
wget https://www2.census.gov/geo/tiger/GENZ2022/shp/cb_2022_us_county_500k.zip
unzip cb_2022_us_county_500k.zip

# Convert shapefile to GeoJSON (requires ogr2ogr)
ogr2ogr -f GeoJSON -where "STATEFP='36'" ny-counties.json cb_2022_us_county_500k.shp
# Replace '36' with your state FIPS code (NY=36, CA=06, TX=48, etc.)
```

**Option 2: Pre-made GeoJSON (Easiest)**
- Eric Celeste's collection: https://eric.clst.org/tech/usgeojson/
- Click your state → Download GeoJSON
- Save as `output/STATE-counties-boundaries.json`

**Option 3: Natural Earth Data**
```bash
# Download from: https://www.naturalearthdata.com/downloads/10m-cultural-vectors/
# Get "Admin 2 – Counties" dataset
```

**Option 4: GitHub Sources**
- Plotly datasets: https://github.com/plotly/datasets/tree/master
- Look for state-specific county files

**For New York (already included):**
- File: `ny-counties-boundaries.json` (already in repo)
- No download needed

**State FIPS Codes (for Census data):**
- NY = 36, CA = 06, TX = 48, FL = 12, PA = 42
- Full list: https://www.census.gov/library/reference/code-lists/ansi.html

**Verify your GeoJSON:**
```bash
# Check it has county features
head -20 your-counties.json
# Should see "type": "FeatureCollection" and county names
```

### 3. Identify Mobile Stations

Find which stations were mobile by checking log headers:

```bash
grep "CATEGORY:" logs/*.log | grep -i mobile
```

Example output:
```
logs/k2a.log:CATEGORY: MOBILE
logs/n2t.log:CATEGORY: MOBILE
```

Make a list of these callsigns.

### 4. Configure the Contest

Edit `contest_config.json`:

```json
{
  "contest_name": "NYQP 2025",
  "state": "NY",
  "state_name": "New York",
  "logs_directory": "/full/path/to/logs",
  "output_directory": "/full/path/to/output",
  "mobile_callsigns": [
    "K2A", "N2T", "K2V", "N2CU"
  ],
  "county_codes": {
    "ALB": "Albany",
    "BRM": "Broome",
    ...
  }
}
```

**Important:** 
- Use full absolute paths
- List ALL mobile callsigns (without /M suffix)
- Include all county code mappings for your state

### 5. Generate Data Files

Run the data extraction script:

```bash
./generate_contest_data.py
```

This creates:
- `output/mobile_tracks.json` - Mobile movement timeline
- `output/timeline_data.json` - All QSOs chronologically

**Verify output:**
```bash
ls -lh output/*.json
```

You should see both files with reasonable sizes.

### 6. Build Static Map

Generate the interactive heat map:

```bash
./build_maps.py
```

This creates:
- `output/ny_interactive_map.html` - Static county heat map with mobile markers

**Test it:**
```bash
firefox output/ny_interactive_map.html
# or
google-chrome output/ny_interactive_map.html
```

### 7. Build Animated Map (Manual)

The animated map currently requires manual setup:

1. Copy the template:
```bash
cp nyqp_2025_animated.html output/my_contest_animated.html
```

2. Edit the file and replace embedded data:
   - Find `const boundaries = {...}` - replace with your state's GeoJSON
   - Find `const mobileTracks = {...}` - replace with your mobile_tracks.json content
   - Find `let timelineData = [...]` - replace with your timeline_data.json content
   - Update title and state name

3. Open in browser:
```bash
firefox output/my_contest_animated.html
```

## Complete Example

```bash
# 1. Clone the repository
git clone git@github.com:mike65535/nyqp-2025-maps.git
cd nyqp-2025-maps

# 2. Copy your logs
cp ~/Downloads/contest-logs/*.log ../logs/

# 3. Find mobiles
grep "CATEGORY:" ../logs/*.log | grep -i mobile

# 4. Edit config
nano contest_config.json
# Update paths, callsigns, counties

# 5. Generate data
./generate_contest_data.py

# 6. Build maps
./build_maps.py

# 7. View results
firefox ny_interactive_map.html
firefox nyqp_2025_animated.html
```

## Troubleshooting

**"No such file or directory" when running scripts**
```bash
chmod +x generate_contest_data.py build_maps.py
```

**"No mobile tracks found"**
- Check that callsigns in config match log filenames (case-insensitive)
- Verify logs are in the correct directory
- Check log files are valid Cabrillo format

**"County not found" errors**
- Ensure all county codes in logs are in your `county_codes` mapping
- Check for typos in 3-letter county abbreviations

**Map shows no data**
- Verify JSON files were created and contain data
- Check browser console (F12) for JavaScript errors
- Ensure GeoJSON county names match your county_codes mapping

## File Outputs

After successful run, you'll have:

```
output/
├── mobile_tracks.json          # Mobile movement data
├── timeline_data.json          # All QSOs timeline
├── ny_interactive_map.html     # Static heat map
└── ny-counties-boundaries.json # County boundaries
```

Plus manually created:
```
├── my_contest_animated.html    # Animated timeline map
```

## Next Steps

- Share HTML files (they're standalone, no server needed)
- Commit changes to git
- Push to GitHub for backup
- Adapt for next year's contest

## For Other State Contests

1. Get new county boundaries GeoJSON
2. Update `contest_config.json` with new state/counties
3. Copy new log files
4. Run `./generate_contest_data.py`
5. Run `./build_maps.py`
6. Manually adapt animated template

## Need Help?

- Check `README.md` for detailed documentation
- See `GITHUB_SETUP.md` for version control
- Review example `contest_config.json` for format
