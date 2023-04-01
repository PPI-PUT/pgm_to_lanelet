#!/usr/bin/env python3

# Copyright 2023 Perception for Physical Interaction Laboratory at Poznan University of Technology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pgm_to_lanelet.pgm_to_lanelet import PgmToLanelet
import pytest


@pytest.mark.parametrize('test_input, expected', [
    ('line_width', 2),
])
def test_custom_param(test_input, expected):
    pgm_to_lanelet = PgmToLanelet()
    pgm_to_lanelet.set_parameters(line_width=test_input)
    assert pgm_to_lanelet._line_width == expected, 'Wrong value after parametrization'
