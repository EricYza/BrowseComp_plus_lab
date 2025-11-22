# Preparation
## python environment
3.10 

## Downloading the package
```bash
pip install -r requirements.txt
```
## Downloading the dataset
```bash
pip install datasets # ensure you have datasets
python scripts_build_index/decrypt_dataset.py --output data/browsecomp_plus_decrypted.jsonl --generate-tsv topics-qrels/queries.tsv
```
## set up java environment
```bash
conda install -c conda-forge openjdk=21
```

## Downloading Pre-Built Indexes
```bash
bash scripts_build_index/download_indexes.sh
```

# Run the dataset
```bash
python search_agent/tongyi_client.py --searcher-type bm25 --index-path indexes/bm25 --output-dir runs/bm25/tongyi --num-threads 10 --query topics-qrels/queries.tsv
```
It will take approximately 20 hours to run.

# Evaluate the result
```bash
python scripts_evaluation/evaluate_run.py --input_dir runs/bm25/tongyi --model hosted_vllm/Alibaba-NLP/Tongyi-DeepResearch-30B-A3B
```