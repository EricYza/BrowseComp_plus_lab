# How to Use Visualization

This guide explains how to visualize the trajectories of the Tongyi-DeepResearch agent using the SAS project visualization tool.

## Prerequisites

1.  **BrowseComp-Plus Lab**: You should have run the agent and generated output files (JSON format) in a directory (e.g., `runs/tongyi`).
2.  **SAS Project**: You need to have the `sas` project set up locally.

## Step 1: Generate Run Data

Run the Tongyi client as usual. The `--store-raw` flag is enabled by default, which ensures that the raw message history (including `<think>`, `<tool_call>`, etc.) is saved. This is required for visualization.

Example command:
```bash
python search_agent/tongyi_client.py \
  --query topics-qrels/queries_small.tsv \
  --output-dir runs/my_experiment \
  --searcher-type bm25 \
  --index-path indexes/bm25
```

## Step 2: Convert Data to SAS Format

Use the provided conversion script to merge the individual run files into a single JSONL file compatible with the SAS visualizer.

```bash
python scripts_evaluation/convert_to_sas.py \
  --input-dir runs/my_experiment \
  --output-file Traj_MyExperiment.jsonl
```

*   `--input-dir`: The directory containing your `run_*.json` files.
*   `--output-file`: The path where the converted JSONL file will be saved.

## Step 3: Run the Visualization

Since you have copied the `sas` project into your workspace, you can run the visualization script directly.

```bash
# Navigate to the sas directory
cd sas

# Run the viewer
python3 trajectory_viewer.py \
  --traj-path viz/public/Webdancer/Traj_Webdancer_GAIA_Level3.json \
  --deepresearch-path ../Traj_MyExperiment.jsonl
```

*   `--traj-path`: Path to the reference trajectory file (relative to the `sas` folder).
*   `--deepresearch-path`: Path to your converted Tongyi-DeepResearch trajectory file (relative to the `sas` folder, so we use `../` to go back to the workspace root).

After running the command, the script should launch a local server. Follow the instructions printed in the terminal (usually opening `http://localhost:3000` or similar) to view it in your browser.

## Troubleshooting

*   **Missing Raw Data**: If the conversion script warns about missing `raw_messages`, make sure you didn't explicitly disable `--store-raw` when running the client.
*   **Visualization Errors**: Ensure the JSONL format is correct. Each line should be a valid JSON object containing `question` and `messages` fields.
