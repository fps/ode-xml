import ode_schema
import ode



def create_sim(object, named_objects = dict()):
    print "create_sim"
    for object in object.World + object.Space + object.Body + object.Geom + object.Joint:
        create_object(object, named_objects)

    return named_objects
    

def create_world(object, named_objects = dict()):
    print "create_world"
    w = ode.World()
    w.setGravity([float(object.Gravity.X), float(object.Gravity.Y), float(object.Gravity.Z)])
    return w


def create_body(object, named_objects = dict()):
    print "create body"
    b = ode.Body(named_objects[object.World])
    b.setMass(create_object(object.Mass, named_objects))

    if object.GravityMode != None:
        if object.GravityMode:
            b.setGravityMode(True)
        else:
            b.setGravityMode(False)

    if object.Position != None:
        b.setPosition(create_vector(object.Position))
    return b

def attach_joint_to_bodies(joint, object, named_objects = dict()):
    if object.Body1 == "None":
        b1 = None
    else:
        b1 = named_objects[object.Body1]

    if object.Body2 == "None":
        b2 = None
    else:
        b2 = named_objects[object.Body2]

    joint.attach(b1,b2)
        

def create_vector(object):
    return [float(object.X), float(object.Y), float(object.Z)]

def create_hinge_joint(object, named_objects = dict()):
    print "create body"
    b = ode.HingeJoint(named_objects[object.World])
    attach_joint_to_bodies(b, object, named_objects)
    if object.Axis != None:
        b.setAxis(create_vector(object.Axis))
    return b


def create_box_total_mass(object, named_objects = dict()):
    print "create box total mass"
    m = ode.Mass()
    m.setBoxTotal(float(object.M), float(object.LX), float(object.LY), float(object.LZ))
    return m


# argument is a subclass of robosim_schema.RSObject
def create_object(object, named_objects = dict()):
    # print factory_functions
    o = factory_functions[object.__class__](object, named_objects)
    if hasattr(object, "Name"):
        named_objects[object.Name] = o
        
    return o


factory_functions = {ode_schema.Sim_ : create_sim, ode_schema.World_ : create_world, ode_schema.Body_ : create_body, ode_schema.HingeJoint_ : create_hinge_joint, ode_schema.BoxTotalMass : create_box_total_mass }



    
