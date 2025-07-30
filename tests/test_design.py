import sys
import os
import pytest

# Add parent directory to path for local imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from design import generate_ff_design

def test_design_shape():
    df = generate_ff_design(3)
    assert df.shape[1] == 3
    assert df.shape[0] == 4

def test_invalid_factor_range():
    with pytest.raises(ValueError):
        generate_ff_design(1)
