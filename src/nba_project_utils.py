from __future__ import annotations
from pathlib import Path
import re
import unicodedata

BASE_DIR = Path(__file__).resolve().parent

# input data files
SALARY_FILE = BASE_DIR / "data" / "nba_player_salaries.csv"
STATS_FILE = BASE_DIR / "data" / "nba_player_stats.csv"

# join output files
JOINED_FILE = BASE_DIR / "data"  / "nba_joined_analysis.csv"
UNMATCHED_SALARY_FILE = BASE_DIR / "data"  / "unmatched_salary_rows.csv"
UNMATCHED_STATS_FILE = BASE_DIR / "data"  / "unmatched_stats_rows.csv"

# model output files
MODEL_RESULTS_FILE = BASE_DIR / "data"  / "regression_model_results.csv"
TOP_OVER_EXPECTED_FILE = BASE_DIR / "data"  / "regression_top_over_expected.csv"
TOP_UNDER_EXPECTED_FILE = BASE_DIR / "data"  / "regression_top_under_expected.csv"
REGRESSION_SUMMARY_FILE = BASE_DIR / "data"  / "regression_summary.csv"
REGRESSION_COEFFICIENTS_FILE = BASE_DIR / "data"  / "regression_coefficients.csv"

# figures directory
FIGURES_DIR = BASE_DIR / "data" / "figures"

def normalize_player_name(name: object) -> str:
    """Normalize NBA player names across Basketball Reference and NBA API."""
    text = "" if name is None else str(name)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = text.replace(".", "")
    text = text.replace("'", "")
    tokens = re.sub(r"[^a-z0-9]+", " ", text).split()
    suffixes = {"jr", "sr", "ii", "iii", "iv", "v"}
    tokens = [token for token in tokens if token not in suffixes]
    return " ".join(tokens)

def ensure_figures_dir() -> Path:
    """Ensure the figures directory exists, creating it if necessary, and return the path."""
    FIGURES_DIR.mkdir(exist_ok=True)
    return FIGURES_DIR

def season_sort_key(season: str) -> int:
    """Extract the starting year from a season string (e.g., '2020-21' -> 2020) for sorting purposes."""
    return int(str(season).split("-")[0])