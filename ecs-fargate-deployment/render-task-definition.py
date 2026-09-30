"""Render a local ECS task definition without committing account identifiers."""
import json
import os
import re
from pathlib import Path
from string import Template

account = os.environ["AWS_ACCOUNT_ID"]
region = os.environ["AWS_REGION"]
if not re.fullmatch(r"[0-9]{12}", account):
    raise SystemExit("AWS_ACCOUNT_ID must contain exactly 12 digits")
if not re.fullmatch(r"[a-z]{2}(?:-[a-z]+)+-[0-9]+", region):
    raise SystemExit("AWS_REGION is invalid")
root = Path(__file__).resolve().parent
rendered = Template((root / "task-definition.template.json").read_text()).substitute(
    AWS_ACCOUNT_ID=account, AWS_REGION=region
)
(root / "task-definition.json").write_text(json.dumps(json.loads(rendered), indent=2) + "\n")
print("Rendered local task-definition.json (ignored by Git)")
