def param_to_slider(param_value, min_val, max_val):
    """
    Map an actual parameter value to a slider value (0-100)
    """
    slider_value = (param_value - min_val) / (max_val - min_val) * 100
    return int(round(slider_value))


def init_tetgen_settings(widget):
    """
    Initialize TetGen settings widgets with default values.
    The slider values are mapped from actual TetGen parameters.
    """
    widget.orderComboBox.setCurrentIndex(0)  # default: Linear

    # Map TetGen default values to slider values
    widget.mindihedralSlider.setValue(param_to_slider(20, min_val=1, max_val=180))
    widget.minRatioDoubleSlider.setValue(param_to_slider(1.5, min_val=1.0, max_val=10.0))
    widget.maxVolumeDoubleSlider.setValue(param_to_slider(1.0, min_val=0.001, max_val=1.0))

    widget.preserveSurfaceCheckBox.setChecked(True)
    widget.verboseCheckBox.setChecked(False)



def slider_to_param(slider_value, min_val, max_val, step=None):
    """Convert slider value (0-100) to actual parameter value with optional rounding."""
    val = min_val + (slider_value / 100.0) * (max_val - min_val)
    if step:
        val = round(val / step) * step
        
    val = round(val, 2) 
    return val


def get_tetgen_parameters(widget):
    """
    Read current TetGen settings from widgets in the given widget instance.
    Slider values are converted from 0-100 to actual parameter ranges.
    Returns:
        dict of parameters
    """

    return dict(
        order=widget.orderComboBox.currentIndex() + 1,

        # Translate sliders to actual ranges
        mindihedral=slider_to_param(
            widget.mindihedralSlider.value(), min_val=1, max_val=180, step=1
        ),
        minratio=slider_to_param(
            widget.minRatioDoubleSlider.value(), min_val=1.0, max_val=10.0, step=0.1
        ),
        maxvolume=slider_to_param(
            widget.maxVolumeDoubleSlider.value(), min_val=0.001, max_val=1.0, step=0.001
        ),

        # Checkboxes
        verbose=1.0 if widget.verboseCheckBox.isChecked() else 0.0,
        psc=1.0 if widget.preserveSurfaceCheckBox.isChecked() else 0.0
    )


