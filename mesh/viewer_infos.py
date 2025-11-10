import vtk
import numpy as np
import pyvista as pv
import os

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