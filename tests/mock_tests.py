import numpy.testing as npt
from unittest.mock import Mock

def test_mock_source():
  from <folder/module> import <function>
  data_source = Mock()
  data_source.<data_loading_function>.return_value = <standard_value>

  result = <function>(data_source)
  expected_output = <expected_output_in_right_data_type>
  # Assert statment example
  npt.assert_array_almost_equal(result, expected_output)
  
