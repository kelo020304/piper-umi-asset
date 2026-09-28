from pathlib import Path
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    folder=Path(__file__).resolve().parent
    # Canonical URDF stays relative. RViz uses ROS resource_retriever file URIs at runtime.
    text=(folder/'piper_umi.urdf').read_text()
    text=text.replace('filename="meshes/', 'filename="'+(folder/'meshes').as_uri()+'/')
    return LaunchDescription([
      Node(package='robot_state_publisher',executable='robot_state_publisher',parameters=[{'robot_description':text}]),
      Node(package='joint_state_publisher_gui',executable='joint_state_publisher_gui',parameters=[{'robot_description':text}]),
      Node(package='rviz2',executable='rviz2',arguments=['-d',str(folder/'view.rviz')])])
