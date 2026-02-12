#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timedelta

RECO_FILE = Path("docs/security_recommendations.json")
FEED_FILE = Path("docs/recommendations_feed.json")


def main():
    if not RECO_FILE.exists():
        print("No recommendations file, exiting.")
        return

    data = json.loads(RECO_FILE.read_text(encoding="utf-8"))
    items = data.get("items", [])

    # Only High/Medium items from last 3 days
    cutoff = datetime.utcnow() - timedelta(days=3)
    out_items = []

    for item in items:
        severity = item.get("severity", "Low")
        if severity == "Low":
            continue

        # parse date (YYYY-MM-DD), fallback to very old
        raw_date = item.get("date", "1970-01-01")
        try:
            dt = datetime.fromisoformat(raw_date)
        except Exception:
            dt = cutoff

        if dt < cutoff:
            continue

        out_items.append(
            {
                "id": item.get("id"),
                "date": raw_date,
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "source": item.get("source", ""),
                "severity": severity,
                "tags": item.get("tags", []),
                "tech": item.get("tech", []),
                "top_recommendations": item.get("recommendations", [])[:2],
            }
        )

    feed = {
        "generatedAt": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "items": out_items,
    }

    FEED_FILE.write_text(
        json.dumps(feed, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Exported {len(out_items)} items to {FEED_FILE}")


if __name__ == "__main__":
    main()
