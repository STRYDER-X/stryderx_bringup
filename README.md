# stryderx_bringup

![ROS 2](https://img.shields.io/badge/ROS%202-Humble-blue)
[![License](https://img.shields.io/badge/license-GPLv3-blue.svg)](LICENSE)

`stryderx_bringup` is a standalone ROS 2 package for starting the StryderX hardware stack. It owns the launch files and runtime parameter files that wire joystick input, drive control, steering control, and camera streaming together.

## Package Contents

| Path | Purpose |
| :--- | :--- |
| `launch/hardware.launch.py` | Starts joystick input, drive control, steering control, and camera streaming. |
| `launch/joystick.launch.py` | Starts `joy_node` and the StryderX joystick teleop node. |
| `launch/drive.launch.py` | Starts the drive controller with ESC angle limits. |
| `launch/steering.launch.py` | Starts the steering controller with servo angle limits. |
| `launch/camera.launch.py` | Starts the camera server with camera runtime settings. |
| `config/*.yaml` | Runtime parameters consumed by the launch files. |

## Dependencies

- ROS 2 Humble.
- `ament_cmake`.
- `launch` and `launch_ros`.
- `ament_index_python`.
- `joy` for joystick input.
- `stryderx_hardware` for the robot-facing controller and camera nodes.
- Robot hardware access when running the full stack:
  - `/dev/video0` for the USB camera.
  - The serial device expected by `stryderx_hardware`.
  - `/dev/input/eventX` devices for joystick input.

## Build

Place this package in the `src/` directory of a ROS 2 workspace:

```bash
mkdir -p ~/stryderx_ws/src
```

Make sure `stryderx_hardware` is also available in the same workspace or installed in the active ROS environment.

From the workspace root, build this package:

```bash
cd ~/stryderx_ws
colcon build --packages-select stryderx_bringup --symlink-install
source install/setup.bash
```

## Launch The Full Hardware Stack

Use `hardware.launch.py` to start all configured hardware nodes:

```bash
ros2 launch stryderx_bringup hardware.launch.py
```

This includes:

- `joy/joy_node`
- `stryderx_hardware/joystick_teleop`
- `stryderx_hardware/drive_controller`
- `stryderx_hardware/steering_controller`
- `stryderx_hardware/camera_server`

## Launch Individual Subsystems

Joystick input and teleop:

```bash
ros2 launch stryderx_bringup joystick.launch.py
```

Drive controller:

```bash
ros2 launch stryderx_bringup drive.launch.py
```

Steering controller:

```bash
ros2 launch stryderx_bringup steering.launch.py
```

Camera server:

```bash
ros2 launch stryderx_bringup camera.launch.py
```

## Configuration

Runtime settings live in `config/` and are installed into the package share directory during the build.

| File | Main Parameters |
| :--- | :--- |
| `camera_params.yaml` | `camera_name`, `camera_type`, `device_index`, `fps`, `timeout_seconds` |
| `drive_controller_params.yaml` | `esc_min_angle`, `esc_max_angle` |
| `steering_controller_params.yaml` | `min_angle`, `max_angle` |
| `joystick_params.yaml` | `left_joystick`, `left_trigger`, `right_trigger` |

After changing a config file, rebuild or use `--symlink-install` during development so launch files pick up the latest values.

## Development Checks

Run the package tests and lint checks from the workspace root:

```bash
colcon test --packages-select stryderx_bringup
colcon test-result --verbose
```

## Maintainer

- Julian A. Rendon
- julianrendon514@gmail.com
