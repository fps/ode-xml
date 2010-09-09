# ./ode-schema.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2010-09-10 00:19:15.008009 by PyXB version 1.1.2
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:47a0ada8-bc60-11df-a135-00e04da8a2a1')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])
ModuleRecord = Namespace.lookupModuleRecordByUID(_GenerationUID, create_if_missing=True)
ModuleRecord._setModule(sys.modules[__name__])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a Python instance."""
    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=Namespace.fallbackNamespace(), location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, _fallback_namespace=default_namespace)


# Complex type RSObject with content type ELEMENT_ONLY
class RSObject (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RSObject')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__AbsentNamespace0_RSObject_Name', False)

    
    Name = property(__Name.value, __Name.set, None, None)


    _ElementMap = {
        __Name.name() : __Name
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'RSObject', RSObject)


# Complex type GeomObject with content type ELEMENT_ONLY
class GeomObject (RSObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GeomObject')
    # Base type is RSObject
    
    # Element Enable uses Python identifier Enable
    __Enable = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Enable'), 'Enable', '__AbsentNamespace0_GeomObject_Enable', False)

    
    Enable = property(__Enable.value, __Enable.set, None, None)

    
    # Element CollideBits uses Python identifier CollideBits
    __CollideBits = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'CollideBits'), 'CollideBits', '__AbsentNamespace0_GeomObject_CollideBits', False)

    
    CollideBits = property(__CollideBits.value, __CollideBits.set, None, None)

    
    # Element Rotation uses Python identifier Rotation
    __Rotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Rotation'), 'Rotation', '__AbsentNamespace0_GeomObject_Rotation', False)

    
    Rotation = property(__Rotation.value, __Rotation.set, None, None)

    
    # Element Name (Name) inherited from RSObject
    
    # Element CategoryBits uses Python identifier CategoryBits
    __CategoryBits = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'CategoryBits'), 'CategoryBits', '__AbsentNamespace0_GeomObject_CategoryBits', False)

    
    CategoryBits = property(__CategoryBits.value, __CategoryBits.set, None, None)

    
    # Element Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Position'), 'Position', '__AbsentNamespace0_GeomObject_Position', False)

    
    Position = property(__Position.value, __Position.set, None, None)

    
    # Element Quaternion uses Python identifier Quaternion
    __Quaternion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Quaternion'), 'Quaternion', '__AbsentNamespace0_GeomObject_Quaternion', False)

    
    Quaternion = property(__Quaternion.value, __Quaternion.set, None, None)


    _ElementMap = RSObject._ElementMap.copy()
    _ElementMap.update({
        __Enable.name() : __Enable,
        __CollideBits.name() : __CollideBits,
        __Rotation.name() : __Rotation,
        __CategoryBits.name() : __CategoryBits,
        __Position.name() : __Position,
        __Quaternion.name() : __Quaternion
    })
    _AttributeMap = RSObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'GeomObject', GeomObject)


# Complex type SpaceBase with content type ELEMENT_ONLY
class SpaceBase (GeomObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SpaceBase')
    # Base type is GeomObject
    
    # Element Rotation (Rotation) inherited from GeomObject
    
    # Element CollideBits (CollideBits) inherited from GeomObject
    
    # Element Geom uses Python identifier Geom
    __Geom = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Geom'), 'Geom', '__AbsentNamespace0_SpaceBase_Geom', True)

    
    Geom = property(__Geom.value, __Geom.set, None, None)

    
    # Element Quaternion (Quaternion) inherited from GeomObject
    
    # Element Name (Name) inherited from RSObject
    
    # Element CategoryBits (CategoryBits) inherited from GeomObject
    
    # Element Position (Position) inherited from GeomObject
    
    # Element Enable (Enable) inherited from GeomObject

    _ElementMap = GeomObject._ElementMap.copy()
    _ElementMap.update({
        __Geom.name() : __Geom
    })
    _AttributeMap = GeomObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SpaceBase', SpaceBase)


# Complex type GeomCapsule with content type ELEMENT_ONLY
class GeomCapsule (GeomObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GeomCapsule')
    # Base type is GeomObject
    
    # Element Rotation (Rotation) inherited from GeomObject
    
    # Element CollideBits (CollideBits) inherited from GeomObject
    
    # Element Enable (Enable) inherited from GeomObject
    
    # Element Length uses Python identifier Length
    __Length = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Length'), 'Length', '__AbsentNamespace0_GeomCapsule_Length', False)

    
    Length = property(__Length.value, __Length.set, None, None)

    
    # Element Radius uses Python identifier Radius
    __Radius = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Radius'), 'Radius', '__AbsentNamespace0_GeomCapsule_Radius', False)

    
    Radius = property(__Radius.value, __Radius.set, None, None)

    
    # Element CategoryBits (CategoryBits) inherited from GeomObject
    
    # Element Name (Name) inherited from RSObject
    
    # Element Position (Position) inherited from GeomObject
    
    # Element Quaternion (Quaternion) inherited from GeomObject

    _ElementMap = GeomObject._ElementMap.copy()
    _ElementMap.update({
        __Length.name() : __Length,
        __Radius.name() : __Radius
    })
    _AttributeMap = GeomObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'GeomCapsule', GeomCapsule)


# Complex type Body_ with content type ELEMENT_ONLY
class Body_ (RSObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Body')
    # Base type is RSObject
    
    # Element Torque uses Python identifier Torque
    __Torque = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Torque'), 'Torque', '__AbsentNamespace0_Body__Torque', False)

    
    Torque = property(__Torque.value, __Torque.set, None, None)

    
    # Element AngularVel uses Python identifier AngularVel
    __AngularVel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'AngularVel'), 'AngularVel', '__AbsentNamespace0_Body__AngularVel', False)

    
    AngularVel = property(__AngularVel.value, __AngularVel.set, None, None)

    
    # Element Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Position'), 'Position', '__AbsentNamespace0_Body__Position', False)

    
    Position = property(__Position.value, __Position.set, None, None)

    
    # Element Force uses Python identifier Force
    __Force = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Force'), 'Force', '__AbsentNamespace0_Body__Force', False)

    
    Force = property(__Force.value, __Force.set, None, None)

    
    # Element FiniteRotationAxis uses Python identifier FiniteRotationAxis
    __FiniteRotationAxis = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'FiniteRotationAxis'), 'FiniteRotationAxis', '__AbsentNamespace0_Body__FiniteRotationAxis', False)

    
    FiniteRotationAxis = property(__FiniteRotationAxis.value, __FiniteRotationAxis.set, None, None)

    
    # Element World uses Python identifier World
    __World = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'World'), 'World', '__AbsentNamespace0_Body__World', False)

    
    World = property(__World.value, __World.set, None, None)

    
    # Element Rotation uses Python identifier Rotation
    __Rotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Rotation'), 'Rotation', '__AbsentNamespace0_Body__Rotation', False)

    
    Rotation = property(__Rotation.value, __Rotation.set, None, None)

    
    # Element Space uses Python identifier Space
    __Space = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Space'), 'Space', '__AbsentNamespace0_Body__Space', False)

    
    Space = property(__Space.value, __Space.set, None, None)

    
    # Element Enabled uses Python identifier Enabled
    __Enabled = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Enabled'), 'Enabled', '__AbsentNamespace0_Body__Enabled', False)

    
    Enabled = property(__Enabled.value, __Enabled.set, None, None)

    
    # Element FiniteRotationMode uses Python identifier FiniteRotationMode
    __FiniteRotationMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'FiniteRotationMode'), 'FiniteRotationMode', '__AbsentNamespace0_Body__FiniteRotationMode', False)

    
    FiniteRotationMode = property(__FiniteRotationMode.value, __FiniteRotationMode.set, None, None)

    
    # Element GravityMode uses Python identifier GravityMode
    __GravityMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'GravityMode'), 'GravityMode', '__AbsentNamespace0_Body__GravityMode', False)

    
    GravityMode = property(__GravityMode.value, __GravityMode.set, None, None)

    
    # Element Name (Name) inherited from RSObject
    
    # Element LinearVel uses Python identifier LinearVel
    __LinearVel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'LinearVel'), 'LinearVel', '__AbsentNamespace0_Body__LinearVel', False)

    
    LinearVel = property(__LinearVel.value, __LinearVel.set, None, None)

    
    # Element Mass uses Python identifier Mass
    __Mass = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Mass'), 'Mass', '__AbsentNamespace0_Body__Mass', False)

    
    Mass = property(__Mass.value, __Mass.set, None, None)

    
    # Element Quaternion uses Python identifier Quaternion
    __Quaternion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Quaternion'), 'Quaternion', '__AbsentNamespace0_Body__Quaternion', False)

    
    Quaternion = property(__Quaternion.value, __Quaternion.set, None, None)


    _ElementMap = RSObject._ElementMap.copy()
    _ElementMap.update({
        __Torque.name() : __Torque,
        __AngularVel.name() : __AngularVel,
        __Position.name() : __Position,
        __Force.name() : __Force,
        __FiniteRotationAxis.name() : __FiniteRotationAxis,
        __World.name() : __World,
        __Rotation.name() : __Rotation,
        __Space.name() : __Space,
        __Enabled.name() : __Enabled,
        __FiniteRotationMode.name() : __FiniteRotationMode,
        __GravityMode.name() : __GravityMode,
        __LinearVel.name() : __LinearVel,
        __Mass.name() : __Mass,
        __Quaternion.name() : __Quaternion
    })
    _AttributeMap = RSObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Body', Body_)


# Complex type Vector with content type EMPTY
class Vector (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Vector')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Y uses Python identifier Y
    __Y = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Y'), 'Y', '__AbsentNamespace0_Vector_Y', pyxb.binding.datatypes.float)
    
    Y = property(__Y.value, __Y.set, None, None)

    
    # Attribute X uses Python identifier X
    __X = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'X'), 'X', '__AbsentNamespace0_Vector_X', pyxb.binding.datatypes.float)
    
    X = property(__X.value, __X.set, None, None)

    
    # Attribute Z uses Python identifier Z
    __Z = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Z'), 'Z', '__AbsentNamespace0_Vector_Z', pyxb.binding.datatypes.float)
    
    Z = property(__Z.value, __Z.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __Y.name() : __Y,
        __X.name() : __X,
        __Z.name() : __Z
    }
Namespace.addCategoryObject('typeBinding', u'Vector', Vector)


# Complex type GeomSphere with content type ELEMENT_ONLY
class GeomSphere (GeomObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GeomSphere')
    # Base type is GeomObject
    
    # Element Rotation (Rotation) inherited from GeomObject
    
    # Element CollideBits (CollideBits) inherited from GeomObject
    
    # Element Enable (Enable) inherited from GeomObject
    
    # Element Quaternion (Quaternion) inherited from GeomObject
    
    # Element Name (Name) inherited from RSObject
    
    # Element CategoryBits (CategoryBits) inherited from GeomObject
    
    # Element Position (Position) inherited from GeomObject
    
    # Element Radius uses Python identifier Radius
    __Radius = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Radius'), 'Radius', '__AbsentNamespace0_GeomSphere_Radius', False)

    
    Radius = property(__Radius.value, __Radius.set, None, None)


    _ElementMap = GeomObject._ElementMap.copy()
    _ElementMap.update({
        __Radius.name() : __Radius
    })
    _AttributeMap = GeomObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'GeomSphere', GeomSphere)


# Complex type GeomPlane with content type ELEMENT_ONLY
class GeomPlane (GeomObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GeomPlane')
    # Base type is GeomObject
    
    # Element Rotation (Rotation) inherited from GeomObject
    
    # Element CollideBits (CollideBits) inherited from GeomObject
    
    # Element Body uses Python identifier Body
    __Body = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Body'), 'Body', '__AbsentNamespace0_GeomPlane_Body', False)

    
    Body = property(__Body.value, __Body.set, None, None)

    
    # Element Enable (Enable) inherited from GeomObject
    
    # Element Enabled uses Python identifier Enabled
    __Enabled = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Enabled'), 'Enabled', '__AbsentNamespace0_GeomPlane_Enabled', False)

    
    Enabled = property(__Enabled.value, __Enabled.set, None, None)

    
    # Element Space uses Python identifier Space
    __Space = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Space'), 'Space', '__AbsentNamespace0_GeomPlane_Space', False)

    
    Space = property(__Space.value, __Space.set, None, None)

    
    # Element Name (Name) inherited from RSObject
    
    # Element CategoryBits (CategoryBits) inherited from GeomObject
    
    # Element Position (Position) inherited from GeomObject
    
    # Element Quaternion (Quaternion) inherited from GeomObject

    _ElementMap = GeomObject._ElementMap.copy()
    _ElementMap.update({
        __Body.name() : __Body,
        __Enabled.name() : __Enabled,
        __Space.name() : __Space
    })
    _AttributeMap = GeomObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'GeomPlane', GeomPlane)


# Complex type Rotation with content type ELEMENT_ONLY
class Rotation (RSObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Rotation')
    # Base type is RSObject
    
    # Element Column3 uses Python identifier Column3
    __Column3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Column3'), 'Column3', '__AbsentNamespace0_Rotation_Column3', False)

    
    Column3 = property(__Column3.value, __Column3.set, None, None)

    
    # Element Column1 uses Python identifier Column1
    __Column1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Column1'), 'Column1', '__AbsentNamespace0_Rotation_Column1', False)

    
    Column1 = property(__Column1.value, __Column1.set, None, None)

    
    # Element Name (Name) inherited from RSObject
    
    # Element Column2 uses Python identifier Column2
    __Column2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Column2'), 'Column2', '__AbsentNamespace0_Rotation_Column2', False)

    
    Column2 = property(__Column2.value, __Column2.set, None, None)


    _ElementMap = RSObject._ElementMap.copy()
    _ElementMap.update({
        __Column3.name() : __Column3,
        __Column1.name() : __Column1,
        __Column2.name() : __Column2
    })
    _AttributeMap = RSObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Rotation', Rotation)


# Complex type Mass with content type ELEMENT_ONLY
class Mass (RSObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Mass')
    # Base type is RSObject
    
    # Element Name (Name) inherited from RSObject

    _ElementMap = RSObject._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = RSObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Mass', Mass)


# Complex type BoxTotalMass with content type ELEMENT_ONLY
class BoxTotalMass (Mass):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BoxTotalMass')
    # Base type is Mass
    
    # Element LZ uses Python identifier LZ
    __LZ = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'LZ'), 'LZ', '__AbsentNamespace0_BoxTotalMass_LZ', False)

    
    LZ = property(__LZ.value, __LZ.set, None, None)

    
    # Element TotalMass uses Python identifier TotalMass
    __TotalMass = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'TotalMass'), 'TotalMass', '__AbsentNamespace0_BoxTotalMass_TotalMass', False)

    
    TotalMass = property(__TotalMass.value, __TotalMass.set, None, None)

    
    # Element LY uses Python identifier LY
    __LY = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'LY'), 'LY', '__AbsentNamespace0_BoxTotalMass_LY', False)

    
    LY = property(__LY.value, __LY.set, None, None)

    
    # Element LX uses Python identifier LX
    __LX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'LX'), 'LX', '__AbsentNamespace0_BoxTotalMass_LX', False)

    
    LX = property(__LX.value, __LX.set, None, None)

    
    # Element Name (Name) inherited from RSObject

    _ElementMap = Mass._ElementMap.copy()
    _ElementMap.update({
        __LZ.name() : __LZ,
        __TotalMass.name() : __TotalMass,
        __LY.name() : __LY,
        __LX.name() : __LX
    })
    _AttributeMap = Mass._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'BoxTotalMass', BoxTotalMass)


# Complex type Sim_ with content type ELEMENT_ONLY
class Sim_ (RSObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Sim')
    # Base type is RSObject
    
    # Element Geom uses Python identifier Geom
    __Geom = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Geom'), 'Geom', '__AbsentNamespace0_Sim__Geom', True)

    
    Geom = property(__Geom.value, __Geom.set, None, None)

    
    # Element World uses Python identifier World
    __World = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'World'), 'World', '__AbsentNamespace0_Sim__World', True)

    
    World = property(__World.value, __World.set, None, None)

    
    # Element Name (Name) inherited from RSObject
    
    # Element Space uses Python identifier Space
    __Space = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Space'), 'Space', '__AbsentNamespace0_Sim__Space', True)

    
    Space = property(__Space.value, __Space.set, None, None)

    
    # Element Body uses Python identifier Body
    __Body = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Body'), 'Body', '__AbsentNamespace0_Sim__Body', True)

    
    Body = property(__Body.value, __Body.set, None, None)


    _ElementMap = RSObject._ElementMap.copy()
    _ElementMap.update({
        __Geom.name() : __Geom,
        __World.name() : __World,
        __Space.name() : __Space,
        __Body.name() : __Body
    })
    _AttributeMap = RSObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Sim', Sim_)


# Complex type World_ with content type ELEMENT_ONLY
class World_ (RSObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'World')
    # Base type is RSObject
    
    # Element AutoDisableSteps uses Python identifier AutoDisableSteps
    __AutoDisableSteps = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'AutoDisableSteps'), 'AutoDisableSteps', '__AbsentNamespace0_World__AutoDisableSteps', False)

    
    AutoDisableSteps = property(__AutoDisableSteps.value, __AutoDisableSteps.set, None, None)

    
    # Element AutoDisableAngularThreshold uses Python identifier AutoDisableAngularThreshold
    __AutoDisableAngularThreshold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'AutoDisableAngularThreshold'), 'AutoDisableAngularThreshold', '__AbsentNamespace0_World__AutoDisableAngularThreshold', False)

    
    AutoDisableAngularThreshold = property(__AutoDisableAngularThreshold.value, __AutoDisableAngularThreshold.set, None, None)

    
    # Element AutoDisableTime uses Python identifier AutoDisableTime
    __AutoDisableTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'AutoDisableTime'), 'AutoDisableTime', '__AbsentNamespace0_World__AutoDisableTime', False)

    
    AutoDisableTime = property(__AutoDisableTime.value, __AutoDisableTime.set, None, None)

    
    # Element CFM uses Python identifier CFM
    __CFM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'CFM'), 'CFM', '__AbsentNamespace0_World__CFM', False)

    
    CFM = property(__CFM.value, __CFM.set, None, None)

    
    # Element AutoDisableFlag uses Python identifier AutoDisableFlag
    __AutoDisableFlag = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'AutoDisableFlag'), 'AutoDisableFlag', '__AbsentNamespace0_World__AutoDisableFlag', False)

    
    AutoDisableFlag = property(__AutoDisableFlag.value, __AutoDisableFlag.set, None, None)

    
    # Element ContactMaxCorrectingVel uses Python identifier ContactMaxCorrectingVel
    __ContactMaxCorrectingVel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ContactMaxCorrectingVel'), 'ContactMaxCorrectingVel', '__AbsentNamespace0_World__ContactMaxCorrectingVel', False)

    
    ContactMaxCorrectingVel = property(__ContactMaxCorrectingVel.value, __ContactMaxCorrectingVel.set, None, None)

    
    # Element ContactSurfaceLayer uses Python identifier ContactSurfaceLayer
    __ContactSurfaceLayer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ContactSurfaceLayer'), 'ContactSurfaceLayer', '__AbsentNamespace0_World__ContactSurfaceLayer', False)

    
    ContactSurfaceLayer = property(__ContactSurfaceLayer.value, __ContactSurfaceLayer.set, None, None)

    
    # Element Body uses Python identifier Body
    __Body = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Body'), 'Body', '__AbsentNamespace0_World__Body', True)

    
    Body = property(__Body.value, __Body.set, None, None)

    
    # Element Name (Name) inherited from RSObject
    
    # Element ERP uses Python identifier ERP
    __ERP = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ERP'), 'ERP', '__AbsentNamespace0_World__ERP', False)

    
    ERP = property(__ERP.value, __ERP.set, None, None)

    
    # Element Gravity uses Python identifier Gravity
    __Gravity = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Gravity'), 'Gravity', '__AbsentNamespace0_World__Gravity', False)

    
    Gravity = property(__Gravity.value, __Gravity.set, None, None)

    
    # Element QuickStepNumIterations uses Python identifier QuickStepNumIterations
    __QuickStepNumIterations = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'QuickStepNumIterations'), 'QuickStepNumIterations', '__AbsentNamespace0_World__QuickStepNumIterations', False)

    
    QuickStepNumIterations = property(__QuickStepNumIterations.value, __QuickStepNumIterations.set, None, None)


    _ElementMap = RSObject._ElementMap.copy()
    _ElementMap.update({
        __AutoDisableSteps.name() : __AutoDisableSteps,
        __AutoDisableAngularThreshold.name() : __AutoDisableAngularThreshold,
        __AutoDisableTime.name() : __AutoDisableTime,
        __CFM.name() : __CFM,
        __AutoDisableFlag.name() : __AutoDisableFlag,
        __ContactMaxCorrectingVel.name() : __ContactMaxCorrectingVel,
        __ContactSurfaceLayer.name() : __ContactSurfaceLayer,
        __Body.name() : __Body,
        __ERP.name() : __ERP,
        __Gravity.name() : __Gravity,
        __QuickStepNumIterations.name() : __QuickStepNumIterations
    })
    _AttributeMap = RSObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'World', World_)


# Complex type Foo with content type ELEMENT_ONLY
class Foo (RSObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Foo')
    # Base type is RSObject
    
    # Element Name (Name) inherited from RSObject

    _ElementMap = RSObject._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = RSObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Foo', Foo)


# Complex type GeomBox with content type ELEMENT_ONLY
class GeomBox (GeomObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GeomBox')
    # Base type is GeomObject
    
    # Element Rotation (Rotation) inherited from GeomObject
    
    # Element Enable (Enable) inherited from GeomObject
    
    # Element CollideBits (CollideBits) inherited from GeomObject
    
    # Element Name (Name) inherited from RSObject
    
    # Element CategoryBits (CategoryBits) inherited from GeomObject
    
    # Element Lengths uses Python identifier Lengths
    __Lengths = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Lengths'), 'Lengths', '__AbsentNamespace0_GeomBox_Lengths', False)

    
    Lengths = property(__Lengths.value, __Lengths.set, None, None)

    
    # Element Position (Position) inherited from GeomObject
    
    # Element Quaternion (Quaternion) inherited from GeomObject

    _ElementMap = GeomObject._ElementMap.copy()
    _ElementMap.update({
        __Lengths.name() : __Lengths
    })
    _AttributeMap = GeomObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'GeomBox', GeomBox)


# Complex type Joint with content type ELEMENT_ONLY
class Joint (RSObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Joint')
    # Base type is RSObject
    
    # Element Body2 uses Python identifier Body2
    __Body2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Body2'), 'Body2', '__AbsentNamespace0_Joint_Body2', False)

    
    Body2 = property(__Body2.value, __Body2.set, None, None)

    
    # Element Feedback uses Python identifier Feedback
    __Feedback = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Feedback'), 'Feedback', '__AbsentNamespace0_Joint_Feedback', False)

    
    Feedback = property(__Feedback.value, __Feedback.set, None, None)

    
    # Element Name (Name) inherited from RSObject
    
    # Element Body1 uses Python identifier Body1
    __Body1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Body1'), 'Body1', '__AbsentNamespace0_Joint_Body1', False)

    
    Body1 = property(__Body1.value, __Body1.set, None, None)


    _ElementMap = RSObject._ElementMap.copy()
    _ElementMap.update({
        __Body2.name() : __Body2,
        __Feedback.name() : __Feedback,
        __Body1.name() : __Body1
    })
    _AttributeMap = RSObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Joint', Joint)


# Complex type HingeJoint with content type ELEMENT_ONLY
class HingeJoint (Joint):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HingeJoint')
    # Base type is Joint
    
    # Element Axis uses Python identifier Axis
    __Axis = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Axis'), 'Axis', '__AbsentNamespace0_HingeJoint_Axis', False)

    
    Axis = property(__Axis.value, __Axis.set, None, None)

    
    # Element Anchor uses Python identifier Anchor
    __Anchor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Anchor'), 'Anchor', '__AbsentNamespace0_HingeJoint_Anchor', False)

    
    Anchor = property(__Anchor.value, __Anchor.set, None, None)

    
    # Element Torque uses Python identifier Torque
    __Torque = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Torque'), 'Torque', '__AbsentNamespace0_HingeJoint_Torque', False)

    
    Torque = property(__Torque.value, __Torque.set, None, None)

    
    # Element Feedback (Feedback) inherited from Joint
    
    # Element Name (Name) inherited from RSObject
    
    # Element Body1 (Body1) inherited from Joint
    
    # Element Body2 (Body2) inherited from Joint

    _ElementMap = Joint._ElementMap.copy()
    _ElementMap.update({
        __Axis.name() : __Axis,
        __Anchor.name() : __Anchor,
        __Torque.name() : __Torque
    })
    _AttributeMap = Joint._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'HingeJoint', HingeJoint)


# Complex type Quaternion with content type EMPTY
class Quaternion (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Quaternion')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute I uses Python identifier I
    __I = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'I'), 'I', '__AbsentNamespace0_Quaternion_I', pyxb.binding.datatypes.float)
    
    I = property(__I.value, __I.set, None, None)

    
    # Attribute K uses Python identifier K
    __K = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'K'), 'K', '__AbsentNamespace0_Quaternion_K', pyxb.binding.datatypes.float)
    
    K = property(__K.value, __K.set, None, None)

    
    # Attribute W uses Python identifier W
    __W = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'W'), 'W', '__AbsentNamespace0_Quaternion_W', pyxb.binding.datatypes.float)
    
    W = property(__W.value, __W.set, None, None)

    
    # Attribute J uses Python identifier J
    __J = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'J'), 'J', '__AbsentNamespace0_Quaternion_J', pyxb.binding.datatypes.float)
    
    J = property(__J.value, __J.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __I.name() : __I,
        __K.name() : __K,
        __W.name() : __W,
        __J.name() : __J
    }
Namespace.addCategoryObject('typeBinding', u'Quaternion', Quaternion)


# Complex type SimpleSpace with content type ELEMENT_ONLY
class SimpleSpace (SpaceBase):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SimpleSpace')
    # Base type is SpaceBase
    
    # Element Rotation (Rotation) inherited from GeomObject
    
    # Element CollideBits (CollideBits) inherited from GeomObject
    
    # Element Geom (Geom) inherited from SpaceBase
    
    # Element Quaternion (Quaternion) inherited from GeomObject
    
    # Element Name (Name) inherited from RSObject
    
    # Element CategoryBits (CategoryBits) inherited from GeomObject
    
    # Element Position (Position) inherited from GeomObject
    
    # Element Enable (Enable) inherited from GeomObject

    _ElementMap = SpaceBase._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = SpaceBase._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SimpleSpace', SimpleSpace)


# Complex type GeomCylinder with content type ELEMENT_ONLY
class GeomCylinder (GeomObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GeomCylinder')
    # Base type is GeomObject
    
    # Element Rotation (Rotation) inherited from GeomObject
    
    # Element Length uses Python identifier Length
    __Length = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Length'), 'Length', '__AbsentNamespace0_GeomCylinder_Length', False)

    
    Length = property(__Length.value, __Length.set, None, None)

    
    # Element Radius uses Python identifier Radius
    __Radius = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Radius'), 'Radius', '__AbsentNamespace0_GeomCylinder_Radius', False)

    
    Radius = property(__Radius.value, __Radius.set, None, None)

    
    # Element Enable (Enable) inherited from GeomObject
    
    # Element Quaternion (Quaternion) inherited from GeomObject
    
    # Element Name (Name) inherited from RSObject
    
    # Element CategoryBits (CategoryBits) inherited from GeomObject
    
    # Element CollideBits (CollideBits) inherited from GeomObject
    
    # Element Position (Position) inherited from GeomObject

    _ElementMap = GeomObject._ElementMap.copy()
    _ElementMap.update({
        __Length.name() : __Length,
        __Radius.name() : __Radius
    })
    _AttributeMap = GeomObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'GeomCylinder', GeomCylinder)


Body = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Body'), Body_)
Namespace.addCategoryObject('elementBinding', Body.name().localName(), Body)

Sim = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Sim'), Sim_)
Namespace.addCategoryObject('elementBinding', Sim.name().localName(), Sim)

World = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'World'), World_)
Namespace.addCategoryObject('elementBinding', World.name().localName(), World)



RSObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=RSObject))
RSObject._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(RSObject._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
RSObject._ContentModel = pyxb.binding.content.ParticleModel(RSObject._GroupModel, min_occurs=1, max_occurs=1)



GeomObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Enable'), pyxb.binding.datatypes.boolean, scope=GeomObject))

GeomObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CollideBits'), pyxb.binding.datatypes.nonNegativeInteger, scope=GeomObject))

GeomObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Rotation'), Rotation, scope=GeomObject))

GeomObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CategoryBits'), pyxb.binding.datatypes.nonNegativeInteger, scope=GeomObject))

GeomObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Position'), Vector, scope=GeomObject))

GeomObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Quaternion'), Quaternion, scope=GeomObject))
GeomObject._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomObject._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
GeomObject._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomObject._UseForTag(pyxb.namespace.ExpandedName(None, u'Enable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomObject._UseForTag(pyxb.namespace.ExpandedName(None, u'CategoryBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomObject._UseForTag(pyxb.namespace.ExpandedName(None, u'CollideBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomObject._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomObject._UseForTag(pyxb.namespace.ExpandedName(None, u'Quaternion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomObject._UseForTag(pyxb.namespace.ExpandedName(None, u'Rotation')), min_occurs=0L, max_occurs=1)
    )
GeomObject._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomObject._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomObject._GroupModel_2, min_occurs=1, max_occurs=1)
    )
GeomObject._ContentModel = pyxb.binding.content.ParticleModel(GeomObject._GroupModel, min_occurs=1, max_occurs=1)



SpaceBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Geom'), GeomObject, scope=SpaceBase))
SpaceBase._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SpaceBase._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
SpaceBase._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SpaceBase._UseForTag(pyxb.namespace.ExpandedName(None, u'Enable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SpaceBase._UseForTag(pyxb.namespace.ExpandedName(None, u'CategoryBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SpaceBase._UseForTag(pyxb.namespace.ExpandedName(None, u'CollideBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SpaceBase._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SpaceBase._UseForTag(pyxb.namespace.ExpandedName(None, u'Quaternion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SpaceBase._UseForTag(pyxb.namespace.ExpandedName(None, u'Rotation')), min_occurs=0L, max_occurs=1)
    )
SpaceBase._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SpaceBase._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SpaceBase._GroupModel_3, min_occurs=1, max_occurs=1)
    )
SpaceBase._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SpaceBase._UseForTag(pyxb.namespace.ExpandedName(None, u'Geom')), min_occurs=0L, max_occurs=None)
    )
SpaceBase._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SpaceBase._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SpaceBase._GroupModel_4, min_occurs=1, max_occurs=1)
    )
SpaceBase._ContentModel = pyxb.binding.content.ParticleModel(SpaceBase._GroupModel, min_occurs=1, max_occurs=1)



GeomCapsule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Length'), pyxb.binding.datatypes.float, scope=GeomCapsule))

GeomCapsule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Radius'), pyxb.binding.datatypes.float, scope=GeomCapsule))
GeomCapsule._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCapsule._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
GeomCapsule._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCapsule._UseForTag(pyxb.namespace.ExpandedName(None, u'Enable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCapsule._UseForTag(pyxb.namespace.ExpandedName(None, u'CategoryBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCapsule._UseForTag(pyxb.namespace.ExpandedName(None, u'CollideBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCapsule._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCapsule._UseForTag(pyxb.namespace.ExpandedName(None, u'Quaternion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCapsule._UseForTag(pyxb.namespace.ExpandedName(None, u'Rotation')), min_occurs=0L, max_occurs=1)
    )
GeomCapsule._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCapsule._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCapsule._GroupModel_3, min_occurs=1, max_occurs=1)
    )
GeomCapsule._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCapsule._UseForTag(pyxb.namespace.ExpandedName(None, u'Length')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCapsule._UseForTag(pyxb.namespace.ExpandedName(None, u'Radius')), min_occurs=0L, max_occurs=1)
    )
GeomCapsule._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCapsule._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCapsule._GroupModel_4, min_occurs=1, max_occurs=1)
    )
GeomCapsule._ContentModel = pyxb.binding.content.ParticleModel(GeomCapsule._GroupModel, min_occurs=1, max_occurs=1)



Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Torque'), Vector, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AngularVel'), Vector, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Position'), Vector, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Force'), Vector, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'FiniteRotationAxis'), Vector, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'World'), pyxb.binding.datatypes.string, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Rotation'), Rotation, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Space'), pyxb.binding.datatypes.string, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Enabled'), pyxb.binding.datatypes.boolean, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'FiniteRotationMode'), pyxb.binding.datatypes.nonNegativeInteger, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'GravityMode'), pyxb.binding.datatypes.boolean, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'LinearVel'), Vector, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Mass'), Mass, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Quaternion'), Quaternion, scope=Body_))
Body_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Body_._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
Body_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Body_._UseForTag(pyxb.namespace.ExpandedName(None, u'Space')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Body_._UseForTag(pyxb.namespace.ExpandedName(None, u'World')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Body_._UseForTag(pyxb.namespace.ExpandedName(None, u'Enabled')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Body_._UseForTag(pyxb.namespace.ExpandedName(None, u'AngularVel')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Body_._UseForTag(pyxb.namespace.ExpandedName(None, u'FiniteRotationAxis')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Body_._UseForTag(pyxb.namespace.ExpandedName(None, u'FiniteRotationMode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Body_._UseForTag(pyxb.namespace.ExpandedName(None, u'Force')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Body_._UseForTag(pyxb.namespace.ExpandedName(None, u'GravityMode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Body_._UseForTag(pyxb.namespace.ExpandedName(None, u'LinearVel')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Body_._UseForTag(pyxb.namespace.ExpandedName(None, u'Mass')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Body_._UseForTag(pyxb.namespace.ExpandedName(None, u'Torque')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Body_._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Body_._UseForTag(pyxb.namespace.ExpandedName(None, u'Quaternion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Body_._UseForTag(pyxb.namespace.ExpandedName(None, u'Rotation')), min_occurs=0L, max_occurs=1)
    )
Body_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Body_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Body_._GroupModel_2, min_occurs=1, max_occurs=1)
    )
Body_._ContentModel = pyxb.binding.content.ParticleModel(Body_._GroupModel, min_occurs=1, max_occurs=1)



GeomSphere._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Radius'), pyxb.binding.datatypes.float, scope=GeomSphere))
GeomSphere._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomSphere._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
GeomSphere._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomSphere._UseForTag(pyxb.namespace.ExpandedName(None, u'Enable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomSphere._UseForTag(pyxb.namespace.ExpandedName(None, u'CategoryBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomSphere._UseForTag(pyxb.namespace.ExpandedName(None, u'CollideBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomSphere._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomSphere._UseForTag(pyxb.namespace.ExpandedName(None, u'Quaternion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomSphere._UseForTag(pyxb.namespace.ExpandedName(None, u'Rotation')), min_occurs=0L, max_occurs=1)
    )
GeomSphere._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomSphere._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomSphere._GroupModel_3, min_occurs=1, max_occurs=1)
    )
GeomSphere._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomSphere._UseForTag(pyxb.namespace.ExpandedName(None, u'Radius')), min_occurs=0L, max_occurs=1)
    )
GeomSphere._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomSphere._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomSphere._GroupModel_4, min_occurs=1, max_occurs=1)
    )
GeomSphere._ContentModel = pyxb.binding.content.ParticleModel(GeomSphere._GroupModel, min_occurs=1, max_occurs=1)



GeomPlane._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Body'), pyxb.binding.datatypes.string, scope=GeomPlane))

GeomPlane._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Enabled'), pyxb.binding.datatypes.boolean, scope=GeomPlane))

GeomPlane._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Space'), pyxb.binding.datatypes.string, scope=GeomPlane))
GeomPlane._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomPlane._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
GeomPlane._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomPlane._UseForTag(pyxb.namespace.ExpandedName(None, u'Enable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane._UseForTag(pyxb.namespace.ExpandedName(None, u'CategoryBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane._UseForTag(pyxb.namespace.ExpandedName(None, u'CollideBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane._UseForTag(pyxb.namespace.ExpandedName(None, u'Quaternion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane._UseForTag(pyxb.namespace.ExpandedName(None, u'Rotation')), min_occurs=0L, max_occurs=1)
    )
GeomPlane._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomPlane._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane._GroupModel_3, min_occurs=1, max_occurs=1)
    )
GeomPlane._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomPlane._UseForTag(pyxb.namespace.ExpandedName(None, u'Space')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane._UseForTag(pyxb.namespace.ExpandedName(None, u'Body')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane._UseForTag(pyxb.namespace.ExpandedName(None, u'Enabled')), min_occurs=0L, max_occurs=1)
    )
GeomPlane._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomPlane._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane._GroupModel_4, min_occurs=1, max_occurs=1)
    )
GeomPlane._ContentModel = pyxb.binding.content.ParticleModel(GeomPlane._GroupModel, min_occurs=1, max_occurs=1)



Rotation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Column3'), Vector, scope=Rotation))

Rotation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Column1'), Vector, scope=Rotation))

Rotation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Column2'), Vector, scope=Rotation))
Rotation._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Rotation._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
Rotation._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Rotation._UseForTag(pyxb.namespace.ExpandedName(None, u'Column1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Rotation._UseForTag(pyxb.namespace.ExpandedName(None, u'Column2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Rotation._UseForTag(pyxb.namespace.ExpandedName(None, u'Column3')), min_occurs=1, max_occurs=1)
    )
Rotation._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Rotation._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Rotation._GroupModel_2, min_occurs=1, max_occurs=1)
    )
Rotation._ContentModel = pyxb.binding.content.ParticleModel(Rotation._GroupModel, min_occurs=1, max_occurs=1)


Mass._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Mass._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
Mass._ContentModel = pyxb.binding.content.ParticleModel(Mass._GroupModel, min_occurs=1, max_occurs=1)



BoxTotalMass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'LZ'), pyxb.binding.datatypes.float, scope=BoxTotalMass))

BoxTotalMass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TotalMass'), pyxb.binding.datatypes.float, scope=BoxTotalMass))

BoxTotalMass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'LY'), pyxb.binding.datatypes.float, scope=BoxTotalMass))

BoxTotalMass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'LX'), pyxb.binding.datatypes.float, scope=BoxTotalMass))
BoxTotalMass._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(BoxTotalMass._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
BoxTotalMass._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(BoxTotalMass._UseForTag(pyxb.namespace.ExpandedName(None, u'TotalMass')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(BoxTotalMass._UseForTag(pyxb.namespace.ExpandedName(None, u'LX')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(BoxTotalMass._UseForTag(pyxb.namespace.ExpandedName(None, u'LY')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(BoxTotalMass._UseForTag(pyxb.namespace.ExpandedName(None, u'LZ')), min_occurs=1, max_occurs=1)
    )
BoxTotalMass._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(BoxTotalMass._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(BoxTotalMass._GroupModel_2, min_occurs=1, max_occurs=1)
    )
BoxTotalMass._ContentModel = pyxb.binding.content.ParticleModel(BoxTotalMass._GroupModel, min_occurs=1, max_occurs=1)



Sim_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Geom'), GeomObject, scope=Sim_))

Sim_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'World'), World_, scope=Sim_))

Sim_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Space'), SpaceBase, scope=Sim_))

Sim_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Body'), Body_, scope=Sim_))
Sim_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Sim_._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
Sim_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Sim_._UseForTag(pyxb.namespace.ExpandedName(None, u'World')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Sim_._UseForTag(pyxb.namespace.ExpandedName(None, u'Space')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Sim_._UseForTag(pyxb.namespace.ExpandedName(None, u'Body')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Sim_._UseForTag(pyxb.namespace.ExpandedName(None, u'Geom')), min_occurs=0L, max_occurs=None)
    )
Sim_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Sim_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Sim_._GroupModel_2, min_occurs=1, max_occurs=1)
    )
Sim_._ContentModel = pyxb.binding.content.ParticleModel(Sim_._GroupModel, min_occurs=1, max_occurs=1)



World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AutoDisableSteps'), pyxb.binding.datatypes.boolean, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AutoDisableAngularThreshold'), pyxb.binding.datatypes.float, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AutoDisableTime'), pyxb.binding.datatypes.boolean, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CFM'), pyxb.binding.datatypes.float, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AutoDisableFlag'), pyxb.binding.datatypes.boolean, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ContactMaxCorrectingVel'), pyxb.binding.datatypes.float, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ContactSurfaceLayer'), pyxb.binding.datatypes.float, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Body'), Body_, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ERP'), pyxb.binding.datatypes.float, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Gravity'), Vector, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'QuickStepNumIterations'), pyxb.binding.datatypes.nonNegativeInteger, scope=World_))
World_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(World_._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
World_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(World_._UseForTag(pyxb.namespace.ExpandedName(None, u'AutoDisableAngularThreshold')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(World_._UseForTag(pyxb.namespace.ExpandedName(None, u'AutoDisableFlag')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(World_._UseForTag(pyxb.namespace.ExpandedName(None, u'AutoDisableSteps')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(World_._UseForTag(pyxb.namespace.ExpandedName(None, u'AutoDisableTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(World_._UseForTag(pyxb.namespace.ExpandedName(None, u'CFM')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(World_._UseForTag(pyxb.namespace.ExpandedName(None, u'ContactMaxCorrectingVel')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(World_._UseForTag(pyxb.namespace.ExpandedName(None, u'ContactSurfaceLayer')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(World_._UseForTag(pyxb.namespace.ExpandedName(None, u'ERP')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(World_._UseForTag(pyxb.namespace.ExpandedName(None, u'Gravity')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(World_._UseForTag(pyxb.namespace.ExpandedName(None, u'QuickStepNumIterations')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(World_._UseForTag(pyxb.namespace.ExpandedName(None, u'Body')), min_occurs=0L, max_occurs=None)
    )
World_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(World_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(World_._GroupModel_2, min_occurs=1, max_occurs=1)
    )
World_._ContentModel = pyxb.binding.content.ParticleModel(World_._GroupModel, min_occurs=1, max_occurs=1)


Foo._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Foo._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
Foo._ContentModel = pyxb.binding.content.ParticleModel(Foo._GroupModel, min_occurs=1, max_occurs=1)



GeomBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Lengths'), Vector, scope=GeomBox))
GeomBox._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomBox._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
GeomBox._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomBox._UseForTag(pyxb.namespace.ExpandedName(None, u'Enable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomBox._UseForTag(pyxb.namespace.ExpandedName(None, u'CategoryBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomBox._UseForTag(pyxb.namespace.ExpandedName(None, u'CollideBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomBox._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomBox._UseForTag(pyxb.namespace.ExpandedName(None, u'Quaternion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomBox._UseForTag(pyxb.namespace.ExpandedName(None, u'Rotation')), min_occurs=0L, max_occurs=1)
    )
GeomBox._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomBox._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomBox._GroupModel_3, min_occurs=1, max_occurs=1)
    )
GeomBox._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomBox._UseForTag(pyxb.namespace.ExpandedName(None, u'Lengths')), min_occurs=0L, max_occurs=1)
    )
GeomBox._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomBox._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomBox._GroupModel_4, min_occurs=1, max_occurs=1)
    )
GeomBox._ContentModel = pyxb.binding.content.ParticleModel(GeomBox._GroupModel, min_occurs=1, max_occurs=1)



Joint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Body2'), pyxb.binding.datatypes.string, scope=Joint))

Joint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Feedback'), pyxb.binding.datatypes.boolean, scope=Joint))

Joint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Body1'), pyxb.binding.datatypes.string, scope=Joint))
Joint._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Joint._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
Joint._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Joint._UseForTag(pyxb.namespace.ExpandedName(None, u'Feedback')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Joint._UseForTag(pyxb.namespace.ExpandedName(None, u'Body1')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Joint._UseForTag(pyxb.namespace.ExpandedName(None, u'Body2')), min_occurs=0L, max_occurs=1)
    )
Joint._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Joint._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Joint._GroupModel_2, min_occurs=1, max_occurs=1)
    )
Joint._ContentModel = pyxb.binding.content.ParticleModel(Joint._GroupModel, min_occurs=1, max_occurs=1)



HingeJoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Axis'), Vector, scope=HingeJoint))

HingeJoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Anchor'), Vector, scope=HingeJoint))

HingeJoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Torque'), pyxb.binding.datatypes.float, scope=HingeJoint))
HingeJoint._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(HingeJoint._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
HingeJoint._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(HingeJoint._UseForTag(pyxb.namespace.ExpandedName(None, u'Feedback')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint._UseForTag(pyxb.namespace.ExpandedName(None, u'Body1')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint._UseForTag(pyxb.namespace.ExpandedName(None, u'Body2')), min_occurs=0L, max_occurs=1)
    )
HingeJoint._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(HingeJoint._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint._GroupModel_3, min_occurs=1, max_occurs=1)
    )
HingeJoint._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(HingeJoint._UseForTag(pyxb.namespace.ExpandedName(None, u'Anchor')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint._UseForTag(pyxb.namespace.ExpandedName(None, u'Axis')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint._UseForTag(pyxb.namespace.ExpandedName(None, u'Torque')), min_occurs=0L, max_occurs=1)
    )
HingeJoint._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(HingeJoint._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint._GroupModel_4, min_occurs=1, max_occurs=1)
    )
HingeJoint._ContentModel = pyxb.binding.content.ParticleModel(HingeJoint._GroupModel, min_occurs=1, max_occurs=1)


SimpleSpace._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SimpleSpace._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
SimpleSpace._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SimpleSpace._UseForTag(pyxb.namespace.ExpandedName(None, u'Enable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SimpleSpace._UseForTag(pyxb.namespace.ExpandedName(None, u'CategoryBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SimpleSpace._UseForTag(pyxb.namespace.ExpandedName(None, u'CollideBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SimpleSpace._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SimpleSpace._UseForTag(pyxb.namespace.ExpandedName(None, u'Quaternion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SimpleSpace._UseForTag(pyxb.namespace.ExpandedName(None, u'Rotation')), min_occurs=0L, max_occurs=1)
    )
SimpleSpace._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SimpleSpace._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SimpleSpace._GroupModel_3, min_occurs=1, max_occurs=1)
    )
SimpleSpace._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SimpleSpace._UseForTag(pyxb.namespace.ExpandedName(None, u'Geom')), min_occurs=0L, max_occurs=None)
    )
SimpleSpace._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SimpleSpace._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SimpleSpace._GroupModel_4, min_occurs=1, max_occurs=1)
    )
SimpleSpace._ContentModel = pyxb.binding.content.ParticleModel(SimpleSpace._GroupModel, min_occurs=1, max_occurs=1)



GeomCylinder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Length'), pyxb.binding.datatypes.float, scope=GeomCylinder))

GeomCylinder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Radius'), pyxb.binding.datatypes.float, scope=GeomCylinder))
GeomCylinder._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCylinder._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
GeomCylinder._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCylinder._UseForTag(pyxb.namespace.ExpandedName(None, u'Enable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCylinder._UseForTag(pyxb.namespace.ExpandedName(None, u'CategoryBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCylinder._UseForTag(pyxb.namespace.ExpandedName(None, u'CollideBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCylinder._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCylinder._UseForTag(pyxb.namespace.ExpandedName(None, u'Quaternion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCylinder._UseForTag(pyxb.namespace.ExpandedName(None, u'Rotation')), min_occurs=0L, max_occurs=1)
    )
GeomCylinder._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCylinder._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCylinder._GroupModel_3, min_occurs=1, max_occurs=1)
    )
GeomCylinder._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCylinder._UseForTag(pyxb.namespace.ExpandedName(None, u'Length')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCylinder._UseForTag(pyxb.namespace.ExpandedName(None, u'Radius')), min_occurs=0L, max_occurs=1)
    )
GeomCylinder._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCylinder._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCylinder._GroupModel_4, min_occurs=1, max_occurs=1)
    )
GeomCylinder._ContentModel = pyxb.binding.content.ParticleModel(GeomCylinder._GroupModel, min_occurs=1, max_occurs=1)
