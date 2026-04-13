<h1 align="center">
  HYC-PFN
</h1>

<h4 align="center">Standalone program for the paper "HYC-PFN: A transformer-based foundation model for accurate and robust prediction of biomass-derived biochar properties"</h4>

<p align="center">
  <a href=""><img src="https://img.shields.io/github/stars/Cobonla/HYC-PFN?" alt="stars"></a>
  <a href=""><img src="https://img.shields.io/github/forks/Cobonla/HYC-PFN?" alt="forks"></a>
  <a href="https://github.com/Cobonla/HYC-PFN/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Cobonla/HYC-PFN" alt="license">
  </a>
</p>

<p align="center">
  <a href="#abstract">Abstract</a> •
  <a href="#introduction">Introduction</a> •
  <a href="#installation">Installation</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#citation">Citation</a>
</p>

<p align="center">
  <!-- <img width="4350" height="3234" alt="Image" src="https://github.com/user-attachments/assets/538dc520-02b2-4f45-9e39-7a6611e8f5b3" /> -->
</p>

---

## Abstract

Update soon!

---

## Introduction

This repository provides the standalone program for HYC-PFN. Please download `models.zip` from [Zenodo](https://doi.org/10.5281/zenodo.19548145) and unzip it to get the models for target prediction.

This tool predicts three key biochar properties from biomass input data using pre-trained TabPFN ensemble models:

| Target | Description |
|--------|-------------|
| **HHV** | Higher Heating Value (MJ/kg) |
| **Yield** | Biochar Yield (%) |
| **CER** | Char Recovery Ratio (%) |

---

## Installation

### Step 1 — Install Conda (if you don't have it)

Download and install **Miniconda** for your operating system: https://docs.conda.io/en/latest/miniconda.html

After installing, open **Anaconda Prompt** (Windows) or your **Terminal** (Mac/Linux).

### Step 2 — Download this repository

```shell
git clone https://github.com/Cobonla/HYC-PFN.git
```
```shell
cd HYC-PFN
```

> If you don't have `git`, download the ZIP from the green **Code** button on this page, unzip it, and open a terminal inside the unzipped folder.

### Step 3 — Download and unzip the models

Download `models.zip` from [Zenodo](https://doi.org/10.5281/zenodo.19547896) and place it inside the `HYC-PFN/` folder. After unzipping, you should see a `models/` folder containing three subfolders: `HHV/`, `Yield/`, and `CER/`.

```shell
unzip models.zip
```

### Step 4 — Create a new environment


```shell
conda create -n HYC-PFN python=3.9.18
```
```shell
conda activate HYC-PFN
```

### Step 5 — Install required packages

```shell
python -m pip install numpy==1.22.4 pandas==2.0.3 --no-cache-dir
```
```shell
python -m pip install tabpfn==6.2.0 --no-cache-dir
```
```shell
python -m pip install joblib==1.3.2 --no-cache-dir
```

---

## Getting Started

### Prepare your input file

Your input must be a CSV file with **one row per sample** and the following columns in this exact order:

| Column | Description |
|--------|-------------|
| `Samples` | Sample name or ID |
| `C (wt%)` | Carbon content |
| `H (wt%)` | Hydrogen content |
| `O (wt%)` | Oxygen content |
| `N (wt%)` | Nitrogen content |
| `S (wt%)` | Sulfur content |
| `H/C` | H/C atomic ratio |
| `FC (wt%)` | Fixed carbon |
| `Ash (wt%)` | Ash content |
| `VM/FC` | Volatile matter / Fixed carbon ratio |
| `CL (wt%)` | Cellulose content |
| `HC (wt%)` | Hemicellulose content |
| `LG (wt%)` | Lignin content |
| `Temp (°C)` | Pyrolysis temperature |
| `Time (min)` | Residence time |
| `HR (°C/min)` | Heating rate |

See `example/Example_input.csv` for a ready-to-use template. You can open it in Excel, fill in your own data, and save it as CSV.

### Run prediction

Replace `{HHV/Yield/CER}` with the property you want to predict:

```shell
python run_prediction.py --input example/Example_input.csv --target HHV
```
```shell
python run_prediction.py --input example/Example_input.csv --target Yield
```
```shell
python run_prediction.py --input example/Example_input.csv --target CER
```

To save results to a specific file, add `--output`:

```shell
python run_prediction.py --input example/Example_input.csv --target HHV --output my_results.csv
```

Results are printed to the screen and saved as a CSV file with columns `Samples` and `predicted_HHV` (or `predicted_Yield` / `predicted_CER`).

### Troubleshooting

**`ModuleNotFoundError`** — You may have forgotten to activate the environment. Run `conda activate HYC-PFN` and try again.

**`FileNotFoundError: models/HHV`** — Make sure you are running the command from inside the `HYC-PFN/` folder.

**Column name error** — Check that your CSV column names match exactly as shown in the table above, including spaces and special characters like `°`.

---

## Citation

If you use this code or part of it, please cite the following paper:

```bibtex
@article{phan2026hycpfn,
  title={HYC-PFN: A transformer-based foundation model for accurate and robust prediction of biomass-derived biochar properties},
  author={Phan, Le Thi, Nithiyanandam, Saraswathy, Zhang, Zilong, and Manavalan, Balachandran},
  journal={},
  volume={},
  pages={},
  year={2026},
  publisher={}
}
```

---

## License

See [LICENSE](https://github.com/Cobonla/HYC-PFN/blob/main/LICENSE) for details.
