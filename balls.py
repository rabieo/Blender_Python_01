import bpy
import random
import math
from bpybb.utils import clean_scene

clean_scene()

max_rotation = math.radians(360)

for i in range(50):
    random_size = random.uniform(0.1,4.0)
    random_location = (
        random.uniform(-15,15),
        random.uniform(-15,35),
        random.uniform(-10,10),
    )
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=random.uniform(0.1,2.0), 
        location=random_location
        )
    bpy.ops.object.modifier_add(type='SUBSURF')


    
    material = bpy.data.materials.new(name=f"mankey_material_{i}")
    material.use_nodes = True
    bsdf_node = material.node_tree.nodes["Principled BSDF"]
    red = random.random()
    green = random.random()
    blue = random.random()
    bsdf_node.inputs["Base Color"].default_value = (red,green,blue,1)
    
    active_object = bpy.context.active_object
    active_object.data.materials.append(material)

bpy.ops.object.camera_add(
    location=(1.2,-28.7,4.3),
    rotation=(1.5, 0.0, 0)
    )

bpy.ops.object.light_add(
    type='POINT',
    location=(20, -40, -5),
    scale=(1, 1, 1)
    )
bpy.context.object.data.energy = 50000

bpy.ops.object.light_add(
    type='POINT',
    location=(-20, -40, 30),
    scale=(1, 1, 1)
    )
bpy.context.object.data.energy = 50000

bpy.ops.object.light_add(
    type='POINT',
    location=(0, 0, -40),
    scale=(1, 1, 1)
    )
bpy.context.object.data.energy = 50000

bpy.ops.object.light_add(
    type='POINT',
    location=(-30, 0, 0),
    scale=(1, 1, 1)
    )
bpy.context.object.data.energy = 50000

bpy.ops.mesh.primitive_plane_add(size=100, location=(0, 50, 0), scale=(1, 1, 1))
bpy.context.object.rotation_euler[0] = 1