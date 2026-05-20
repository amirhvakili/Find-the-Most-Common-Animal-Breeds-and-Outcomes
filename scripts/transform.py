import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.extract import extract_function

def transform_function():
    raw_df = extract_function()
    records = raw_df.where(raw_df.notna(), other='').to_dict("records")
    return records