#!/usr/bin/env python3
"""Interactive MuJoCo viewer. Assets resolve relative to this script."""
from pathlib import Path
import argparse,time
import mujoco,mujoco.viewer
p=argparse.ArgumentParser();p.add_argument('--animate',action='store_true');args=p.parse_args()
model=mujoco.MjModel.from_xml_path(str(Path(__file__).with_name('scene.xml')))
data=mujoco.MjData(model);mujoco.mj_resetDataKeyframe(model,data,0)
with mujoco.viewer.launch_passive(model,data) as viewer:
 viewer.cam.lookat[:]=[0,0,.27];viewer.cam.distance=1.05;viewer.cam.azimuth=135;viewer.cam.elevation=-20
 while viewer.is_running():
  start=time.monotonic()
  if args.animate:
   import math
   data.ctrl[6]=.025*(1-math.cos(data.time*1.5))
  mujoco.mj_step(model,data);viewer.sync();time.sleep(max(0,model.opt.timestep-(time.monotonic()-start)))
