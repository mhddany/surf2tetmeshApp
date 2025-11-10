import vtk


def display_stl(widget, mesh_polydata):
    """
    Display STL mesh in the widget's stlView.

    Parameters:
        widget: instance of Widget containing stl_renderer, stlView, stl_actor, etc.
        mesh_polydata: vtkPolyData or pyvista mesh
    """
    # Clear previous actors
    widget.stl_renderer.RemoveAllViewProps()

    # Mapper
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(mesh_polydata)

    # Actor
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(0.83, 0.83, 0.83)
    actor.GetProperty().EdgeVisibilityOn()
    actor.GetProperty().SetEdgeColor(0.2, 0.2, 0.2)
    actor.GetProperty().SetLineWidth(1.0)

    # Store reference in widget
    widget.stl_actor = actor

    # Add to renderer
    widget.stl_renderer.AddActor(actor)
    widget.stl_renderer.SetBackground(0.878, 0.949, 0.808)
    widget.stl_renderer.ResetCamera()
    widget.stlView.GetRenderWindow().Render()

    