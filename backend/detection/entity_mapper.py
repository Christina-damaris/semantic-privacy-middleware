from backend.detection.entity_category_map import ENTITY_CATEGORY_MAP
from backend.detection.rule_loader import load_rule_table


rules = load_rule_table()


def get_entity_details(entity_type):
    """
    Returns category, action and risk
    for a detected entity.
    """

    category = ENTITY_CATEGORY_MAP.get(entity_type)

    if category is None:
        return None

    category_rules = rules.get(category)

    if category_rules is None:
        return None

    return {

        "category": category,

        "action": category_rules["action"],

        "risk": category_rules["risk"]

    }