import cadquery as cq

# ISO M4 Cap Screw Body (No Threads)
shank_dia = 4.0
shank_len = 20.0
head_dia = 7.0
head_height = 4.0

# Create shank and head
shank = cq.Workplane("XY").circle(shank_dia / 2).extrude(shank_len)
head = cq.Workplane("XY").circle(head_dia / 2).extrude(head_height)

# Combine parts
screw = head.union(shank.translate((0, 0, -shank_len)))

# Export STEP file to Desktop
output_path = r"C:\\Users\\Administrator\\Desktop\\M4_Cap_Screw.step"
screw.val().exportStep(output_path)
print(f"✅ STEP file saved to: {output_path}")
