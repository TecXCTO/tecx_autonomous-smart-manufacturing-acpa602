# Real-Time Laser Meltpool Diagnostics Packet Structure
builtin_interfaces/Time timestamp   # Strict clock sync tracking time stamp
uint64 frame_id                      # Monotonically increasing frame identifier
float32 meltpool_area_mm2            # Calculated footprint surface tracking scale
float32 aspect_ratio                 # Meltpool width divided by height ratio
float32 peak_temperature_c           # Dynamic maximum infrared thermal core reading
float32 porosity_index               # NPU live inference defect classification score
