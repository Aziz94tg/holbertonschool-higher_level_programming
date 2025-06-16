#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics:
- File size total
- Count of HTTP status codes
Printed every 10 lines and on KeyboardInterrupt (CTRL + C)
"""

import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_counts = {}
total_size = 0
line_count = 0

def print_stats():
    """Prints collected metrics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))

try:
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) >= 7:
            try:
                status = int(parts[-2])
                size = int(parts[-1])
                total_size += size

                if status in status_codes:
                    if status not in status_counts:
                        status_counts[status] = 0
                    status_counts[status] += 1
            except (ValueError, IndexError):
                pass

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass
finally:
    print_stats()
