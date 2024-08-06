import numpy as np
from .fog import *
import torch
from PIL import Image, ImageDraw, ImageFont


class FogDepthMapModifier:
    @classmethod
    def INPUT_TYPES(cls):     
         return {"required": {  
            "image": ("IMAGE", ),
            "rm_background": ("FLOAT", {"default": 0.2, "min": 0.0, "max": 1.0, "step": 0.01}),
            "intensity": ("FLOAT", {"default": 0.1, "min": 0.0, "max": 1.0, "step": 0.01})
            }
        }
            
    RETURN_TYPES = ("IMAGE", )
    RETURN_NAMES =("image", )
    FUNCTION = "process"
    CATEGORY = "fog"


    def process(self, image, rm_background, intensity):
        print(image.shape)
        image = image[0].cpu().numpy()
        image = add_fog_effect(image, intensity)
        image = remove_background_percentage(image, rm_background)
        image = torch.tensor(image)
        image = torch.unsqueeze(image, 0)
        return (image, )
         