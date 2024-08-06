
import cv2
import numpy as np

def add_fog_effect(depth_map, fog_intensity=0.5):
    fog_color = 0  # White color for fog
    fog_layer = np.full(depth_map.shape, fog_color, dtype=np.float32)
    foggy_depth_map = cv2.addWeighted(depth_map, 1 - fog_intensity, fog_layer, fog_intensity, 0)
    return foggy_depth_map

# Function to remove a percentage of the background
def remove_background_percentage(depth_map, threshold=0.2):
    depth_map[depth_map < threshold] = 0
    return depth_map