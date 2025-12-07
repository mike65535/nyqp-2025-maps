#!/usr/bin/env python3
"""
Generate mobile tracking data and timeline for state QSO party contests.
Configurable for any state with county-based multipliers.
"""

import json
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime

class ContestDataGenerator:
    def __init__(self, logs_dir, state_abbrev, mobile_callsigns):
        self.logs_dir = Path(logs_dir)
        self.state_abbrev = state_abbrev
        self.mobile_callsigns = set(mobile_callsigns)
        
    def parse_qso_line(self, line):
        """Parse a Cabrillo QSO line."""
        parts = line.split()
        if len(parts) < 11:
            return None
            
        return {
            'freq': parts[1],
            'mode': parts[2],
            'date': parts[3],
            'time': parts[4],
            'tx_call': parts[5],
            'tx_rst': parts[6],
            'tx_county': parts[7],
            'rx_call': parts[8],
            'rx_rst': parts[9],
            'rx_county': parts[10]
        }
    
    def generate_mobile_tracks(self):
        """Generate mobile_tracks.json from log files."""
        mobile_tracks = defaultdict(list)
        
        for mobile in self.mobile_callsigns:
            log_file = self.logs_dir / f"{mobile.lower()}.log"
            if not log_file.exists():
                print(f"Warning: Log file not found for {mobile}")
                continue
                
            with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    if not line.startswith('QSO:'):
                        continue
                        
                    qso = self.parse_qso_line(line)
                    if not qso:
                        continue
                    
                    timestamp = f"{qso['date'][:4]}-{qso['date'][4:6]}-{qso['date'][6:8]} {qso['time'][:2]}:{qso['time'][2:4]}:{qso['time'][4:6]}"
                    county = qso['tx_county']
                    
                    # Only add if county changed or first entry
                    if not mobile_tracks[mobile] or mobile_tracks[mobile][-1]['county'] != county:
                        mobile_tracks[mobile].append({
                            'timestamp': timestamp,
                            'county': county
                        })
        
        return dict(mobile_tracks)
    
    def generate_timeline(self):
        """Generate timeline data from all logs."""
        timeline = []
        
        for log_file in self.logs_dir.glob('*.log'):
            with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    if not line.startswith('QSO:'):
                        continue
                        
                    qso = self.parse_qso_line(line)
                    if not qso:
                        continue
                    
                    # Only include QSOs where TX is from target state
                    if len(qso['tx_county']) == 3:  # State county code
                        timestamp = f"{qso['date'][:4]}-{qso['date'][4:6]}-{qso['date'][6:8]} {qso['time'][:2]}:{qso['time'][2:4]}:{qso['time'][4:6]}"
                        timeline.append([timestamp, qso['tx_county']])
        
        # Sort by timestamp
        timeline.sort(key=lambda x: x[0])
        return timeline
    
    def save_data(self, output_dir):
        """Generate and save all data files."""
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True)
        
        print("Generating mobile tracks...")
        mobile_tracks = self.generate_mobile_tracks()
        with open(output_dir / 'mobile_tracks.json', 'w') as f:
            json.dump(mobile_tracks, f, indent=2)
        print(f"  Found {len(mobile_tracks)} mobiles")
        
        print("Generating timeline...")
        timeline = self.generate_timeline()
        with open(output_dir / 'timeline_data.json', 'w') as f:
            json.dump(timeline, f)
        print(f"  Generated {len(timeline)} QSO entries")
        
        print(f"\nData files saved to {output_dir}/")
        return mobile_tracks, timeline


if __name__ == '__main__':
    # NYQP 2025 Configuration
    LOGS_DIR = '/home/mgilmer/Downloads/QSO_PARTIES/NYQP-2025/logs'
    OUTPUT_DIR = '/home/mgilmer/Downloads/QSO_PARTIES/NYQP-2025/analysis'
    STATE = 'NY'
    
    # Mobile callsigns (from CATEGORY: MOBILE in log headers)
    MOBILES = [
        'AB1BL', 'AD4EB', 'K2A', 'K2G', 'K2Q', 'K2V', 'KQ2R', 'KV2X/M',
        'N1GBE', 'N2B', 'N2CU', 'N2T', 'W1WV/M', 'WI2M', 'WT2X'
    ]
    
    generator = ContestDataGenerator(LOGS_DIR, STATE, MOBILES)
    generator.save_data(OUTPUT_DIR)
