"""GTFS-Realtime ingestion."""
from gtfsrt.consumer import VehiclePosition, fetch_feed, poll, vehicle_positions

__all__ = ["VehiclePosition", "fetch_feed", "poll", "vehicle_positions"]
