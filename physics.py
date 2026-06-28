import numpy as np
import ball
import wall
import arc

class Physics:
    grav = np.zeros(2)

    def __init__(self):
        #self.collisions = 0
        pass

    def tick(self, objects, gravity: np.array, drag: float) -> int:
        # self.grav = gravity
        collisions = 0
        for obj in objects:
            if not isinstance(obj, ball.Ball):
                continue # other things dont move

            obj.speed += self.grav
            obj.speed *= 1 - drag
            for other in objects:
                if other is obj:
                    continue
                if isinstance(other, ball.Ball):
                    collisions += self.sphereSphereCollision(obj, other)
                    continue
                if isinstance(other, wall.Wall):
                    collisions += self.sphereWallCollision(obj, other)
                    continue
                if isinstance(other, arc.Arc):
                    collisions += self.sphereArcCollision(obj, other)
                    continue
                
            obj.position += obj.speed
        return collisions

    def sphereSphereCollision(self, sphere1: ball.Ball, sphere2: ball.Ball) -> int:
        dist = np.linalg.norm(sphere2.position - sphere1.position)
        if dist > (sphere2.radius + sphere1.radius):
            return 0
        normal = (sphere2.position - sphere1.position)/dist
        v1parallel, v2parallel = np.dot(sphere1.speed, normal), np.dot(sphere2.speed, normal)
        if not v1parallel - v2parallel > 0:
            # Spheres actually already have collided and are moving away from each other
            return 0
        m1, m2 = sphere1.mass, sphere2.mass
        # hier wirds interessant
        sphere1.speed += normal * ((m1*v1parallel+m2*(2*v2parallel-v1parallel))/(m1+m2)-v1parallel)
        sphere2.speed += normal * ((m2*v2parallel+m1*(2*v1parallel-v2parallel))/(m1+m2)-v2parallel)
        return 1
        
    def sphereWallCollision(self, sphere: ball.Ball, wall: wall.Wall) -> int:
        AP, AB = sphere.position - wall.pointA, wall.pointB - wall.pointA
        h = max(0, min(1, np.dot(AP,AB)/np.dot(AB,AB)))
        connection = AP - h*AB
        if np.linalg.norm(connection) > sphere.radius:
            return 0
        normal = -connection/np.linalg.norm(connection)
        vparallel = np.dot(sphere.speed, normal)
        if not vparallel > 0:
            return 0
        sphere.speed -= 2 * normal * vparallel
        return 1

    def sphereArcCollision(self, sphere: ball.Ball, arc: arc.Arc) -> int:
        return 0
