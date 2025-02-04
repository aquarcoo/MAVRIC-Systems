#!/usr/bin/env python

#import modules
import auto_globals
import rospy

from std_msgs.msg import String
from std_msgs.msg import Bool
from geometry_msgs.msg import Vector3
from mavric.msg import Autonomous, Waypoint, Drivetrain, Steertrain, GPS#, LED

from StateMachine import StateMachine, State
from IdleState import Idle
from TurnTowardWaypointState import TurnTowardWaypoint
from DriveTowardWaypointState import DriveTowardWaypoint
from ReachedWaypointState import ReachedWaypoint

# define state machine class


class AutonomousStateMachine(StateMachine):
    def __init__(self):
        StateMachine.__init__(self, AutonomousStateMachine.idle)


AutonomousStateMachine.idle = Idle(AutonomousStateMachine)
AutonomousStateMachine.turnTowardWaypoint = TurnTowardWaypoint(AutonomousStateMachine)
AutonomousStateMachine.driveTowardWaypoint = DriveTowardWaypoint(AutonomousStateMachine)
AutonomousStateMachine.reachedWaypoint = ReachedWaypoint(AutonomousStateMachine)

# define functions


def hms_to_s(h, m, s):
    # convert from hours-minutes-seconds to seconds
    return (h * 60 * 60) + (m * 60) + s


def cmd_cb(data):
    # enable/disable autonomous, forget current waypoints
    if data.command == 'E':
        auto_globals.enabled = True
        #auto_globals.indicator_pub(True, 255, "RED")

    elif data.command == 'D':
        auto_globals.enabled = False
        #auto_globals.indicator_pub(True, 255, "BLUE")

    elif data.command == 'F':
        auto_globals.waypoints = []


def waypoint_cb(data):
    # add new waypoint to list
    auto_globals.waypoints.append([data.latitude, data.longitude])

def gps_fix_cb(data):
    auto_globals.good_fix = data.data


def gps_cb(data):
    # how often does the gps publish? do we have to compare values here?

    auto_globals.prev_position = auto_globals.position
    auto_globals.position = [data.longitude, data.latitude]
    auto_globals.fix_time = hms_to_s(data.time_h, data.time_m, data.time_s)
    #auto_globals.heading = data.heading


def imu_cb(data):
    if auto_globals.good_imu:
        auto_globals.heading = data.z


def imu_cal_cb(data):
    auto_globals.good_imu = True

    # if data.z > 0:
    #    auto_globals.good_imu = True
    # else:
    #    auto_globals.good_imu = False


# main loop
auto = AutonomousStateMachine()


def main():
    # setup ROS node
    rospy.init_node("ANS")

    #init publishers
    auto_globals.drive_pub = rospy.Publisher("Drive_Train", Drivetrain, queue_size=10)
    auto_globals.steer_pub = rospy.Publisher("Steer_Train", Steertrain, queue_size=10)
    auto_globals.debug_pub = rospy.Publisher("Autonomous_Debug", String, queue_size=10)
    #auto_globals.indicator_pub = rospy.Publisher("/indicators/light_pole", LED, queue_size=10)


    cmd_sub = rospy.Subscriber("Autonomous", Autonomous, cmd_cb, queue_size=10)
    way_sub = rospy.Subscriber("Next_Waypoint", Waypoint, waypoint_cb, queue_size=10)
    gps_fix_sub = rospy.Subscriber("GPS_Fix", Bool, gps_fix_cb, queue_size=10)
    gps_sub = rospy.Subscriber("GPS", GPS, gps_cb, queue_size=10)

    imu_sub = rospy.Subscriber("FusedAngle", Vector3, imu_cb, queue_size=10)
    imu_cal_sub = rospy.Subscriber("SensorCalibrations", Vector3, imu_cal_cb, queue_size=10)

    auto_globals.Scale = rospy.get_param("~Range", 0.5)
    auto_globals.Rover_Width = rospy.get_param("~Rover_Width", 1)
    auto_globals.Rover_MinTurnRadius = rospy.get_param("~Rover_MinTurnRadius", 2)

    rate = rospy.Rate(2)  # 2 Hz

    while not rospy.is_shutdown():
        auto.run()
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
