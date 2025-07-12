import csv
import os

input_file = "lichess_db_puzzle.csv"  # <-- Update if your filename is different
output_dir = "puzzles"  # Directory to store the categorized puzzle files

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Define mate tags to filter (mateIn1 through mateIn6)
mate_ranges = range(1, 7)
mate_tags = {f"mateIn{i}" for i in mate_ranges}

# Initialize counters for each mate category
counts = {f"mateIn{i}": 0 for i in mate_ranges}
total_count = 0

# Create output file handlers
output_files = {}
for i in mate_ranges:
    output_files[f"mateIn{i}"] = open(os.path.join(output_dir, f"mate_in_{i}.fen"), "w")

try:
    with open(input_file, "r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            themes = row["Themes"].split()

            # Check which mate tag the puzzle has
            for mate_tag in mate_tags:
                if mate_tag in themes:
                    # Write FEN to the corresponding file
                    output_files[mate_tag].write(row["FEN"] + "\n")
                    counts[mate_tag] += 1
                    total_count += 1
                    break  # A puzzle should only belong to one mate category
finally:
    # Close all output files
    for file in output_files.values():
        file.close()

# Print summary
print(f"✅ Done! Extracted {total_count} mate puzzles to directory: {output_dir}")
for i in mate_ranges:
    mate_tag = f"mateIn{i}"
    output_path = os.path.join(output_dir, f"mate_in_{i}.fen")
    print(f"  - {counts[mate_tag]} mate-in-{i} puzzles saved to: {output_path}")
