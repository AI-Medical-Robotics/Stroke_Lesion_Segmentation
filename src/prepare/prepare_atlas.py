
# 1. Resample DWI, BO, ADC into 1x1x1 mm^3
# 2. Skull-stripped with an in-house "UNet BrainMask Network"
# 3. Used "in-plan" (IP) linear transformations to map the images to the standard MNI (Montreal Neurological Institute) template
# 4. Normalized the DWI intensity to reduce the variability and increase the comparability among subjects
# 5. "Down-sampled" (DS) images to reduce the memory resource requirement in the next steps (e.g. DL networks)
