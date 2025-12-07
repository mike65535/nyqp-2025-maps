# NYQP 2025 Mobile Tracking Map

Interactive visualization of mobile station activity during the 2025 New York QSO Party.

## Features

### Animated Map (`nyqp_2025_animated.html`)
- Real-time animation of 14 mobile stations moving through NY counties
- County heat map showing QSO activity intensity
- Unique vehicle icons and colors for each mobile
- Filter mobiles by counties operated (ALL, 5+, 10+)
- Variable speed playback (100x - 2000x)
- Interactive timeline scrubbing
- Time display in Zulu format (DD MMM YYYY HH:MM:SS Z)

### Static Interactive Map (`nyqp_interactive_map.html`)
- County heat map with QSO counts
- Mobile markers at final positions
- Popup details for counties and mobiles
- Color-coded activity levels

## Files

- `nyqp_2025_animated.html` - Animated timeline map (standalone)
- `nyqp_interactive_map.html` - Static interactive map
- `mobile_tracks.json` - Mobile station tracking data
- `ny-counties-boundaries.json` - NY county boundary GeoJSON
- `timeline_data.json` - Complete QSO timeline

## Scripts

### Data Generation
```bash
./generate_contest_data.py
```
Generates `mobile_tracks.json` and `timeline_data.json` from Cabrillo logs.

### Map Building
```bash
./build_maps.py
```
Builds HTML maps from data files and config.

## Configuration

Edit `contest_config.json` to customize:
- Contest name and state
- Mobile callsigns
- County codes and names
- Mobile icons and colors
- File paths

## Usage

Open any `.html` file in a modern web browser. No installation or server required.

## Mobile Stations (14)

AB1BL 🚙, K2A 🚐, K2G 🛻, K2Q 🚗, K2V 🚕, KQ2R 🚌, KV2X/M 🚎, N1GBE 🚓, N2B 🚑, N2CU 🚒, N2T 🚚, W1WV/M 🚛, WI2M 🚜, WT2X 🏎️

## Adapting for Other States

1. Copy `contest_config.json` and update:
   - State abbreviation and name
   - County codes (3-letter abbreviations)
   - Mobile callsigns
   - Paths

2. Obtain state county boundaries GeoJSON

3. Run data generation:
   ```bash
   ./generate_contest_data.py
   ```

4. Build maps:
   ```bash
   ./build_maps.py
   ```

5. Manually adapt `nyqp_2025_animated.html` template (TODO: automate)

## Development

Git repository tracks all changes. After modifications:
```bash
git add <files>
git commit -m "Description of changes"
```

## TODO

- [ ] Templatize animated map for automatic generation
- [ ] Add command-line arguments to scripts
- [ ] Support other contest formats beyond Cabrillo
- [ ] Add statistics dashboard

