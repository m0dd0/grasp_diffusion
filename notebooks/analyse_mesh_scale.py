from pathlib import Path
import trimesh
import h5py

GRASPS_PATH = Path("/home/moritz/Documents/data/grasps/")
MESHES_PATH = Path("/home/moritz/Documents/data/meshes/")

def get_all_object_classes(grasps_path):
    return [p.name for p in grasps_path.iterdir()]

def get_mesh_files(grasps_path, object_class):
    return [p for p in (grasps_path / object_class).iterdir()]

meshes = []
mesh_scales = []
for mesh_file in mesh_files:
    grasp_data = h5py.File(mesh_file, "r")
    grasp_mesh_file_name = grasp_data["object/file"][()].decode("utf-8").split("/")[-1]
    grasp_mesh_path = MESHES_PATH / mesh_file.parent.name / grasp_mesh_file_name

    meshes.append(trimesh.load(grasp_mesh_path, file_type="obj", force="mesh"))
    mesh_scales.append(grasp_data["object/scale"][()])

for mesh 

# for mesh in meshes:
#     print(mesh.bounds)
#     print(mesh.centroid)
# center all meshes
# for mesh in meshes:
#     mesh.apply_translation(-mesh.centroid)

scene = trimesh.Scene()
scene.add_geometry(trimesh.creation.axis(axis_length=200, axis_radius=10))
scene.add_geometry(meshes)
scene.show()
