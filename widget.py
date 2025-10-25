import vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PySide6.QtWidgets import QWidget, QFileDialog
from ui_widget import Ui_Widget  # generated from Qt Designer


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Surf2Mesh")

        # === Connect button ===
        self.selectFileButton.clicked.connect(self.select_stl_file)        
        self.generateMeshButton.clicked.connect(self.generate_tet_mesh)

        # === Setup STL Viewer ===
        self.stl_renderer = vtk.vtkRenderer()
        self.stlView.GetRenderWindow().AddRenderer(self.stl_renderer)
        self.stl_interactor = self.stlView.GetRenderWindow().GetInteractor()
        self.stl_interactor.Initialize()

        # Add axes to STL view
        stl_axes = vtk.vtkAxesActor()
        self.stl_axes_widget = vtk.vtkOrientationMarkerWidget()
        self.stl_axes_widget.SetOrientationMarker(stl_axes)
        self.stl_axes_widget.SetInteractor(self.stl_interactor)
        self.stl_axes_widget.SetViewport(0.0, 0.0, 0.2, 0.2)
        self.stl_axes_widget.SetEnabled(1)
        self.stl_axes_widget.InteractiveOff()

        # === Setup Tet Viewer ===
        self.tet_renderer = vtk.vtkRenderer()
        self.tetView.GetRenderWindow().AddRenderer(self.tet_renderer)
        self.tet_interactor = self.tetView.GetRenderWindow().GetInteractor()
        self.tet_interactor.Initialize()

        # Add axes to Tet view
        tet_axes = vtk.vtkAxesActor()
        self.tet_axes_widget = vtk.vtkOrientationMarkerWidget()
        self.tet_axes_widget.SetOrientationMarker(tet_axes)
        self.tet_axes_widget.SetInteractor(self.tet_interactor)
        self.tet_axes_widget.SetViewport(0.0, 0.0, 0.2, 0.2)
        self.tet_axes_widget.SetEnabled(1)
        self.tet_axes_widget.InteractiveOff()

    # === File selection ===
    def select_stl_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select STL file",
            "",
            "STL Files (*.stl);;All Files (*)"
        )
        if file_path:
            self.stl_file = file_path
            print(f"Selected STL: {self.stl_file}")
            self.display_stl(self.stl_file)
            
    def generate_tet_mesh(self):
        from surf2tetmesh import Surf2TetMesh
        
        # Generate mesh from STL
        self.fem_obj = Surf2TetMesh(self.stl_file)
        self.fem_obj.generate_fem()
        print(f"Generated Tetrahedral Mesh: {self.fem_obj.fem_mesh}")
        
        # Display in VTK widget
        self.display_tet_mesh(self.fem_obj.fem_mesh)
                   

    # === STL display ===
    def display_stl(self, file_path):
        """Display STL mesh in stlView."""
        self.stl_renderer.RemoveAllViewProps()

        reader = vtk.vtkSTLReader()
        reader.SetFileName(file_path)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(0.9, 0.9, 0.9)  # Light gray

        self.stl_renderer.AddActor(actor)
        self.stl_renderer.SetBackground(0.1, 0.1, 0.1)
        self.stl_renderer.ResetCamera()

        self.stlView.GetRenderWindow().Render()

    # === Tet display ===
    def display_tet_mesh(self, vtk_unstructured_grid):
        """Display tetrahedral mesh in tetView."""
        # Clear previous render objects
        self.tet_renderer.RemoveAllViewProps()

        # Mapper
        mapper = vtk.vtkDataSetMapper()
        mapper.SetInputData(vtk_unstructured_grid)

        # Actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # === Style settings ===
        prop = actor.GetProperty()
        prop.SetColor(0.7, 0.7, 1.0)        # Light blue surface
        prop.EdgeVisibilityOn()             # 🔹 Show mesh edges
        prop.SetEdgeColor(0.2, 0.2, 0.2)    # Dark gray edges
        prop.SetLineWidth(1.0)
        prop.SetRepresentationToSurface()   # Surface + edges

        # Optional: enable smooth edges
        self.tet_renderer.UseFXAAOn()       # Anti-aliasing

        # Add actor to renderer
        self.tet_renderer.AddActor(actor)
        self.tet_renderer.SetBackground(0.1, 0.1, 0.1)
        self.tet_renderer.ResetCamera()

        # Render the updated scene
        self.tetView.GetRenderWindow().Render()
