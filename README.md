# GTFS-Realtime Consumer

Async-friendly GTFS-Realtime poller for vehicle positions, trip updates, and alerts. Decodes the protobuf feed into typed dataclasses; can write JSONL snapshots to disk or stream to stdout for piping into Kafka / Redpanda.

## Use

```python
from pathlib import Path
from gtfsrt import poll

poll("https://api.mta.info/...vehicle-positions", interval_s=30, out_path=Path("vp.jsonl"))
```

## Feeds tested against

- MTA New York Subway VehiclePositions
- Calgary Transit GTFS-Realtime
- TTC TripUpdates

<!-- 2024-04 -->

<!-- maint 2025-01-27 -->

<!-- maint 2025-03-08 -->

<!-- maint 2025-04-15 -->

<!-- maint 2025-05-24 -->

<!-- maint 2025-07-03 -->

<!-- maint 2025-08-10 -->

<!-- maint 2025-09-19 -->

<!-- maint 2025-10-27 -->

<!-- maint 2025-12-06 -->

<!-- maint 2024-02-06 -->

<!-- maint 2024-03-28 -->

<!-- maint 2024-05-19 -->

<!-- maint 2024-07-11 -->

<!-- maint 2024-09-01 -->

<!-- maint 2024-10-22 -->

<!-- maint 2024-12-13 -->

<!-- maint 2023-02-19 -->

<!-- maint 2023-04-25 -->

<!-- m 2026-04-17T19:22:00-06:00 -->

<!-- m 2023-04-07T15:25:00-06:00 -->

<!-- m 2023-08-26T20:16:00-06:00 -->

<!-- m 2026-01-20T15:35:00-06:00 -->

<!-- m 2026-03-04T18:11:00-06:00 -->

<!-- m 2026-03-02T13:06:00-06:00 -->

<!-- m 2025-04-07T17:12:00-06:00 -->

<!-- m 2023-03-11T19:14:00-06:00 -->

<!-- m 2024-08-25T19:29:00-06:00 -->

<!-- m 2023-09-22T23:08:00-06:00 -->

<!-- m 2023-04-12T21:24:00-06:00 -->
