<div align="center">

# Piper × UMI

`URDF` · `MuJoCo XML` · `USD / Isaac Sim`

<img src="usd/images/isaac_sim_overview.png" alt="Piper 与 UMI 整体装配" width="100%">

</div>

## 当前进度

实物安装已完成，正在进行 **IK 开发**。下一步使用开源数据开展训练与验证。

[安装结论（HTML）](usd/installation_conclusion.html) · 下载后可离线阅读。

## 模型

| 格式 | 模型 | 预览场景 |
| :-- | :-- | :-- |
| URDF | [piper_umi.urdf](urdf/piper_umi.urdf) | — |
| MuJoCo XML | [piper_umi.xml](xml/piper_umi.xml) | [scene.xml](xml/scene.xml) |
| USD / Isaac Sim | [piper_umi.usd](usd/piper_umi.usd) | [scene.usda](usd/scene.usda) |

每个目录包含完整依赖，可独立使用。link6 与安装法兰采用原生件，UMI 支座为白色，软指为浅桔黄色。

<img src="usd/images/isaac_sim_gripper.png" alt="UMI 末端与相机支架" width="100%">

## 3D 打印件

共 **2 种零件、3 件**，文件与当前装配的 v2 版本一致。

| 零件 | 数量 | 用途 | 文件 |
| :-- | :--: | :-- | :-- |
| UMI 手指支座（v2） | **2** | 左右各一件，同款打印两份，无需镜像 | [STL](urdf/printing/umi-piper-finger-sup-v2.stl) · [STEP](urdf/printing/umi-piper-finger-sup-v2.step) |
| Piper 相机支架（v2） | **1** | 固定相机安装接口 | [STL](urdf/printing/piper-camera-base-v2.stl) · [STEP](urdf/printing/piper-camera-base-v2.step) |

STL 单位为 **mm**，切片时按 **100%** 比例导入。软指使用现成或硅胶翻模件；link6 与安装法兰使用原生件。

## 支架偏差

| CAD 比较基准 | 相机安装基准偏差 |
| :-- | --: |
| 原 SW 总装设计叠放位置 | **0.284 mm** |
| 同开度、中线与软指根部平均位置 | **0.386 mm** |

孔轴线基本平行。第二项为 CAD 归一化比较，保留两侧根部 0.420 mm 的高度差。详细条件见 [测量记录](usd/camera_alignment.json)；数值不代表相机光心外参。

## 模型验证

- **资产交付**：URDF、XML、USD 均已独立加载。
- **运动与联动**：已在 MuJoCo 3.3.5 和 Isaac Sim 5.1.0 验证六轴运动与夹爪联动。

## 来源与许可

官方运动学及原生输出盘、法兰来自 [AgileX agx_arm_urdf](https://github.com/agilexrobotics/agx_arm_urdf/tree/f6642ce0d7872c686f29c99e9e10cd23d1d49313)，部分外观颜色参考 [Piper 官方 DAE](https://github.com/agilexrobotics/piper_ros/tree/noetic/src/piper_description/meshes/dae)。各格式目录附来源记录与上游许可；用户提供的 CAD / 网格未统一重新授权。
