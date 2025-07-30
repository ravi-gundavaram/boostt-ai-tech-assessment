# boostt-ai-tech-assessment
Technical assessment for Boostt AI - causal inference, CUPED, synthetic control, and RL reward adapter.
# Boostt AI Tech Assessment

This repo implements a causal measurement pipeline including:
- Fractional factorial design
- CUPED variance reduction
- Synthetic control estimation
- Reward adapter for RL
- BigQuery schema and pipeline design

## Structure
- `design.py` — Resolution IV factorial matrix
- `cuped.ipynb` — Variance reduction using CUPED
- `synthetic_control.py` — Geo-based counterfactuals
- `reward_adapter.py` — Converts lift into proto message
- `schema.sql` — BigQuery DDL + scheduled queries
- `design.md` — Pipeline architecture for BigQuery + Vertex AI

## To Run
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
pytest
