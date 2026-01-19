## Part 1 – CLI based TOPSIS Implementation

This part implements the TOPSIS algorithm as a **Command Line Interface (CLI)** program.

### Features
- Accepts input CSV file
- Accepts weights and impacts via command line
- Generates output CSV with TOPSIS score and rank

### Command to run
```bash
python topsis.py data.csv "1,1,1,1,1" "+,+,-,+,+" result.csv
