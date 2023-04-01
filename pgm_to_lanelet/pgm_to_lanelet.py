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

from pathlib import Path
import cv2
from yaml import safe_load


class PgmToLanelet:

    def __init__(self) -> None:
        self._map_yaml_path = 'map.yaml'
        self._line_width = 1
        self._point_size = 1
        self._map_cfg = None

    def set_parameters(self, **kwargs) -> None:
        for arg in kwargs:
            if hasattr(self, '_' + arg):
                setattr(self, '_' + arg, kwargs[arg])

    def execute(self) -> None:
        self.load_map()
        img = cv2.imread(
            (Path(self._map_yaml_path).parent / self._map_cfg['image']).as_posix(),
            cv2.IMREAD_GRAYSCALE)

        pass

    def load_map(self) -> None:
        with open(self._map_yaml_path, 'r') as f:
            self._map_cfg = safe_load(f)
