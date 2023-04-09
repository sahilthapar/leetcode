from typing import List
import re

def num_unique_emails(emails: List[str]) -> int:
    result = set()
    for e in emails:
        local, domain = e.split('@')
        result.add((local.split('+')[0].replace('.', ''), domain))
    return len(result)
