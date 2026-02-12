#!/usr/bin/env python3
import json
from pathlib import Path

NEWS_FILE = Path("docs/news.json")
RECO_FILE = Path("docs/security_recommendations.json")
FEED_FILE = Path("docs/data/feed.json")


def main():
    if not NEWS_FILE.exists() or not RECO_FILE.exists():
        print("Missing news or recommendations file, exiting.")
        return

    news_data = json.loads(NEWS_FILE.read_text(encoding="utf-8"))
    reco_data = json.loads(RECO_FILE.read_text(encoding="utf-8"))

    news_items = news_data.get("items", [])
    reco_items = reco_data.get("items", [])

    # Build map of recommendations by article id
    reco_map = {item["id"]: item for item in reco_items}

    feed = []
    for news in news_items:
        news_id = news.get("id")
        if not news_id or news_id not in reco_map:
            continue

        reco = reco_map[news_id]

        # Expand recommendations into structured fields
        recos = reco.get("recommendations", [])
        
        # Basic heuristic: split into who/risk/actions
        rec_who = ["Organizations using affected products or services."]
        rec_risk = [
            f"Impact: {reco.get('severity', 'Medium')} severity incident.",
            "Review article for specific attack surface and exploitation details."
        ]
        rec_actions_0_24 = recos[:2] if len(recos) >= 2 else recos
        rec_actions_24_72 = recos[2:4] if len(recos) > 2 else ["Monitor vendor advisories for patches."]
        rec_detection = ["Review logs for suspicious activity mentioned in the article."]

        feed_item = {
            "id": news_id,
            "date": news.get("date", ""),
            "severity": reco.get("severity", "medium").lower(),
            "tag": ", ".join(reco.get("tags", [])),
            "title": news.get("title", ""),
            "newsTitle": news.get("title", ""),
            "newsBody": news.get("summary", "")[:300] + "...",  # truncate
            "recSummary": recos[0] if recos else "Review the incident and assess relevance.",
            "recWho": rec_who,
            "recRisk": rec_risk,
            "recActions0_24": rec_actions_0_24,
            "recActions24_72": rec_actions_24_72,
            "recDetection": rec_detection,
        }
        feed.append(feed_item)

    # Keep only last 20 items
    feed = feed[:20]

    FEED_FILE.parent.mkdir(parents=True, exist_ok=True)
    FEED_FILE.write_text(
        json.dumps(feed, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"Built feed with {len(feed)} items -> {FEED_FILE}")


if __name__ == "__main__":
    main()
