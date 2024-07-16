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
