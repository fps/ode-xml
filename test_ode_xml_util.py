import ode_xml_util
import ode_schema

xml_instance = ode_schema.CreateFromDocument(file("simpleton.xml").read())

print "Name of the world is " + (xml_instance.World[0].Name)
print "There is " + str(len(xml_instance.Body)) + " body/bodies in it"

sim = ode_xml_util.create_object(xml_instance)

for i in range(1, 100):
    sim["Earth"].quickStep(0.1)
    print sim["Thing"].getPosition()
