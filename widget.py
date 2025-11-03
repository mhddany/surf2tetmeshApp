import vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PySide6.QtWidgets import QWidget, QFileDialog, QDialog, QVBoxLayout, QLabel, QProgressBar
from ui_widget import Ui_Widget  # generated from Qt Designer
import numpy as np
import pyvista as pv


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
        
        self.stl_actor = None
        self.tet_actor = None
        self.stl_normals_actor = None
        self.tet_normals_actor = None
                
        self.cameraViewComboBox.currentTextChanged.connect(self.update_view_settings)
        self.viewModeComboBox.currentTextChanged.connect(self.update_view_settings)
        self.normalsLengthLabelSpinBox.valueChanged.connect(self.update_view_settings)

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
            self.stl_mesh = pv.read(file_path)
            print(f"Selected STL: {file_path}")
            self.display_stl(self.stl_mesh)
            
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
            self.tet_mesh = self.fem_obj.fem_mesh
            print(f"Generated Tetrahedral Mesh: {self.fem_obj.fem_mesh}")
            self.display_tet_mesh(self.fem_obj.fem_mesh)

        worker.finished.connect(handle_result)      
                    
    # === STL display ===
    def display_stl(self, mesh_polydata):
        """Display STL mesh in stlView."""
        self.stl_renderer.RemoveAllViewProps()

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(mesh_polydata)

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(0.83, 0.83, 0.83)
        actor.GetProperty().EdgeVisibilityOn()
        actor.GetProperty().SetEdgeColor(0.2, 0.2, 0.2)
        actor.GetProperty().SetLineWidth(1.0)

        self.stl_actor = actor
        self.stl_renderer.AddActor(actor)
        self.stl_renderer.SetBackground(0.878, 0.949, 0.808)
        self.stl_renderer.ResetCamera()
        self.stlView.GetRenderWindow().Render()

        # Update display settings
        self.update_view_settings()

        # Update STL info labels
        self.update_stl_info_labels(mesh_polydata, self.stl_file)

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
        
        # Update display settings
        self.update_view_settings()

        # Update Tet mesh info labels
        self.update_tet_info_labels(self.tet_mesh)
        
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
            
    def update_stl_info_labels(self, mesh_polydata, file_path=None):
        """
        Update STL info labels:
        - File name
        - Number of points
        - Number of faces (vertices)
        """
        import os

        # Update file name
        if file_path:
            file_name = os.path.basename(file_path)
        else:
            file_name = "Unknown"
        self.stlFileNameLabel.setText(f"File: {file_name}")

        # Update number of points
        n_points = mesh_polydata.n_points
        self.stlPointsLabel.setText(f"Points: {n_points}")

        # Update number of faces / vertices
        n_faces = mesh_polydata.n_cells
        self.stlVerticesLabel.setText(f"Faces: {n_faces}")
        
    def update_tet_info_labels(self, tet_mesh):
        """
        Update tetrahedral mesh info labels:
        - Nodes
        - Edges
        - Elements (tets)
        """
        if tet_mesh is None:
            self.tetNodesLabel.setText("Nodes: 0")
            self.tetEdgesLabel.setText("Edges: 0")
            self.tetElementsLabel.setText("Elements: 0")
            return

        # Number of nodes
        n_nodes = tet_mesh.n_points
        self.tetNodesLabel.setText(f"Nodes: {n_nodes}")

        # Number of edges
        # Extract edges as PolyData and count lines
        edges_polydata = tet_mesh.extract_all_edges()
        n_edges = edges_polydata.n_lines
        self.tetEdgesLabel.setText(f"Edges: {n_edges}")

        # Number of elements (tets)
        n_elements = tet_mesh.n_cells
        self.tetElementsLabel.setText(f"Elements: {n_elements}")

            
    def update_view_settings(self):
        """
        Apply all current display settings to both STL and Tet viewers:
        - Camera orientation
        - Display mode (Surface, Surface+Edges, Wireframe, Points)
        - Normals arrows (controlled by spinbox)
        """
        # --- 1. Camera ---
        current_view = self.cameraViewComboBox.currentText()
        self.on_camera_view_changed(current_view)

        # --- 2. Display Mode ---
        display_mode = self.viewModeComboBox.currentText()
        normals_length = self.normalsLengthLabelSpinBox.value()

        for actor, renderer, view, normals_actor_attr in [
            (self.stl_actor, self.stl_renderer, self.stlView, "stl_normals_actor"),
            (self.tet_actor, self.tet_renderer, self.tetView, "tet_normals_actor")
        ]:
            if actor is None:
                print("no available actors")
                continue
                

            prop = actor.GetProperty()
            # Reset
            prop.SetRepresentationToSurface()
            prop.EdgeVisibilityOff()
            prop.SetOpacity(1.0)

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

            # --- Normals ---
            # Remove previous normals actor
            if getattr(self, normals_actor_attr, None):
                renderer.RemoveActor(getattr(self, normals_actor_attr))
                setattr(self, normals_actor_attr, None)

            if normals_length > 0:
                # Compute normals
                # For STL, actor.GetMapper().GetInput() returns vtkPolyData
                # For Tet, convert actor to PyVista PolyData or use stored mesh
                mesh = getattr(self, "stl_mesh" if actor == self.stl_actor else "tet_mesh", None)
                if mesh is None:
                    print("no available mesh")
                    continue

                centroids, normals, surf_polydata = self.compute_surface_normals(mesh)

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
                setattr(self, normals_actor_attr, normals_actor)

            # Re-render
            renderer.GetRenderWindow().Render()    
    
    def compute_surface_normals(self, mesh):
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

