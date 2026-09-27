import json
import sys
from pathlib import Path


def norm(items):
    return " | ".join(str(x).lower() for x in items)


def contains_all(text, terms):
    return all(term.lower() in text for term in terms)


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: python3 grade_results.py results.json")

    cases = json.loads(Path("eval_cases.json").read_text())
    results = json.loads(Path(sys.argv[1]).read_text())
    by_id = {item["id"]: item for item in results}

    failures = []
    checks = 0

    for case in cases:
        result = by_id.get(case["id"])
        if result is None:
            failures.append(f'{case["id"]}: missing result')
            continue

        facts = norm(result.get("facts", []))
        hypotheses = norm(result.get("hypotheses", []))
        missing = norm(result.get("missing", []))

        criteria = [
            ("facts", contains_all(facts, case["fact_terms"])),
            ("hypotheses", contains_all(hypotheses, case["hypothesis_terms"])),
            ("missing", contains_all(missing, case["missing_terms"])),
            (
                "forbidden_fact",
                not any(term.lower() in facts for term in case["forbidden_fact_terms"]),
            ),
        ]

        for name, passed in criteria:
            checks += 1
            if not passed:
                failures.append(f'{case["id"]}: {name} failed')

    print(f"checks={checks}")
    print(f"failures={len(failures)}")
    for failure in failures:
        print(f"FAIL {failure}")

    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
