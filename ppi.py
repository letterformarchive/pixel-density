import cv2, math

image_path = '/PATH/TO/FILE' # TODO add filepath  

# Physical measurements (cm) of image window, converted to in
height_cm = 00   # TODO Update with actual measurements
width_cm = 00    # TODO Update with actual measurements
height_in = height_cm / 2.54  
width_in = width_cm / 2.54  

# Load the image
image = cv2.imread(image_path)

# Get dimensions (height, width, channels)
height_px, width_px, channels = image.shape

print("\n")
print(f"Image dims (HxW): {height_px:.0f} x {width_px:.0f} px")
print(f" Phys dims (HxW): {height_in:.0f} x {width_in:.0f} in")
# print(f"        Channels: {channels}")

ppi_x = width_px / width_in
ppi_y = height_px / height_in

# Diagonal PPI (true density)
ppi_diag = math.sqrt(width_px**2 + height_px**2) / math.sqrt(width_in**2 + height_in**2)

# print(f"Horizontal PPI: {ppi_x:.0f}")
# print(f"Vertical PPI: {ppi_y:.0f}")
print(f"Diagonal PPI (overall): {ppi_diag:.0f}")