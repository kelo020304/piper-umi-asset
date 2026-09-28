# Piper + UMI — standalone URDF

Entry: `piper_umi.urdf`. Keep `meshes/` beside it. All mesh paths are relative; this folder can be copied independently. No xacro or external model package is needed to parse the canonical model.

The URDF includes the right-finger `<mimic>` relation. Consumers must implement mimic semantics. MuJoCo's direct URDF importer does not apply this relation as a constraint; use the separately supplied MJCF package for MuJoCo simulation.

## ROS 2 visualization

Copy this folder as `src/piper_umi_description` in a ROS 2 workspace, then:

```bash
colcon build --packages-select piper_umi_description
source install/setup.bash
ros2 launch piper_umi_description display.launch.py
```

The launch file resolves local mesh paths to `file://` URLs at runtime for RViz. It starts robot_state_publisher, joint_state_publisher_gui and RViz; drive the left finger slider. Software dependencies are listed in `package.xml`. This ROS launch was source-checked, but not executed on this machine.

For a dynamics importer, select fixed-base import. No transmissions, ROS control hardware plugin, or real-arm driver is included.

## Model conventions

SI units: metres, kilograms, radians (USD angular drive/limit attributes use degrees per USD convention). Z is up. `base_link` is the robot base; `tool0` is a nominal midpoint near the finger tips, not a measured TCP calibration.

Six revolute arm joints: `joint1`–`joint6`. Two prismatic finger joints: `gripper_left_joint`, `gripper_right_joint`. Both scalar coordinates increase outward, with opposite spatial axes. Right follows left with multiplier +1. There are 8 physical joint coordinates and 7 independent controls.

Control **one-finger travel q = 0…0.05 m**. The nominal total stroke is 100 mm. Due to the UMI mounting geometry, the projected inner finger gap is approximately **2.882 mm + 2q**, with q expressed in mm: approximately 2.882–102.882 mm. The model minimum leaves 0.2 mm between the slider bodies. These are CAD-derived model limits and a nominal 100 mm stroke, not measured hardware limits. The 0.2 m/s single-finger velocity limit is a simulation default. The saved CAD pose uses q ≈ 0.029968804 m; full joint state is in `model_info.json`.

The soft fingers are **rigid bodies**. The parallel motion is idealized; gear/linkage contact transmission and silicone deformation are not simulated. Visuals combine the supplied Piper appearance, stock disk/flange and custom CAD gripper. Arm collisions retain the calibrated CAD hull approximation; stock disk/flange and custom gripper use convex hulls, with adjacent mating-body collisions excluded. Concave holes and slots are therefore simplified for contact.

Arm masses/inertias are official nominal values. Custom end-effector masses/inertias are estimated from CAD: drive/rail aggregate 0.45 kg, printed supports 1250 kg/m³, soft fingers 1050 kg/m³, sliders 7800 kg/m³. Physical material densities were not measured. The stock flange uses its official nominal inertia; visual paint colors do not set physical density.

## Appearance and native mounting revision

The two UMI finger supports are white (RGBA 0.95, 0.95, 0.95, 1); the two fingers are light apricot-yellow (1, 0.67, 0.30, 1). Base through link5 use 76 supplied material-separated Piper OBJ meshes. Official DAE diffuse colors restore the archive's missing material library, including dark covers and contrasting label geometry. The robot needs no external image textures or MTL libraries. The USD demo scene includes its own local blue checker floor texture.

`link6` uses the stock output disk. A stock `flange_link` replaces the custom `UMI-PIPER-CAMERA-MOUNT`; its joint to link6 is fixed. The gripper drive is mounted at the official +4.5 mm offset. Relative to the previous custom mount, the retained end effector shifts approximately +3.013 mm along link6 Z, with minor XY centering corrections (0.087 mm and 0.0035 mm). Exact transforms are in `model_info.json`. The custom 155 mm rail, UMI finger spacing, 100 mm nominal total stroke and camera base are retained. The archive's different 145 mm stock gripper is not substituted.


## Camera mount comparison

The original SolidWorks design overlay gives a **0.284 mm** camera-mount datum offset with effectively parallel hole axes. Aligning the mechanism centrelines at equal opening and using the mean finger-root position gives **0.386 mm**: (+0.002, -0.341, +0.180) mm along opening, fingertip and height directions. The Piper roots retain a 0.420 mm height difference; the assembly is not tilted to force both root points to coincide. One fork gap is 2 mm wider. These are mechanical CAD measurements; see `camera_alignment.json` for the reference definitions.
