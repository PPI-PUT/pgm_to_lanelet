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

import rclpy
from rclpy.node import Node
from pgm_to_lanelet import PgmToLanelet


class PgmToLaneletNode(Node):

    def __init__(self) -> None:
        super().__init__('pgm_to_lanelet_node')
        self.pgm_to_lanelet = PgmToLanelet()
        self.pgm_to_lanelet.set_parameters(
            map_yaml_path=self.declare_parameter('map_yaml_path', 'map.yaml').value,
            line_width=self.declare_parameter('line_width', 1).value,
            point_size=self.declare_parameter('point_size', 1).value,
        )
        self.pgm_to_lanelet.execute()


def main(args=None):
    rclpy.init(args=args)
    node = PgmToLaneletNode()
    try:
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
