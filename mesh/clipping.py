import vtk
from mesh.viewer_infos import update_view_settings

def generate_clipped_mesh(widget, mesh, clip_value):
    """
    Generate clipped surface and wireframe actors for a mesh at a given clip_value.
    
    Parameters:
        widget: Widget instance
        mesh: vtkUnstructuredGrid or vtkPolyData
        clip_value: float in [-1, +1] for clipping along Z axis
    Returns:
        surface_actor, wire_actor: vtkActors for clipped mesh
    """
    bounds = mesh.GetBounds()
    z_min, z_max = bounds[4], bounds[5]
    z_cut = z_min + (clip_value + 1) / 2 * (z_max - z_min)

    plane = vtk.vtkPlane()
    plane.SetOrigin(0, 0, z_cut)
    plane.SetNormal(0, 0, 1)

    clipper = vtk.vtkClipDataSet()
    clipper.SetInputData(mesh)
    clipper.SetClipFunction(plane)
    clipper.Update()
    clipped_output = clipper.GetOutput()

    # Surface actor
    surface_mapper = vtk.vtkDataSetMapper()
    surface_mapper.SetInputData(clipped_output)
    surface_actor = vtk.vtkActor()
    surface_actor.SetMapper(surface_mapper)
    surface_actor.GetProperty().SetColor(0.8, 0.8, 0.8)
    surface_actor.GetProperty().EdgeVisibilityOff()

    # Wireframe actor
    wire_mapper = vtk.vtkDataSetMapper()
    wire_mapper.SetInputData(clipped_output)
    wire_actor = vtk.vtkActor()
    wire_actor.SetMapper(wire_mapper)
    wire_actor.GetProperty().SetRepresentationToWireframe()
    wire_actor.GetProperty().SetColor(0, 0, 0)

    return surface_actor, wire_actor


def get_clipped_polydata(widget, mesh, clip_value):
    """
    Return clipped mesh (vtkPolyData or vtkUnstructuredGrid) without creating actors.
    """
    bounds = mesh.GetBounds()
    z_min, z_max = bounds[4], bounds[5]
    z_cut = z_min + (clip_value + 1) / 2 * (z_max - z_min)

    plane = vtk.vtkPlane()
    plane.SetOrigin(0, 0, z_cut)
    plane.SetNormal(0, 0, 1)

    clipper = vtk.vtkClipDataSet()
    clipper.SetInputData(mesh)
    clipper.SetClipFunction(plane)
    clipper.Update()

    return clipper.GetOutput()


def update_clipped_mesh(widget):
    """
    Update the widget's clipped mesh actors based on the current slider value.
    """
    clip_value = widget.tessellatedSlider.value() / 100.0  # -1..+1

    # Get clipped data
    clipped_polydata = get_clipped_polydata(widget, widget.tet_mesh, clip_value)

    # Update the existing actors
    widget.clipped_tet_surface.GetMapper().SetInputData(clipped_polydata)
    widget.clipped_tet_wire.GetMapper().SetInputData(clipped_polydata)

    # Update display settings (representation, normals, etc.)
    update_view_settings(widget)

    # Re-render
    widget.tet_renderer.GetRenderWindow().Render()
