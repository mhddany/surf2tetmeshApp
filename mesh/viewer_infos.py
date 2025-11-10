import vtk
import numpy as np
import pyvista as pv
import os

def setup_stl_viewer(widget):
    """Initialize the STL viewer inside the given widget."""
    widget.stl_renderer = vtk.vtkRenderer()
    widget.stlView.GetRenderWindow().AddRenderer(widget.stl_renderer)
    widget.stl_renderer.SetBackground(0.878, 0.949, 0.808) 
    widget.stl_interactor = widget.stlView.GetRenderWindow().GetInteractor()
    widget.stl_interactor.Initialize()

    # Add axes
    axes = vtk.vtkAxesActor()
    widget.stl_axes_widget = vtk.vtkOrientationMarkerWidget()
    widget.stl_axes_widget.SetOrientationMarker(axes)
    widget.stl_axes_widget.SetInteractor(widget.stl_interactor)
    widget.stl_axes_widget.SetViewport(0.0, 0.0, 0.2, 0.2)
    widget.stl_axes_widget.SetEnabled(1)
    widget.stl_axes_widget.InteractiveOff()


def setup_tet_viewer(widget):
    """Initialize the Tet viewer inside the given widget."""
    widget.tet_renderer = vtk.vtkRenderer()
    widget.tetView.GetRenderWindow().AddRenderer(widget.tet_renderer)
    widget.tet_renderer.SetBackground(0.83, 0.83, 0.83)
    widget.tet_interactor = widget.tetView.GetRenderWindow().GetInteractor()
    widget.tet_interactor.Initialize()

    # Add axes
    axes = vtk.vtkAxesActor()
    widget.tet_axes_widget = vtk.vtkOrientationMarkerWidget()
    widget.tet_axes_widget.SetOrientationMarker(axes)
    widget.tet_axes_widget.SetInteractor(widget.tet_interactor)
    widget.tet_axes_widget.SetViewport(0.0, 0.0, 0.2, 0.2)
    widget.tet_axes_widget.SetEnabled(1)
    widget.tet_axes_widget.InteractiveOff()


def setup_viewers(widget):
    """Setup both STL and Tet viewers."""
    setup_stl_viewer(widget)
    setup_tet_viewer(widget)

    # Initialize actors
    widget.stl_actor = None
    widget.tet_actor = None
    widget.stl_normals_actor = None
    widget.tet_normals_actor = None

def update_stl_info_labels(widget, mesh_polydata, file_path=None):
    """
    Update STL info labels:
    - File name
    - Number of points
    - Number of faces (vertices)
    """
    if file_path:
        file_name = os.path.basename(file_path)
    else:
        file_name = "Unknown"
    widget.stlFileNameLabel.setText(f"File: {file_name}")

    # Number of points
    n_points = mesh_polydata.n_points
    widget.stlPointsLabel.setText(f"Points: {n_points}")

    # Number of faces / vertices
    n_faces = mesh_polydata.n_cells
    widget.stlVerticesLabel.setText(f"Faces: {n_faces}")


def update_tet_info_labels(widget, tet_mesh):
    """
    Update tetrahedral mesh info labels:
    - Nodes
    - Edges
    - Elements (tets)
    """
    if tet_mesh is None:
        widget.tetNodesLabel.setText("Nodes: 0")
        widget.tetEdgesLabel.setText("Edges: 0")
        widget.tetElementsLabel.setText("Elements: 0")
        return

    # Number of nodes
    n_nodes = tet_mesh.n_points
    widget.tetNodesLabel.setText(f"Nodes: {n_nodes}")

    # Number of edges
    edges_polydata = tet_mesh.extract_all_edges()
    n_edges = edges_polydata.n_lines
    widget.tetEdgesLabel.setText(f"Edges: {n_edges}")

    # Number of elements (tets)
    n_elements = tet_mesh.n_cells
    widget.tetElementsLabel.setText(f"Elements: {n_elements}")


def update_view_settings(widget):
    """
    Update display properties of STL and Tet actors:
    - Representation (Surface, Surface+Edges, Wireframe, Points)
    - Edge visibility
    - Opacity
    """
    # --- Camera ---
    current_view = widget.cameraViewComboBox.currentText()
    on_camera_view_changed(widget, current_view)
    
    # --- Display Mode ---
    display_mode = widget.viewModeComboBox.currentText()
    opacity = 1.0  # default; could be parameterized

    for actor, renderer in [
        (widget.stl_actor, widget.stl_renderer),
        (widget.tet_actor, widget.tet_renderer)
    ]:
        if actor is None:
            continue

        prop = actor.GetProperty()
        # Reset
        prop.SetRepresentationToSurface()
        prop.EdgeVisibilityOff()
        prop.SetOpacity(opacity)

        # Display mode
        if display_mode == "Surface":
            prop.SetRepresentationToSurface()
            prop.EdgeVisibilityOff()
        elif display_mode == "Surface + Edges":
            prop.SetRepresentationToSurface()
            prop.EdgeVisibilityOn()
        elif display_mode == "Wireframe":
            prop.SetRepresentationToWireframe()
            prop.EdgeVisibilityOff()
        elif display_mode == "Points":
            prop.SetRepresentationToPoints()
            prop.SetPointSize(4)

        # Re-render
        renderer.GetRenderWindow().Render()

def on_camera_view_changed(widget, view_name: str):
    """Change camera view for both STL and Tet viewers."""
    for renderer in [widget.stl_renderer, widget.tet_renderer]:
        camera = renderer.GetActiveCamera()
        if camera is None:
            continue

        # Try to compute a focal point from the current actors
        actors = renderer.GetActors()
        actors.InitTraversal()
        actor = actors.GetNextActor()
        if actor:
            bounds = actor.GetBounds()
            center = [
                (bounds[1] + bounds[0]) / 2.0,
                (bounds[3] + bounds[2]) / 2.0,
                (bounds[5] + bounds[4]) / 2.0,
            ]
        else:
            center = [0.0, 0.0, 0.0]

        # Set camera position depending on view
        view = view_name.lower()
        if view == "x":
            camera.SetPosition(center[0], center[1] - 1.0, center[2])
            camera.SetViewUp(0, 0, 1)
        elif view == "y":
            camera.SetPosition(center[0], center[1], center[2] + 1.0)
            camera.SetViewUp(0, 1, 0)
        elif view == "z":
            camera.SetPosition(center[0] + 1.0, center[1], center[2])
            camera.SetViewUp(0, 0, 1)
        elif view in ["3d", "perspective"]:
            camera.SetPosition(center[0] + 1.0, center[1] - 1.0, center[2] + 1.0)
            camera.SetViewUp(0, 0, 1)
        else:
            print(f"Unknown view name: {view_name}")
            continue

        camera.SetFocalPoint(center)
        renderer.ResetCamera()
        renderer.GetRenderWindow().Render()