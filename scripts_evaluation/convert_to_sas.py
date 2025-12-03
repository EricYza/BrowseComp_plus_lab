import argparse
import json
import glob
import os
from pathlib import Path


def convert_to_sas(input_dir, output_file):
    input_path = Path(input_dir)
    output_path = Path(output_file)

    # Get all run_*.json files
    run_files = list(input_path.glob("run_*.json"))
    print(f"Found {len(run_files)} run files in {input_dir}")

    count = 0
    with open(output_path, "w", encoding="utf-8") as outfile:
        for run_file in run_files:
            try:
                with open(run_file, "r", encoding="utf-8") as infile:
                    data = json.load(infile)

                if "raw_messages" not in data:
                    print(
                        f"Skipping {run_file.name}: 'raw_messages' not found. Did you run with --store-raw?"
                    )
                    continue

                messages = data["raw_messages"]

                # Extract question from the first user message
                question = ""
                for msg in messages:
                    if msg["role"] == "user":
                        question = msg["content"]
                        break

                # Construct the SAS format object
                sas_entry = {
                    "question": question,
                    "Ground truth": "",  # We don't have ground truth in the run output usually
                    "messages": messages,
                }

                # Write to JSONL
                outfile.write(json.dumps(sas_entry, ensure_ascii=False) + "\n")
                count += 1

            except Exception as e:
                print(f"Error processing {run_file.name}: {e}")

    print(
        f"Conversion complete. Converted {count} files. Output saved to {output_file}"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert BrowseComp-Plus run outputs to SAS visualization format"
    )
    parser.add_argument(
        "--input-dir", required=True, help="Directory containing run_*.json files"
    )
    parser.add_argument(
        "--output-file", required=True, help="Path to the output JSONL file"
    )

    args = parser.parse_args()

    convert_to_sas(args.input_dir, args.output_file)
