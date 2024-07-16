"""GTFS-Realtime poller: vehicle positions, trip updates, alerts."""

from __future__ import annotations

import json
import time
from dataclasses import dataclass
from pathlib import Path

import httpx
from google.transit import gtfs_realtime_pb2


@dataclass(frozen=True)
class VehiclePosition:
    vehicle_id: str
    trip_id: str
    route_id: str
    lat: float
    lon: float
    bearing: float | None
    speed_mps: float | None
    timestamp: int
    occupancy: str | None


def fetch_feed(url: str, timeout_s: float = 10.0) -> gtfs_realtime_pb2.FeedMessage:
    response = httpx.get(url, timeout=timeout_s)
    response.raise_for_status()
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(response.content)
    return feed


def vehicle_positions(feed: gtfs_realtime_pb2.FeedMessage) -> list[VehiclePosition]:
    out: list[VehiclePosition] = []
    for entity in feed.entity:
        if not entity.HasField("vehicle"):
            continue
        v = entity.vehicle
        pos = v.position
        out.append(VehiclePosition(
            vehicle_id=v.vehicle.id or entity.id,
            trip_id=v.trip.trip_id,
            route_id=v.trip.route_id,
            lat=pos.latitude,
            lon=pos.longitude,
            bearing=pos.bearing if pos.HasField("bearing") else None,
            speed_mps=pos.speed if pos.HasField("speed") else None,
            timestamp=v.timestamp,
            occupancy=v.OccupancyStatus.Name(v.occupancy_status)
                if v.HasField("occupancy_status") else None,
        ))
    return out


def poll(
    url: str,
    interval_s: int = 30,
    duration_s: int | None = None,
    out_path: Path | None = None,
) -> None:
    start = time.monotonic()
    while True:
        try:
            feed = fetch_feed(url)
            positions = vehicle_positions(feed)
            for p in positions:
                line = json.dumps(p.__dict__)
                if out_path:
                    with out_path.open("a") as fh:
                        fh.write(line + "\n")
                else:
                    print(line)
        except Exception as exc:
            print(f"fetch_failed: {exc}")
        if duration_s and (time.monotonic() - start) >= duration_s:
            return
        time.sleep(interval_s)
