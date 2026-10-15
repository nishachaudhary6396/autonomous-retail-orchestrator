# Autonomous Retail Inventory Orchestration

## Project Overview

An AI-powered, multi-agent pipeline that turns raw retail transaction data into a clear, explained procurement decision — automatically.

Upload a CSV of retail transactions and the pipeline will ingest and stage the data in PostgreSQL, profile it, compute sales analytics, and run it through five sequential AI agents that check data quality, assess warehouse readiness, forecast demand, plan inventory reorders, and issue a final approval — all visible live in a Streamlit dashboard.

## Features

**CSV ingestion** — load, validate, and clean raw retail transaction exports
**PostgreSQL staging** — a single source of truth for every downstream step
**Data profiling & sales analytics** — nulls, duplicates, revenue, top products, top customers, monthly trend
**Sequential multi-agent pipeline** built with **LangGraph**:

- **Quality Agent** — scores data quality and flags issues
- **Warehouse Agent** — judges whether the data is ready for warehouse use
- **Demand Agent** — forecasts high/medium/low demand products
- **Inventory Agent** — builds a priority/standard reorder plan
- **Approval Agent** — issues the final go/no-go procurement decision
Powered by **Groq (Llama 3.3)** via LangChain, with every agent's output forced into a strict **Pydantic** schema
**Streamlit dashboard** — run the whole pipeline and inspect every stage's output in dedicated tabs

## Architecture

CSV Upload
    │
    ▼
Ingestion (load → validate → transform)
    │
    ▼
PostgreSQL Staging Table
    │
    ▼
Profiling & Sales Analytics
    │
    ▼
LangGraph Agent Pipeline
    │
    ├── Quality Agent
    ├── Warehouse Agent
    ├── Demand Agent
    ├── Inventory Agent
    └── Approval Agent
    │
    ▼
Final Procurement Decision
    │
    ▼
Streamlit UI (live results)


## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.12 |
| Data Processing | Polars, Pandas, NumPy |
| Database | PostgreSQL (Neon) + SQLAlchemy |
| Agent Orchestration | LangGraph |
| LLM Provider | Groq (Llama 3.3 70B) via LangChain |
| Data Validation | Pydantic / pydantic-settings |
| UI | Streamlit |


## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/nishachaudhary6396/autonomous-retail-orchestrator
cd autonomous-retail-orchestrator
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv .venv
```

**Activate the virtual environment:**

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

### 3. Set up the database

Run `database_neon.sql` against your PostgreSQL or Neon instance to create the staging schema.

### 4. Configure environment variables

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
DATABASE_URL=postgresql+psycopg://<user>:<password>@<host>/<database>?sslmode=require
```

### 5. Run the app

```bash
streamlit run app/ui/streamlit_app.py
```
Then, from the sidebar:

1. Upload a CSV file and click **Load into staging table**.
2. Click **Run full pipeline**.
3. View the results in the following tabs:
   - **Analytics**
   - **Data Quality**
   - **Warehouse Readiness**
   - **Demand Forecast**
   - **Inventory Plan**
   - **Final Approval**

##  Expected CSV Columns

The uploaded file should match the classic Online Retail transaction format:

| Column | Description |
|---|---|
| InvoiceNo | Unique invoice/transaction ID |
| StockCode | Product/SKU code |
| Description | Product description |
| Quantity | Units sold |
| InvoiceDate | Transaction date/time |
| UnitPrice | Price per unit |
| CustomerID | Customer ID |
| Country | Customer's country |

##  Running Tests

Run the following command from the project root directory:

```bash
pytest
```

Tests cover ingestion (loader, transformer, validator), the database layer, profiling, analytics, the LLM wrapper, and the agent graph.

