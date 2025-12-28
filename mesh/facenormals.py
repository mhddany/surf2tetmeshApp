# mesh/normals.py
import vtk
import numpy as np
import pyvista as pv

def compute_surface_normals(mesh):
    """
    Compute centroids and normals of surface triangles.
    mesh: pyvista.PolyData or pyvista.UnstructuredGrid
    Returns: centroids, normals, surf_polydata
    """
    if mesh is None:
        return None, None, None

    # If mesh is UnstructuredGrid, extract surface
    if isinstance(mesh, pv.UnstructuredGrid):
        surf = mesh.extract_surface()
    else:
        # assume PolyData
        surf = mesh

    nodes = surf.points
    faces_raw = surf.faces.reshape(-1, 4)[:, 1:]
    centroids = np.mean(nodes[faces_raw], axis=1)
    v1 = nodes[faces_raw[:, 0]]
    v2 = nodes[faces_raw[:, 1]]
    v3 = nodes[faces_raw[:, 2]]
    normals = np.cross(v2 - v1, v3 - v1)
    normals /= np.linalg.norm(normals, axis=1)[:, np.newaxis]

    return centroids, normals, surf

def display_normals(widget, actor, renderer, ratio=5.0, normals_actor_attr="normals_actor"):
    """
    Compute and display normals for a mesh actor.
    widget: the main Widget instance (contains stl_mesh or tet_mesh)
    actor: vtkActor for which normals are computed
    renderer: corresponding vtkRenderer
    ratio: percentage of max mesh dimension for arrow length (0-100)
    normals_actor_attr: attribute name in widget to store the normals actor
    """
    # Remove previous normals actor
    if getattr(widget, normals_actor_attr, None):
        renderer.RemoveActor(getattr(widget, normals_actor_attr))
        setattr(widget, normals_actor_attr, None)

    # Determine which mesh to use
    mesh = getattr(widget, "stl_mesh" if actor == widget.stl_actor else "tet_mesh", None)
    if mesh is None:
        return

    # Compute centroids and normals
    if isinstance(mesh, pv.UnstructuredGrid):
        surf = mesh.extract_surface()
    else:
        surf = mesh

    nodes = surf.points
    faces_raw = surf.faces.reshape(-1, 4)[:, 1:]
    centroids = np.mean(nodes[faces_raw], axis=1)
    v1 = nodes[faces_raw[:, 0]]
    v2 = nodes[faces_raw[:, 1]]
    v3 = nodes[faces_raw[:, 2]]
    normals = np.cross(v2 - v1, v3 - v1)
    normals /= np.linalg.norm(normals, axis=1)[:, np.newaxis]

    # Compute mesh size for scaling arrows
    bbox_min = np.min(nodes, axis=0)
    bbox_max = np.max(nodes, axis=0)
    max_dim = np.max(bbox_max - bbox_min)
    normals_length = (ratio / 100.0) * max_dim

    # Create VTK points
    points = vtk.vtkPoints()
    for c in centroids:
        points.InsertNextPoint(c)

    pd = vtk.vtkPolyData()
    pd.SetPoints(points)

    vectors = vtk.vtkFloatArray()
    vectors.SetNumberOfComponents(3)
    vectors.SetName("Normals")
    for n in normals * normals_length:
        vectors.InsertNextTuple(n)
    pd.GetPointData().SetVectors(vectors)

    # Glyph arrows
    arrow_source = vtk.vtkArrowSource()
    glyph = vtk.vtkGlyph3D()
    glyph.SetSourceConnection(arrow_source.GetOutputPort())
    glyph.SetInputData(pd)
    glyph.SetVectorModeToUseVector()
    glyph.SetScaleModeToScaleByVector()
    glyph.SetScaleFactor(1.0)
    glyph.Update()

    normals_actor = vtk.vtkActor()
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(glyph.GetOutputPort())
    normals_actor.SetMapper(mapper)
    normals_actor.GetProperty().SetColor(1, 0, 0)  # red

    renderer.AddActor(normals_actor)
    setattr(widget, normals_actor_attr, normals_actor)
    renderer.GetRenderWindow().Render()


def update_face_normals(widget):
    """
    Wrapper to update normals for both STL and Tet actors
    based on the current spinbox value.
    """
    length = widget.normalsLengthLabelSlider.value()/10
    display_normals(widget, widget.stl_actor, widget.stl_renderer, length, "stl_normals_actor")
    display_normals(widget, widget.tet_actor, widget.tet_renderer, length, "tet_normals_actor")