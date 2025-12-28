import vtk

def display_tet_mesh(widget, vtk_unstructured_grid):
    """
    Display tetrahedral mesh in the widget's tetView, with optional clipped actors.

    Parameters:
        widget: instance of Widget containing tet_renderer, tetView, etc.
        vtk_unstructured_grid: vtkUnstructuredGrid or PyVista mesh
    """
    # Clear previous actors
    widget.tet_renderer.RemoveAllViewProps()

    # Main Mapper & Actor
    mapper = vtk.vtkDataSetMapper()
    mapper.SetInputData(vtk_unstructured_grid)

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    widget.tet_actor = actor  # store reference

    # Style settings
    prop = actor.GetProperty()
    prop.SetColor(0.878, 0.949, 0.808)
    prop.EdgeVisibilityOn()
    prop.SetEdgeColor(0.2, 0.2, 0.2)
    prop.SetLineWidth(1.0)
    prop.SetRepresentationToSurface()

    # Anti-aliasing
    widget.tet_renderer.UseFXAAOn()

    # Add main actor to renderer
    widget.tet_renderer.AddActor(actor)
    widget.tet_renderer.SetBackground(0.83, 0.83, 0.83)
    widget.tet_renderer.ResetCamera()
    
    # Render
    widget.tetView.GetRenderWindow().Render()
'''
    # Initialize clipped actors
    widget.clipped_tet_surface = vtk.vtkActor()
    surface_mapper = vtk.vtkDataSetMapper()
    surface_mapper.SetInputData(vtk_unstructured_grid)
    widget.clipped_tet_surface.SetMapper(surface_mapper)
    widget.clipped_tet_surface.GetProperty().SetColor(0.878, 0.949, 0.808)
    widget.clipped_tet_surface.GetProperty().EdgeVisibilityOff()

    widget.clipped_tet_wire = vtk.vtkActor()
    wire_mapper = vtk.vtkDataSetMapper()
    wire_mapper.SetInputData(vtk_unstructured_grid)
    widget.clipped_tet_wire.SetMapper(wire_mapper)
    widget.clipped_tet_wire.GetProperty().SetRepresentationToWireframe()
    widget.clipped_tet_wire.GetProperty().SetColor(0.2, 0.2, 0.2)

    # Add clipped actors to renderer
    widget.tet_renderer.AddActor(widget.clipped_tet_surface)
    widget.tet_renderer.AddActor(widget.clipped_tet_wire)
    '''
    
