from datetime import timedelta
from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32

source = FileSource(
    path="data/data.parquet",
    timestamp_field="event_timestamp",
)

utente = Entity(name="user_id")

stats = FeatureView(
    name="user_stats",
    entities=[utente],
    ttl=timedelta(days=7),
    schema=[
        Field(name="score", dtype=Float32),
    ],
    source=source,
)
