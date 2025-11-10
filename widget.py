import vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PySide6.QtWidgets import QWidget, QFileDialog, QDialog, QVBoxLayout, QLabel, QProgressBar
from ui_applayout import Ui_Widget  # generated from Qt Designer
import numpy as np
import pyvista as pv
from surf2tet.tetgen_settings import init_tetgen_settings
from surf2tet.mesh_generator import generate_tet_mesh
from mesh.select_file import select_stl_file
from mesh.clipping import update_clipped_mesh
from mesh.viewer_infos import update_view_settings
from mesh.facenormals import update_face_normals

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Surf2Mesh")
                
        # Initialize TetGen settings
        init_tetgen_settings(self)

        # === Connect button ===
        self.selectFileButton.clicked.connect(lambda: select_stl_file(self))      
        self.generateMeshButton.clicked.connect(lambda: generate_tet_mesh(self))

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
                
        self.cameraViewComboBox.currentTextChanged.connect(
            lambda _: update_view_settings(self)
        )
        self.viewModeComboBox.currentTextChanged.connect(
            lambda _: update_view_settings(self)
        )
        self.normalsLengthLabelSpinBox.valueChanged.connect(lambda _: update_face_normals(self)) 
        self.tessellatedSlider.valueChanged.connect(lambda: update_clipped_mesh(self))     
      
  


