
from loader.loading_runner import FunctionProgressDialog
import tetgen
from mesh.tet_display import display_tet_mesh
from mesh.viewer_infos import update_tet_info_labels, update_view_settings
from surf2tet.tetgen_settings import get_tetgen_parameters


def generate_fem(widget, order=1, mindihedral=20, minratio=1.5,
                 maxvolume=1.0, psc=1.0, verbose=0.0):
    """
    Generate tetrahedral FEM mesh using TetGen from the mesh stored in the widget.

    Parameters:
        widget: instance of Widget containing stl_mesh
    """
    if not hasattr(widget, "stl_mesh"):
        raise ValueError("Widget does not have stl_mesh attribute")

    tet = tetgen.TetGen(widget.stl_mesh)
    tet.tetrahedralize(
        order=order,
        mindihedral=mindihedral,
        minratio=minratio,
        maxvolume=maxvolume,
        psc=psc,
        verbose=verbose
    )
    widget.fem_mesh = tet.grid
    print(f"Generated FEM mesh with {widget.fem_mesh.n_cells} tetrahedra")

def generate_tet_mesh(widget):
    """
    Generate tetrahedral FEM mesh using TetGen from the widget's STL mesh,
    with a progress dialog.
    
    Parameters:
        widget: instance of Widget containing stl_mesh and tet_mesh attributes
    """

    def generate_fem_task(stl_file, progress_callback=None):
        # Get TetGen parameters from UI
        params = get_tetgen_parameters(widget)
        # Generate FEM mesh directly in the widget
        generate_fem(widget, **params)
        # No return needed; mesh stored in widget.fem_mesh

    # Create progress dialog
    progress = FunctionProgressDialog(widget, "Generating FEM mesh...")

    # Run the task
    worker = progress.run(generate_fem_task, widget.stl_file)

    # When the worker finishes, update the widget
    def handle_result(_):
        widget.tet_mesh = widget.fem_mesh
        print(f"Generated Tetrahedral Mesh: {widget.tet_mesh}")
        
        # display tetrahedral mesh
        display_tet_mesh(widget, widget.tet_mesh)
        
        # Update display settings (representation, normals, etc.)
        update_view_settings(widget)
        
        # Update tetrahedral mesh info labels        
        update_tet_info_labels(widget, widget.tet_mesh)

    worker.finished.connect(handle_result)
