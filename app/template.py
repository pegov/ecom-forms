from typing import Iterable, Dict, Optional

from app.validator import validate


def find_template_name(
    templates: Iterable[Dict[str, str]],
    query: Dict[str, str],
) -> Optional[str]:
    """Find the most compatible template name."""
    comp_name = ""
    comp_len = 0
    for t in templates:
        base_len = len(t) - 1
        if base_len > len(query):
            continue

        i = base_len
        for q_key, q_value in query.items():
            if q_key not in t.keys():
                continue

            t_type = t[q_key]
            q_type = validate(q_value)

            if t_type == q_type:
                i -= 1
                if i == 0:
                    if base_len > comp_len:
                        comp_name = t.get("name")
                        comp_len = base_len

                    break

    if comp_len > 0:
        return comp_name

    return None
