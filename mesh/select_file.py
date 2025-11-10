import pyvista as pv
from PySide6.QtWidgets import QFileDialog
from mesh.stl_display import display_stl
from mesh.viewer_infos import update_stl_info_labels, update_view_settings

def select_stl_file(widget):
    """
    Open file dialog and store mesh directly in the passed widget instance.
    """
    file_path, _ = QFileDialog.getOpenFileName(
        widget,
        "Select STL file",
        "",
        "STL Files (*.stl);;All Files (*)"
    )
    if file_path:
        widget.stl_file = file_path
        widget.stl_mesh = pv.read(file_path)
        print(f"Selected STL: {file_path}")
        
        # display surface mesh
        display_stl(widget, widget.stl_mesh)
        
        # Update display settings
        update_view_settings(widget)
        
        # Update STL info labels
        update_stl_info_labels(widget, widget.stl_mesh, file_path)
