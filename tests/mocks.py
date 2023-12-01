from typing import Dict, List, Optional

from app.db.abc import AbstractDatabase


class MockDatabase(AbstractDatabase):
    templates: List[Dict[str, str]] = [
        {
            "name": "Sign up",
            "username": "text",
            "email": "email",
            "phone": "phone",
            "date_added": "date",
        },
        {
            "name": "Order",
            "order_id": "text",
            "receiver_email": "email",
            "receiver_phone": "phone",
            "receiver_address": "text",
            "date_registered": "date",
            "date_completed": "date",
        },
    ]

    def get_template_name(self, fields: Dict[str, str]) -> Optional[str]:
        candidate_name = ""
        candidate_len = 0
        for template in self.templates:
            if (
                set(fields.items()).issubset(set(template.items()))
                and len(template) > candidate_len
            ):
                candidate_name = template.get("name")  # type: ignore
                candidate_len = len(template)

        if candidate_len > 0:
            return candidate_name

        return None
