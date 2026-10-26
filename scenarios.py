"""Five trials per original criterion; run_eval.py disables caching."""

SCENARIOS = [
    {"name": "matching query completes", "query": "graphic tee",
     "wardrobe": "example", "criterion": 1},
    {"name": "impossible query stops early", "query": "unobtainium astronaut ballgown",
     "wardrobe": "example", "criterion": 2},
    {"name": "selected item stays consistent", "query": "graphic tee",
     "wardrobe": "example", "criterion": 3},
    {"name": "fit card has required format and details", "query": "graphic tee",
     "wardrobe": "example", "criterion": 4, "item_id": "lst_006",
     "outfit": "Pair the graphic tee with baggy dark-wash jeans and chunky white sneakers."},
    {"name": "search respects requested budgets", "query": "graphic tee",
     "wardrobe": "example", "criterion": 5, "budgets": [10, 18, 24, 30, 50]},
]

WARDROBES = ("example", "empty")


def validate() -> list[str]:
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("query", "").strip():
            problems.append(f"scenario {i} has no query")
        if scenario.get("wardrobe") not in WARDROBES:
            problems.append(f"scenario {i} has an invalid wardrobe")
    return problems
