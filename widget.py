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
from mesh.viewer_infos import setup_viewers, update_view_settings
from mesh.facenormals import update_face_normals

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Surf2Mesh")
        
        # Setup STL and Tet viewers
        setup_viewers(self)

        # Initialize TetGen settings
        init_tetgen_settings(self)

        # Connect buttons
        self.selectFileButton.clicked.connect(lambda: select_stl_file(self))      
        self.generateMeshButton.clicked.connect(lambda: generate_tet_mesh(self))       

        # Connect UI signals
        self.cameraViewComboBox.currentTextChanged.connect(lambda _: update_view_settings(self))
        self.viewModeComboBox.currentTextChanged.connect(lambda _: update_view_settings(self))
        self.normalsLengthLabelSpinBox.valueChanged.connect(lambda _: update_face_normals(self))
        self.tessellatedSlider.valueChanged.connect(lambda: update_clipped_mesh(self))
      
  


