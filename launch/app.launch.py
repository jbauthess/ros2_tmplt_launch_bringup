# Historic version of launch file. 
# # Not too much used anymore. Advantage : we can add logic, conditions inside the code. 
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():    # this function shall be called with this name
    ld = LaunchDescription()

    node1 = Node(
        package="ros2_tmplt_py",
        executable="client"
    )

    node2 = Node(
        package="ros2_tmplt_cpp",
        executable="server"
    )

    ld.add_action(node1)
    ld.add_action(node2)

    return ld
