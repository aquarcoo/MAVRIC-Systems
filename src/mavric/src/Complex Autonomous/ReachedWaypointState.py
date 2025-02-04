import complex_globals as g
import time

from StateMachine import State

class ReachedWayPoint(State):
    def __init__(self, stateMachine):
        self._stateMachine = stateMachine
    
    def enter(self):
        g.drive_pub.publish(0, 0, 0, 0, 0, 0)
        g.steer_pub.publish(0, 0, 0, 0)
        self.blink = True
        g.indicator_pub.publish(self.blink, 255, "Green")
        self.stop_time = time.time()
        self.blink_time = time.time()


    def run(self):
        if time.time() - self.blink_time > 0.75:
            self.blink = abs(self.blink-1)
            g.indicator_pub.publish(self.blink, 255, "Green")
            self.blink_time = time.time()

    def next(self):
	    #eventually go into CV state
        if time.time() - self.stop_time > 5:
            g.indicator_pub.publish(False, 255, "Green")
            if(len(g.waypoints) > 1):
                g.pathpoint_num = -1
                g.waypoints.pop(0)
                g.waypoint_id.pop(0)
                g.path.set_end_point(g.waypoints[0])
                return self._stateMachine.nextPathPoint

            if(len(g.waypoints) > 0):
                g.pathpoint_num = 0
                g.waypoints.pop(0)
                g.waypoint_id.pop(0)
                return self._stateMachine.idle
        
        return self._stateMachine.reachedWaypoint