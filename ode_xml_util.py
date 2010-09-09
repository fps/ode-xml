import ode_schema
import ode



def create_sim(object, named_objects = dict()):
    print "create_sim"
    for object in object.World + object.Space + object.Body + object.Geom:
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
    return b

def create_box_total_mass(object, named_objects = dict()):
    print "create box total mass"
    m = ode.Mass()
    m.setBoxTotal(object.TotalMass, object.LX, object.LY, object.LZ)
    return m


# argument is a subclass of robosim_schema.RSObject
def create_object(object, named_objects = dict()):
    # print factory_functions
    o = factory_functions[object.__class__](object, named_objects)
    if hasattr(object, "Name"):
        named_objects[object.Name] = o
        
    return o


factory_functions = {robosim_schema.Sim_ : create_sim, robosim_schema.World_ : create_world, robosim_schema.Body_ : create_body, robosim_schema.BoxTotalMass : create_box_total_mass }



    
