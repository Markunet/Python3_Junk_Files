from diagrams import Diagram, Cluster, Edge, Node
from diagrams.generic.network import Switch
from diagrams.onprem.network import Internet


graph_attr = {"spline": "false"}

with Diagram("Clos", show=False, direction="TB", graph_attr=graph_attr):
    with Cluster("Leaf layer"):
        leaf_switches = [
            Switch("leaf1"),
            Switch("leaf2"),
            Switch("leaf3"),
            Switch("leaf4"),
            Switch("leaf5"),
            Switch("leaf6"),
            Switch("leaf7"),
            Switch("leaf8"),
        ]

    with Cluster("External Leaf layer"):
        external_leaf_switches = [
            Switch("ex-leaf1"),
            Switch("ex-leaf2"),
        ]

    with Cluster("Spine layer"):
        spine1 = Switch("spine1")
        spine2 = Switch("spine2")
        spine3 = Switch("spine3")
        spine4 = Switch("spine4")

    with Cluster("External Network"):
        exn = Internet("External Network")

    spine1 >> leaf_switches
    spine2 >> leaf_switches
    spine3 >> leaf_switches
    spine4 >> leaf_switches

    spine1 >> external_leaf_switches
    spine2 >> external_leaf_switches
    spine3 >> external_leaf_switches
    spine4 >> external_leaf_switches

    exn >> external_leaf_switches
