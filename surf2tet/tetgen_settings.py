def init_tetgen_settings(widget):
    """
    Initialize TetGen settings widgets with default values.
    
    Parameters:
        widget: instance of Widget class that has the TetGen UI widgets
    """
    widget.orderComboBox.setCurrentIndex(0)  # default: Linear
    widget.mindihedralSpinBox.setValue(20)   # Min dihedral angle
    widget.minRatioDoubleSpinBox.setValue(1.5)  # Min ratio
    widget.maxVolumeDoubleSpinBox.setValue(1.0) # Max volume
    widget.preserveSurfaceCheckBox.setChecked(True)
    widget.verboseCheckBox.setChecked(False)


def get_tetgen_parameters(widget):
    """
    Read current TetGen settings from widgets in the given widget instance.
    
    Returns:
        dict of parameters
    """
    return dict(
        order=widget.orderComboBox.currentIndex() + 1,
        mindihedral=widget.mindihedralSpinBox.value(),
        minratio=widget.minRatioDoubleSpinBox.value(),
        maxvolume=widget.maxVolumeDoubleSpinBox.value(),
        verbose=1.0 if widget.verboseCheckBox.isChecked() else 0.0,
        psc=1.0 if widget.preserveSurfaceCheckBox.isChecked() else 0.0
    )
    

