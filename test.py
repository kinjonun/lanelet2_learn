import lanelet2
from lanelet2.core import BasicPoint2d
from lanelet2.ml_converter import MapDataInterface

pos = BasicPoint2d(10, 10)                              # set your local reference frame origin
yaw = 0                                                 # set your local reference frame yaw angle (heading)
mDataIf = MapDataInterface(ll2_map)                     # get the MapDataInterface object and pass the ll2 map
mDataIf.setCurrPosAndExtractSubmap2d(pos, yaw)            # extract the local submap
lData = mDataIf.laneData(True)                          # get the LaneData local instance labels
tfData = lData.getTensorInstanceData(True, False)        # get the local instance labels as numpy arrays