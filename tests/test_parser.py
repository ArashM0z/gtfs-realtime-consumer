"""Parser smoke test using a synthetic feed."""
from google.transit import gtfs_realtime_pb2

from gtfsrt.consumer import vehicle_positions


def test_parse_synthetic_feed() -> None:
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.header.gtfs_realtime_version = "2.0"
    entity = feed.entity.add()
    entity.id = "vehicle-1"
    v = entity.vehicle
    v.vehicle.id = "bus-42"
    v.trip.trip_id = "trip-001"
    v.trip.route_id = "route-1"
    v.position.latitude = 40.7555
    v.position.longitude = -73.9876
    v.timestamp = 1_700_000_000

    positions = vehicle_positions(feed)
    assert len(positions) == 1
    assert positions[0].vehicle_id == "bus-42"
    assert positions[0].route_id == "route-1"
