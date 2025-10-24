import vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from ui_widget import Ui_Widget  # your generated UI from Qt Designer


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Surf2Mesh")

        # Connect button click
        self.selectFileButton.clicked.connect(self.select_stl_file)

        # Prepare VTK renderer
        self.renderer = vtk.vtkRenderer()
        self.stlView.GetRenderWindow().AddRenderer(self.renderer)
        self.interactor = self.stlView.GetRenderWindow().GetInteractor()
        self.interactor.Initialize()

        # Add XYZ axes widget
        axes = vtk.vtkAxesActor()
        self.axes_widget = vtk.vtkOrientationMarkerWidget()
        self.axes_widget.SetOrientationMarker(axes)
        self.axes_widget.SetInteractor(self.interactor)
        self.axes_widget.SetViewport(0.0, 0.0, 0.2, 0.2)  # bottom-left corner
        self.axes_widget.SetEnabled(1)
        self.axes_widget.InteractiveOff()  # Make it non-draggable

    def select_stl_file(self):
        # Open a file dialog to select STL
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select STL file",
            "",
            "STL Files (*.stl);;All Files (*)"
        )
        if file_path:
            print(f"Selected STL: {file_path}")
            self.display_stl(file_path)

    def display_stl(self, file_path):
        """Display the STL file in the VTK 3D viewer."""
        # Clear previous objects from renderer
        self.renderer.RemoveAllViewProps()

        # Read STL file
        reader = vtk.vtkSTLReader()
        reader.SetFileName(file_path)

        # Map geometry to graphics primitives
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())

        # Create an actor for the mesh
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Add actor to renderer
        self.renderer.AddActor(actor)
        self.renderer.SetBackground(0.1, 0.1, 0.1)
        self.renderer.ResetCamera()

        # Refresh the render window
        self.stlView.GetRenderWindow().Render()