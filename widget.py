import vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PySide6.QtWidgets import QWidget, QFileDialog, QDialog, QVBoxLayout, QLabel, QProgressBar
from ui_widget import Ui_Widget  # generated from Qt Designer


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Surf2Mesh")
                
        # Initialize TetGen settings
        self.init_tetgen_settings()

        # === Connect button ===
        self.selectFileButton.clicked.connect(self.select_stl_file)        
        self.generateMeshButton.clicked.connect(self.generate_tet_mesh)

        # === Setup STL Viewer ===
        self.stl_renderer = vtk.vtkRenderer()
        self.stlView.GetRenderWindow().AddRenderer(self.stl_renderer)
        self.stl_renderer.SetBackground(0.878, 0.949, 0.808) 
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
        self.tet_renderer.SetBackground(0.83, 0.83, 0.83)
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
        
        
        self.cameraViewComboBox.currentTextChanged.connect(self.update_view_settings)
        self.showFacesCheckBox.toggled.connect(self.update_view_settings)
        self.showEdgesCheckBox.toggled.connect(self.update_view_settings)

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
        from loader.loading_runner import FunctionProgressDialog
        def generate_fem_task(stl_file, progress_callback=None):
            params = self.get_tetgen_parameters()
            fem_obj = Surf2TetMesh(stl_file)
            fem_obj.generate_fem(**params)
            return fem_obj
        
        # Create progress dialog
        progress = FunctionProgressDialog(self, "Generating FEM mesh...")

        # Run the task
        worker = progress.run(generate_fem_task, self.stl_file)

        # When the worker finishes, handle the result
        def handle_result(fem_obj):
            self.fem_obj = fem_obj
            print(f"Generated Tetrahedral Mesh: {self.fem_obj.fem_mesh}")
            self.display_tet_mesh(self.fem_obj.fem_mesh)

        worker.finished.connect(handle_result)      
                    
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
        actor.GetProperty().SetColor(0.83, 0.83, 0.83)  # Light gray
        actor.GetProperty().EdgeVisibilityOn()              # Show edges
        actor.GetProperty().SetEdgeColor(0.2, 0.2, 0.2)    # Dark gray edges
        actor.GetProperty().SetLineWidth(1.0)  
        self.stl_actor = actor  # Store reference for later use           

        self.stl_renderer.AddActor(actor)
        self.stl_renderer.SetBackground(0.878, 0.949, 0.808) 
        self.stl_renderer.ResetCamera()

        self.stlView.GetRenderWindow().Render()
        
        current_view = self.cameraViewComboBox.currentText()
        self.on_camera_view_changed(current_view)

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
        self.tet_actor = actor  # Store reference for later use

        # === Style settings ===
        prop = actor.GetProperty()
        prop.SetColor(0.878, 0.949, 0.808)  
        prop.EdgeVisibilityOn()             # Show mesh edges
        prop.SetEdgeColor(0.2, 0.2, 0.2)    # Dark gray edges
        prop.SetLineWidth(1.0)
        prop.SetRepresentationToSurface()   # Surface + edges

        # Optional: enable smooth edges
        self.tet_renderer.UseFXAAOn()       # Anti-aliasing

        # Add actor to renderer
        self.tet_renderer.AddActor(actor)        
        self.tet_renderer.SetBackground(0.83, 0.83, 0.83)
        self.tet_renderer.ResetCamera()

        # Render the updated scene
        self.tetView.GetRenderWindow().Render()
        
        current_view = self.cameraViewComboBox.currentText()
        self.on_camera_view_changed(current_view)
        
    # === Initialize TetGen Settings Widgets ===
    def init_tetgen_settings(self):
        # Element order (ComboBox)
        self.orderComboBox.setCurrentIndex(0)  # default: Linear

        # SpinBox / DoubleSpinBox values
        self.mindihedralSpinBox.setValue(20)        # Min dihedral angle
        self.minRatioDoubleSpinBox.setValue(1.5)    # Min ratio
        self.maxVolumeDoubleSpinBox.setValue(1.0)   # Max volume

        # CheckBoxes
        self.preserveSurfaceCheckBox.setChecked(True)
        self.verboseCheckBox.setChecked(False)
        
    def get_tetgen_parameters(self):
        return dict(
            order=self.orderComboBox.currentIndex() + 1,  # 1 or 2
            mindihedral=self.mindihedralSpinBox.value(),
            minratio=self.minRatioDoubleSpinBox.value(),
            maxvolume=self.maxVolumeDoubleSpinBox.value(),
            verbose=1.0 if self.verboseCheckBox.isChecked() else 0.0,
            psc=1.0 if self.preserveSurfaceCheckBox.isChecked() else 0.0
        )

    def on_camera_view_changed(self, view_name: str):
        """Change camera view for both STL and Tet viewers."""
        for renderer in [self.stl_renderer, self.tet_renderer]:
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
            
    def update_view_settings(self):
        """Apply all current display settings to both STL and TET viewers."""
        # === 1. Camera View ===
        current_view = self.cameraViewComboBox.currentText()
        self.on_camera_view_changed(current_view)

        # === 2. Mesh Display Style ===
        show_faces = self.showFacesCheckBox.isChecked()
        show_edges = self.showEdgesCheckBox.isChecked()      

        for actor, renderer, view in [
            (getattr(self, "stl_actor", None), self.stl_renderer, self.stlView),
            (getattr(self, "tet_actor", None), self.tet_renderer, self.tetView)
        ]:
            if actor is None:
                continue  # Mesh not yet loaded

            prop = actor.GetProperty()

            # --- Faces ---
            if show_faces:
                prop.SetRepresentationToSurface()
            else:
                prop.SetRepresentationToWireframe()

            # --- Edges ---
            if show_edges:
                prop.EdgeVisibilityOn()
            else:
                prop.EdgeVisibilityOff()