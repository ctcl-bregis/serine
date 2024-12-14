# Serine - CTCL 2024
# File: /py/src/css.py
# Purpose: CSS restructuring steps
# Created: November 30, 2024
# Modified: December 4, 2024

import re
from re import Match
import re

def no_where(inp: str) -> str:
    """
    Converts :where() pseudo-class in a CSS file into individual selectors.
    """
    pattern = r'([^,\s]+):where\((.*?)\)'

    def expand_where(match: Match[str]) -> str:
        """
        Replace :where() with expanded selectors, ensuring parent selectors are prefixed.
        """
        parent_selector = match.group(1)
        group_content = match.group(2)
        individual_selectors = group_content.split(",")
        expanded = ', '.join(f"{parent_selector}{selector.strip()}" for selector in individual_selectors)
        return expanded

    out = re.sub(pattern, expand_where, inp)
    return out
