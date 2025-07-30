# Architecture: Causal Measurement Pipeline with BigQuery + Vertex AI

This pipeline processes pre/post experiment data to deliver uplift metrics to Boostt AI's reinforcement learning (RL) system.

## Flow:
1. **Data Ingestion:**
   - Daily event-level data is ingested into `customer_daily` in BigQuery.
   - Includes treatment flag, geo, spend, and factorial factors.

2. **CUPED Adjustment:**
   - A scheduled query computes daily `theta` values and stores them in `cuped_theta`.
   - Adjusted post_spend is computed to reduce variance.

3. **Lift Calculation:**
   - `experiments_lift` stores CUPED-based lift % and confidence intervals.

4. **Design Matrix:**
   - `generate_ff_design()` creates Resolution IV designs for experimentation with multiple binary factors.

5. **Synthetic Control:**
   - For geolocked tests, a synthetic control is estimated using ridge regression.

6. **Reward Adapter:**
   - Lift metrics are converted to `Reward` messages using gRPC-compatible format.
   - These are sent to the RL service to optimize future experiment allocations.

## Diagram:

```mermaid
graph TD
    A[BigQuery: customer_daily] --> B[CUPED Adjustment]
    B --> C[Lift Calculation Table: experiments_lift]
    A --> D[Vertex AI: Synthetic Control]
    C --> E[gRPC Reward Adapter]
    D --> E
    E --> F[RL Budget Optimizer]
