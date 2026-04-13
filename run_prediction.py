import argparse
import os
import sys
import pandas as pd
import numpy as np
from prediction import get_prediction

REQUIRED_COLUMNS = ["C (wt%)", "H (wt%)", "O (wt%)", "N (wt%)", "S (wt%)",
    "H/C (wt%)", "FC (wt%)", "Ash (wt%)", "VM/FC (wt%)",
    "CL (wt%)", "HC (wt%)", "LG (wt%)",
    "Temp (°C)", "Time (min)", "HR (°C/min)"]

def check_columns(df):
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        print("\nERROR: Missing columns in your CSV:")
        for c in missing:
            print(f"  - {c}")
        print(f"\nRequired: {', '.join(REQUIRED_COLUMNS)}\n")
        sys.exit(1)

def check_models(target):
    model_dir = os.path.join("models", target)
    if not os.path.isdir(model_dir):
        print(f"\nERROR: Model folder not found: '{model_dir}'")
        sys.exit(1)
    pkl_files = [f for f in os.listdir(model_dir) if f.endswith(".pkl") and "TabPFN" in f]
    if not pkl_files:
        print(f"\nERROR: No TabPFN .pkl files found in '{model_dir}'\n")
        sys.exit(1)
    print(f"Found {len(pkl_files)} model(s) in '{model_dir}'")

def build_ndata(df):
    ndata = {}
    for i, row in df.iterrows():
        sample_id = str(row.get("Samples", f"sample_{i+1}"))
        ndata[sample_id] = row[REQUIRED_COLUMNS].values.astype(float)
    return ndata

def main():
    parser = argparse.ArgumentParser(
        description="Predict biochar properties from your input CSV.",
        epilog="Example: python run_prediction.py --input example/Example_input.csv --target HHV")
    parser.add_argument("--input",  required=True, help="Path to your input CSV file")
    parser.add_argument("--target", required=True, choices=["HHV", "Yield", "CER"], help="Target to predict")
    parser.add_argument("--output", default="results.csv", help="Output CSV path (default: results.csv)")
    args = parser.parse_args()

    print(f"\nInput : {args.input}")
    print(f"Target: {args.target}")
    print(f"Output: {args.output}\n")

    if not os.path.isfile(args.input):
        print(f"ERROR: File not found: '{args.input}'\n")
        sys.exit(1)

    df = pd.read_csv(args.input)
    print(f"Loaded {len(df)} sample(s)")

    check_columns(df)
    check_models(args.target)

    print(f"\nRunning {args.target} prediction...\n")
    results = get_prediction(build_ndata(df), target_type=args.target)

    out_df = pd.DataFrame([
        {"Samples": k, f"predicted_{args.target}": round(float(v), 4)}
        for k, v in results.items()
    ])
    out_df.to_csv(args.output, index=False)

    print(f"\nDone! Results saved to: {args.output}\n")
    print(out_df.to_string(index=False))
    print()


if __name__ == "__main__":
    main()