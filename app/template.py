from typing import Iterable, Dict, Optional

from app.validator import validate


def find_template_name(
    templates: Iterable[Dict[str, str]],
    query: Dict[str, str],
) -> Optional[str]:
    """Find first valid template name."""
    for t in templates:
        i = len(t) - 1
        for q_key, q_value in query.items():
            if q_key not in t.keys():
                continue

            t_type = t[q_key]
            q_type = validate(q_value)

            if t_type == q_type:
                i -= 1
                if i == 0:
                    return t.get("name")

    return None
