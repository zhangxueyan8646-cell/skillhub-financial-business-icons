#!/usr/bin/env python3
"""Search the bundled catalog; output candidates, never silently choose a variant."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def normalize(text):
    return re.sub(r"[\s+：:／/_-]+", "", text).casefold()


def search(query):
    rows = json.loads((ROOT / "references/icon-index.json").read_text())
    q = normalize(query)
    if not q:
        return {"status": "missing", "candidates": []}
    exact = [r for r in rows if q in (normalize(r['name']), normalize(r['id']))]
    if exact:
        found = exact
    elif any(q in {normalize(k) for k in r['keywords']} for r in rows):
        found = [r for r in rows if q in {normalize(k) for k in r['keywords']}]
    else:
        scored = []
        for row in rows:
            # Explicit market qualifiers must agree. Avoid A/H market substitution.
            words = row['name'] + ' '.join(row['keywords'])
            if any(m in query and m not in words for m in ('港股', 'A股', 'ETF', '期货')):
                continue
            keys = {normalize(k) for k in row['keywords'] if len(normalize(k)) >= 2}
            hits = [k for k in keys if k in q]
            name = normalize(row['name'])
            score = sum(len(k) for k in hits) + (len(name) * 3 if name in q else 0)
            # One generic business word is insufficient for an automatic match.
            if score >= 4:
                scored.append((score, row))
        scored.sort(key=lambda item: (-item[0], item[1]['id']))
        found = [r for s, r in scored if s == scored[0][0]] if scored else []
    return {
        "status": "missing" if not found else "ambiguous" if len(found) > 1 else "candidate",
        "note": "检索建议需结合业务语境核对；不自动替代缺失图标。",
        "candidates": [{k: r[k] for k in ('id', 'name', 'shape', 'suggestedUse', 'kind', 'reusePath', 'preview')} for r in found],
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query')
    args = parser.parse_args()
    print(json.dumps(search(args.query), ensure_ascii=False, indent=2))
