import redis
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.transform import transform_function


def load_to_redis():

    r = redis.Redis(host= '192.168.64.1', port=6379, db=0, decode_responses=True)
    records = transform_function()

    for i in range(len(records)):
        r.delete(f"row_{i}")
        r.hset(f"row_{i}", mapping=records[i])