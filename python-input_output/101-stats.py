#!/usr/bin/python3
"""Reads stdin line by line and computes:
- Total file size
- Count of valid HTTP status codes
"""

import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_counts = {}
total_size = 0
line_count = 0


def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            parts = line.strip().split()

            try:
                size = int(parts[-1])
                total_size += size
            except (ValueError, IndexError):
                pass

            try:
                status = int(parts[-2])
                if status in status_codes:
                    status_counts[status] = status_counts.get(status, 0) + 1
            except (ValueError, IndexError):
                pass

            line_count += 1
            if line_count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        pass
    finally:
        print_stats()
