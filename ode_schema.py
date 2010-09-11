# ./ode_schema.py
# PyXB bindings for NamespaceModule
# NSM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2010-09-11 14:37:37.674873 by PyXB version 1.1.2
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:5bfabc48-bda1-11df-a679-00e04da8a2a1')

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


# Complex type GeomObject with content type ELEMENT_ONLY
class GeomObject (RSObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GeomObject')
    # Base type is RSObject
    
    # Element CategoryBits uses Python identifier CategoryBits
    __CategoryBits = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'CategoryBits'), 'CategoryBits', '__AbsentNamespace0_GeomObject_CategoryBits', False)

    
    CategoryBits = property(__CategoryBits.value, __CategoryBits.set, None, None)

    
    # Element Name (Name) inherited from RSObject
    
    # Element CollideBits uses Python identifier CollideBits
    __CollideBits = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'CollideBits'), 'CollideBits', '__AbsentNamespace0_GeomObject_CollideBits', False)

    
    CollideBits = property(__CollideBits.value, __CollideBits.set, None, None)

    
    # Element Enable uses Python identifier Enable
    __Enable = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Enable'), 'Enable', '__AbsentNamespace0_GeomObject_Enable', False)

    
    Enable = property(__Enable.value, __Enable.set, None, None)

    
    # Element Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Position'), 'Position', '__AbsentNamespace0_GeomObject_Position', False)

    
    Position = property(__Position.value, __Position.set, None, None)

    
    # Element Quaternion uses Python identifier Quaternion
    __Quaternion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Quaternion'), 'Quaternion', '__AbsentNamespace0_GeomObject_Quaternion', False)

    
    Quaternion = property(__Quaternion.value, __Quaternion.set, None, None)

    
    # Element Rotation uses Python identifier Rotation
    __Rotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Rotation'), 'Rotation', '__AbsentNamespace0_GeomObject_Rotation', False)

    
    Rotation = property(__Rotation.value, __Rotation.set, None, None)


    _ElementMap = RSObject._ElementMap.copy()
    _ElementMap.update({
        __CategoryBits.name() : __CategoryBits,
        __CollideBits.name() : __CollideBits,
        __Enable.name() : __Enable,
        __Position.name() : __Position,
        __Quaternion.name() : __Quaternion,
        __Rotation.name() : __Rotation
    })
    _AttributeMap = RSObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'GeomObject', GeomObject)


# Complex type Param with content type EMPTY
class Param (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Param')
    # Base type is pyxb.binding.datatypes.anyType

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Param', Param)


# Complex type ParamBounce with content type EMPTY
class ParamBounce (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamBounce')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamBounce_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamBounce', ParamBounce)


# Complex type ParamBounce3 with content type EMPTY
class ParamBounce3 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamBounce3')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamBounce3_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamBounce3', ParamBounce3)


# Complex type Body_ with content type ELEMENT_ONLY
class Body_ (RSObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Body')
    # Base type is RSObject
    
    # Element Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Position'), 'Position', '__AbsentNamespace0_Body__Position', False)

    
    Position = property(__Position.value, __Position.set, None, None)

    
    # Element FiniteRotationAxis uses Python identifier FiniteRotationAxis
    __FiniteRotationAxis = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'FiniteRotationAxis'), 'FiniteRotationAxis', '__AbsentNamespace0_Body__FiniteRotationAxis', False)

    
    FiniteRotationAxis = property(__FiniteRotationAxis.value, __FiniteRotationAxis.set, None, None)

    
    # Element GravityMode uses Python identifier GravityMode
    __GravityMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'GravityMode'), 'GravityMode', '__AbsentNamespace0_Body__GravityMode', False)

    
    GravityMode = property(__GravityMode.value, __GravityMode.set, None, None)

    
    # Element Quaternion uses Python identifier Quaternion
    __Quaternion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Quaternion'), 'Quaternion', '__AbsentNamespace0_Body__Quaternion', False)

    
    Quaternion = property(__Quaternion.value, __Quaternion.set, None, None)

    
    # Element Rotation uses Python identifier Rotation
    __Rotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Rotation'), 'Rotation', '__AbsentNamespace0_Body__Rotation', False)

    
    Rotation = property(__Rotation.value, __Rotation.set, None, None)

    
    # Element Mass uses Python identifier Mass
    __Mass = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Mass'), 'Mass', '__AbsentNamespace0_Body__Mass', False)

    
    Mass = property(__Mass.value, __Mass.set, None, None)

    
    # Element Force uses Python identifier Force
    __Force = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Force'), 'Force', '__AbsentNamespace0_Body__Force', False)

    
    Force = property(__Force.value, __Force.set, None, None)

    
    # Element AngularVel uses Python identifier AngularVel
    __AngularVel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'AngularVel'), 'AngularVel', '__AbsentNamespace0_Body__AngularVel', False)

    
    AngularVel = property(__AngularVel.value, __AngularVel.set, None, None)

    
    # Element Space uses Python identifier Space
    __Space = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Space'), 'Space', '__AbsentNamespace0_Body__Space', False)

    
    Space = property(__Space.value, __Space.set, None, None)

    
    # Element Name (Name) inherited from RSObject
    
    # Element LinearVel uses Python identifier LinearVel
    __LinearVel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'LinearVel'), 'LinearVel', '__AbsentNamespace0_Body__LinearVel', False)

    
    LinearVel = property(__LinearVel.value, __LinearVel.set, None, None)

    
    # Element World uses Python identifier World
    __World = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'World'), 'World', '__AbsentNamespace0_Body__World', False)

    
    World = property(__World.value, __World.set, None, None)

    
    # Element FiniteRotationMode uses Python identifier FiniteRotationMode
    __FiniteRotationMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'FiniteRotationMode'), 'FiniteRotationMode', '__AbsentNamespace0_Body__FiniteRotationMode', False)

    
    FiniteRotationMode = property(__FiniteRotationMode.value, __FiniteRotationMode.set, None, None)

    
    # Element Enabled uses Python identifier Enabled
    __Enabled = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Enabled'), 'Enabled', '__AbsentNamespace0_Body__Enabled', False)

    
    Enabled = property(__Enabled.value, __Enabled.set, None, None)

    
    # Element Torque uses Python identifier Torque
    __Torque = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Torque'), 'Torque', '__AbsentNamespace0_Body__Torque', False)

    
    Torque = property(__Torque.value, __Torque.set, None, None)


    _ElementMap = RSObject._ElementMap.copy()
    _ElementMap.update({
        __Position.name() : __Position,
        __FiniteRotationAxis.name() : __FiniteRotationAxis,
        __GravityMode.name() : __GravityMode,
        __Quaternion.name() : __Quaternion,
        __Rotation.name() : __Rotation,
        __Mass.name() : __Mass,
        __Force.name() : __Force,
        __AngularVel.name() : __AngularVel,
        __Space.name() : __Space,
        __LinearVel.name() : __LinearVel,
        __World.name() : __World,
        __FiniteRotationMode.name() : __FiniteRotationMode,
        __Enabled.name() : __Enabled,
        __Torque.name() : __Torque
    })
    _AttributeMap = RSObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Body', Body_)


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
    
    # Element Name (Name) inherited from RSObject
    
    # Attribute LZ uses Python identifier LZ
    __LZ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'LZ'), 'LZ', '__AbsentNamespace0_BoxTotalMass_LZ', pyxb.binding.datatypes.float)
    
    LZ = property(__LZ.value, __LZ.set, None, None)

    
    # Attribute M uses Python identifier M
    __M = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'M'), 'M', '__AbsentNamespace0_BoxTotalMass_M', pyxb.binding.datatypes.float)
    
    M = property(__M.value, __M.set, None, None)

    
    # Attribute LY uses Python identifier LY
    __LY = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'LY'), 'LY', '__AbsentNamespace0_BoxTotalMass_LY', pyxb.binding.datatypes.float)
    
    LY = property(__LY.value, __LY.set, None, None)

    
    # Attribute LX uses Python identifier LX
    __LX = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'LX'), 'LX', '__AbsentNamespace0_BoxTotalMass_LX', pyxb.binding.datatypes.float)
    
    LX = property(__LX.value, __LX.set, None, None)


    _ElementMap = Mass._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Mass._AttributeMap.copy()
    _AttributeMap.update({
        __LZ.name() : __LZ,
        __M.name() : __M,
        __LY.name() : __LY,
        __LX.name() : __LX
    })
Namespace.addCategoryObject('typeBinding', u'BoxTotalMass', BoxTotalMass)


# Complex type Vector_ with content type EMPTY
class Vector_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Vector')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Y uses Python identifier Y
    __Y = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Y'), 'Y', '__AbsentNamespace0_Vector__Y', pyxb.binding.datatypes.float)
    
    Y = property(__Y.value, __Y.set, None, None)

    
    # Attribute X uses Python identifier X
    __X = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'X'), 'X', '__AbsentNamespace0_Vector__X', pyxb.binding.datatypes.float)
    
    X = property(__X.value, __X.set, None, None)

    
    # Attribute Z uses Python identifier Z
    __Z = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Z'), 'Z', '__AbsentNamespace0_Vector__Z', pyxb.binding.datatypes.float)
    
    Z = property(__Z.value, __Z.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __Y.name() : __Y,
        __X.name() : __X,
        __Z.name() : __Z
    }
Namespace.addCategoryObject('typeBinding', u'Vector', Vector_)


# Complex type ParamFMax with content type EMPTY
class ParamFMax (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamFMax')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamFMax_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamFMax', ParamFMax)


# Complex type ParamSuspensionCFM3 with content type EMPTY
class ParamSuspensionCFM3 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamSuspensionCFM3')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamSuspensionCFM3_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamSuspensionCFM3', ParamSuspensionCFM3)


# Complex type ParamFMax3 with content type EMPTY
class ParamFMax3 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamFMax3')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamFMax3_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamFMax3', ParamFMax3)


# Complex type paramSuspensionERP with content type ELEMENT_ONLY
class paramSuspensionERP (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'paramSuspensionERP')
    # Base type is Param
    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_paramSuspensionERP_Value', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'paramSuspensionERP', paramSuspensionERP)


# Complex type ParamStopERP with content type EMPTY
class ParamStopERP (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamStopERP')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamStopERP_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamStopERP', ParamStopERP)


# Complex type paramVel with content type ELEMENT_ONLY
class paramVel (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'paramVel')
    # Base type is Param
    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_paramVel_Value', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'paramVel', paramVel)


# Complex type ParamStopERP3 with content type EMPTY
class ParamStopERP3 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamStopERP3')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamStopERP3_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamStopERP3', ParamStopERP3)


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

    
    # Element Body uses Python identifier Body
    __Body = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Body'), 'Body', '__AbsentNamespace0_Sim__Body', True)

    
    Body = property(__Body.value, __Body.set, None, None)

    
    # Element Name (Name) inherited from RSObject
    
    # Element Space uses Python identifier Space
    __Space = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Space'), 'Space', '__AbsentNamespace0_Sim__Space', True)

    
    Space = property(__Space.value, __Space.set, None, None)


    _ElementMap = RSObject._ElementMap.copy()
    _ElementMap.update({
        __Geom.name() : __Geom,
        __World.name() : __World,
        __Body.name() : __Body,
        __Space.name() : __Space
    })
    _AttributeMap = RSObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Sim', Sim_)


# Complex type ParamCFM3 with content type EMPTY
class ParamCFM3 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamCFM3')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamCFM3_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamCFM3', ParamCFM3)


# Complex type Quaternion_ with content type EMPTY
class Quaternion_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Quaternion')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute I uses Python identifier I
    __I = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'I'), 'I', '__AbsentNamespace0_Quaternion__I', pyxb.binding.datatypes.float)
    
    I = property(__I.value, __I.set, None, None)

    
    # Attribute K uses Python identifier K
    __K = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'K'), 'K', '__AbsentNamespace0_Quaternion__K', pyxb.binding.datatypes.float)
    
    K = property(__K.value, __K.set, None, None)

    
    # Attribute J uses Python identifier J
    __J = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'J'), 'J', '__AbsentNamespace0_Quaternion__J', pyxb.binding.datatypes.float)
    
    J = property(__J.value, __J.set, None, None)

    
    # Attribute W uses Python identifier W
    __W = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'W'), 'W', '__AbsentNamespace0_Quaternion__W', pyxb.binding.datatypes.float)
    
    W = property(__W.value, __W.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __I.name() : __I,
        __K.name() : __K,
        __J.name() : __J,
        __W.name() : __W
    }
Namespace.addCategoryObject('typeBinding', u'Quaternion', Quaternion_)


# Complex type ParamCFM2 with content type EMPTY
class ParamCFM2 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamCFM2')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamCFM2_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamCFM2', ParamCFM2)


# Complex type paramStopCFM with content type ELEMENT_ONLY
class paramStopCFM (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'paramStopCFM')
    # Base type is Param
    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_paramStopCFM_Value', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'paramStopCFM', paramStopCFM)


# Complex type ParamStopCFM2 with content type EMPTY
class ParamStopCFM2 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamStopCFM2')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamStopCFM2_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamStopCFM2', ParamStopCFM2)


# Complex type paramBounce with content type ELEMENT_ONLY
class paramBounce (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'paramBounce')
    # Base type is Param
    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_paramBounce_Value', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'paramBounce', paramBounce)


# Complex type ParamLoStop2 with content type EMPTY
class ParamLoStop2 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamLoStop2')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamLoStop2_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamLoStop2', ParamLoStop2)


# Complex type paramFudgeFactor with content type ELEMENT_ONLY
class paramFudgeFactor (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'paramFudgeFactor')
    # Base type is Param
    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_paramFudgeFactor_Value', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'paramFudgeFactor', paramFudgeFactor)


# Complex type Rotation_ with content type ELEMENT_ONLY
class Rotation_ (RSObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Rotation')
    # Base type is RSObject
    
    # Element Column3 uses Python identifier Column3
    __Column3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Column3'), 'Column3', '__AbsentNamespace0_Rotation__Column3', False)

    
    Column3 = property(__Column3.value, __Column3.set, None, None)

    
    # Element Column1 uses Python identifier Column1
    __Column1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Column1'), 'Column1', '__AbsentNamespace0_Rotation__Column1', False)

    
    Column1 = property(__Column1.value, __Column1.set, None, None)

    
    # Element Column2 uses Python identifier Column2
    __Column2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Column2'), 'Column2', '__AbsentNamespace0_Rotation__Column2', False)

    
    Column2 = property(__Column2.value, __Column2.set, None, None)

    
    # Element Name (Name) inherited from RSObject

    _ElementMap = RSObject._ElementMap.copy()
    _ElementMap.update({
        __Column3.name() : __Column3,
        __Column1.name() : __Column1,
        __Column2.name() : __Column2
    })
    _AttributeMap = RSObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Rotation', Rotation_)


# Complex type GeomCylinder_ with content type ELEMENT_ONLY
class GeomCylinder_ (GeomObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GeomCylinder')
    # Base type is GeomObject
    
    # Element CategoryBits (CategoryBits) inherited from GeomObject
    
    # Element Quaternion (Quaternion) inherited from GeomObject
    
    # Element Name (Name) inherited from RSObject
    
    # Element CollideBits (CollideBits) inherited from GeomObject
    
    # Element Enable (Enable) inherited from GeomObject
    
    # Element Position (Position) inherited from GeomObject
    
    # Element Length uses Python identifier Length
    __Length = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Length'), 'Length', '__AbsentNamespace0_GeomCylinder__Length', False)

    
    Length = property(__Length.value, __Length.set, None, None)

    
    # Element Radius uses Python identifier Radius
    __Radius = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Radius'), 'Radius', '__AbsentNamespace0_GeomCylinder__Radius', False)

    
    Radius = property(__Radius.value, __Radius.set, None, None)

    
    # Element Rotation (Rotation) inherited from GeomObject

    _ElementMap = GeomObject._ElementMap.copy()
    _ElementMap.update({
        __Length.name() : __Length,
        __Radius.name() : __Radius
    })
    _AttributeMap = GeomObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'GeomCylinder', GeomCylinder_)


# Complex type SpaceBase with content type ELEMENT_ONLY
class SpaceBase (GeomObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SpaceBase')
    # Base type is GeomObject
    
    # Element Geom uses Python identifier Geom
    __Geom = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Geom'), 'Geom', '__AbsentNamespace0_SpaceBase_Geom', True)

    
    Geom = property(__Geom.value, __Geom.set, None, None)

    
    # Element Enable (Enable) inherited from GeomObject
    
    # Element Name (Name) inherited from RSObject
    
    # Element CollideBits (CollideBits) inherited from GeomObject
    
    # Element CategoryBits (CategoryBits) inherited from GeomObject
    
    # Element Position (Position) inherited from GeomObject
    
    # Element Quaternion (Quaternion) inherited from GeomObject
    
    # Element Rotation (Rotation) inherited from GeomObject

    _ElementMap = GeomObject._ElementMap.copy()
    _ElementMap.update({
        __Geom.name() : __Geom
    })
    _AttributeMap = GeomObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SpaceBase', SpaceBase)


# Complex type SimpleSpace_ with content type ELEMENT_ONLY
class SimpleSpace_ (SpaceBase):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SimpleSpace')
    # Base type is SpaceBase
    
    # Element Geom (Geom) inherited from SpaceBase
    
    # Element Enable (Enable) inherited from GeomObject
    
    # Element Name (Name) inherited from RSObject
    
    # Element CollideBits (CollideBits) inherited from GeomObject
    
    # Element CategoryBits (CategoryBits) inherited from GeomObject
    
    # Element Position (Position) inherited from GeomObject
    
    # Element Quaternion (Quaternion) inherited from GeomObject
    
    # Element Rotation (Rotation) inherited from GeomObject

    _ElementMap = SpaceBase._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = SpaceBase._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SimpleSpace', SimpleSpace_)


# Complex type ParamFudgeFactor2 with content type EMPTY
class ParamFudgeFactor2 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamFudgeFactor2')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamFudgeFactor2_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamFudgeFactor2', ParamFudgeFactor2)


# Complex type paramSuspensionCFM with content type ELEMENT_ONLY
class paramSuspensionCFM (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'paramSuspensionCFM')
    # Base type is Param
    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_paramSuspensionCFM_Value', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'paramSuspensionCFM', paramSuspensionCFM)


# Complex type ParamStopCFM3 with content type EMPTY
class ParamStopCFM3 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamStopCFM3')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamStopCFM3_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamStopCFM3', ParamStopCFM3)


# Complex type ParamHiStop with content type EMPTY
class ParamHiStop (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamHiStop')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamHiStop_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamHiStop', ParamHiStop)


# Complex type ParamSuspensionERP2 with content type EMPTY
class ParamSuspensionERP2 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamSuspensionERP2')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamSuspensionERP2_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamSuspensionERP2', ParamSuspensionERP2)


# Complex type ParamCFM with content type EMPTY
class ParamCFM (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamCFM')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamCFM_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamCFM', ParamCFM)


# Complex type ParamStopCFM with content type EMPTY
class ParamStopCFM (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamStopCFM')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamStopCFM_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamStopCFM', ParamStopCFM)


# Complex type ParamHiStop2 with content type EMPTY
class ParamHiStop2 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamHiStop2')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamHiStop2_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamHiStop2', ParamHiStop2)


# Complex type ParamLoStop with content type EMPTY
class ParamLoStop (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamLoStop')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamLoStop_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamLoStop', ParamLoStop)


# Complex type paramHiStop with content type ELEMENT_ONLY
class paramHiStop (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'paramHiStop')
    # Base type is Param
    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_paramHiStop_Value', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'paramHiStop', paramHiStop)


# Complex type ParamVel3 with content type EMPTY
class ParamVel3 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamVel3')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamVel3_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamVel3', ParamVel3)


# Complex type ParamVel2 with content type EMPTY
class ParamVel2 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamVel2')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamVel2_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamVel2', ParamVel2)


# Complex type ParamFudgeFactor3 with content type EMPTY
class ParamFudgeFactor3 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamFudgeFactor3')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamFudgeFactor3_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamFudgeFactor3', ParamFudgeFactor3)


# Complex type ParamLoStop3 with content type EMPTY
class ParamLoStop3 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamLoStop3')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamLoStop3_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamLoStop3', ParamLoStop3)


# Complex type ParamSuspensionCFM with content type EMPTY
class ParamSuspensionCFM (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamSuspensionCFM')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamSuspensionCFM_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamSuspensionCFM', ParamSuspensionCFM)


# Complex type GeomBox with content type ELEMENT_ONLY
class GeomBox (GeomObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GeomBox')
    # Base type is GeomObject
    
    # Element Lengths uses Python identifier Lengths
    __Lengths = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Lengths'), 'Lengths', '__AbsentNamespace0_GeomBox_Lengths', False)

    
    Lengths = property(__Lengths.value, __Lengths.set, None, None)

    
    # Element Enable (Enable) inherited from GeomObject
    
    # Element Name (Name) inherited from RSObject
    
    # Element CollideBits (CollideBits) inherited from GeomObject
    
    # Element CategoryBits (CategoryBits) inherited from GeomObject
    
    # Element Position (Position) inherited from GeomObject
    
    # Element Quaternion (Quaternion) inherited from GeomObject
    
    # Element Rotation (Rotation) inherited from GeomObject

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
    
    # Element Param uses Python identifier Param
    __Param = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Param'), 'Param', '__AbsentNamespace0_Joint_Param', True)

    
    Param = property(__Param.value, __Param.set, None, None)

    
    # Element Feedback uses Python identifier Feedback
    __Feedback = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Feedback'), 'Feedback', '__AbsentNamespace0_Joint_Feedback', False)

    
    Feedback = property(__Feedback.value, __Feedback.set, None, None)

    
    # Element Body1 uses Python identifier Body1
    __Body1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Body1'), 'Body1', '__AbsentNamespace0_Joint_Body1', False)

    
    Body1 = property(__Body1.value, __Body1.set, None, None)

    
    # Element Name (Name) inherited from RSObject
    
    # Element Body2 uses Python identifier Body2
    __Body2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Body2'), 'Body2', '__AbsentNamespace0_Joint_Body2', False)

    
    Body2 = property(__Body2.value, __Body2.set, None, None)


    _ElementMap = RSObject._ElementMap.copy()
    _ElementMap.update({
        __Param.name() : __Param,
        __Feedback.name() : __Feedback,
        __Body1.name() : __Body1,
        __Body2.name() : __Body2
    })
    _AttributeMap = RSObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Joint', Joint)


# Complex type HingeJoint2_ with content type ELEMENT_ONLY
class HingeJoint2_ (Joint):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HingeJoint2')
    # Base type is Joint
    
    # Element Body2 (Body2) inherited from Joint
    
    # Element Feedback (Feedback) inherited from Joint
    
    # Element Body1 (Body1) inherited from Joint
    
    # Element Torque uses Python identifier Torque
    __Torque = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Torque'), 'Torque', '__AbsentNamespace0_HingeJoint2__Torque', False)

    
    Torque = property(__Torque.value, __Torque.set, None, None)

    
    # Element Anchor uses Python identifier Anchor
    __Anchor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Anchor'), 'Anchor', '__AbsentNamespace0_HingeJoint2__Anchor', False)

    
    Anchor = property(__Anchor.value, __Anchor.set, None, None)

    
    # Element Name (Name) inherited from RSObject
    
    # Element Param (Param) inherited from Joint
    
    # Element Axis2 uses Python identifier Axis2
    __Axis2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Axis2'), 'Axis2', '__AbsentNamespace0_HingeJoint2__Axis2', False)

    
    Axis2 = property(__Axis2.value, __Axis2.set, None, None)

    
    # Element Axis1 uses Python identifier Axis1
    __Axis1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Axis1'), 'Axis1', '__AbsentNamespace0_HingeJoint2__Axis1', False)

    
    Axis1 = property(__Axis1.value, __Axis1.set, None, None)


    _ElementMap = Joint._ElementMap.copy()
    _ElementMap.update({
        __Torque.name() : __Torque,
        __Anchor.name() : __Anchor,
        __Axis2.name() : __Axis2,
        __Axis1.name() : __Axis1
    })
    _AttributeMap = Joint._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'HingeJoint2', HingeJoint2_)


# Complex type ParamFudgeFactor with content type EMPTY
class ParamFudgeFactor (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamFudgeFactor')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamFudgeFactor_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamFudgeFactor', ParamFudgeFactor)


# Complex type paramCFM with content type ELEMENT_ONLY
class paramCFM (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'paramCFM')
    # Base type is Param
    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_paramCFM_Value', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'paramCFM', paramCFM)


# Complex type ParamSuspensionCFM2 with content type EMPTY
class ParamSuspensionCFM2 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamSuspensionCFM2')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamSuspensionCFM2_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamSuspensionCFM2', ParamSuspensionCFM2)


# Complex type paramLoStop with content type ELEMENT_ONLY
class paramLoStop (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'paramLoStop')
    # Base type is Param
    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_paramLoStop_Value', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'paramLoStop', paramLoStop)


# Complex type ParamSuspensionERP with content type EMPTY
class ParamSuspensionERP (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamSuspensionERP')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamSuspensionERP_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamSuspensionERP', ParamSuspensionERP)


# Complex type GeomCapsule_ with content type ELEMENT_ONLY
class GeomCapsule_ (GeomObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GeomCapsule')
    # Base type is GeomObject
    
    # Element CategoryBits (CategoryBits) inherited from GeomObject
    
    # Element Length uses Python identifier Length
    __Length = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Length'), 'Length', '__AbsentNamespace0_GeomCapsule__Length', False)

    
    Length = property(__Length.value, __Length.set, None, None)

    
    # Element Radius uses Python identifier Radius
    __Radius = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Radius'), 'Radius', '__AbsentNamespace0_GeomCapsule__Radius', False)

    
    Radius = property(__Radius.value, __Radius.set, None, None)

    
    # Element Name (Name) inherited from RSObject
    
    # Element CollideBits (CollideBits) inherited from GeomObject
    
    # Element Enable (Enable) inherited from GeomObject
    
    # Element Position (Position) inherited from GeomObject
    
    # Element Quaternion (Quaternion) inherited from GeomObject
    
    # Element Rotation (Rotation) inherited from GeomObject

    _ElementMap = GeomObject._ElementMap.copy()
    _ElementMap.update({
        __Length.name() : __Length,
        __Radius.name() : __Radius
    })
    _AttributeMap = GeomObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'GeomCapsule', GeomCapsule_)


# Complex type ParamVel with content type EMPTY
class ParamVel (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamVel')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamVel_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamVel', ParamVel)


# Complex type World_ with content type ELEMENT_ONLY
class World_ (RSObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'World')
    # Base type is RSObject
    
    # Element QuickStepNumIterations uses Python identifier QuickStepNumIterations
    __QuickStepNumIterations = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'QuickStepNumIterations'), 'QuickStepNumIterations', '__AbsentNamespace0_World__QuickStepNumIterations', False)

    
    QuickStepNumIterations = property(__QuickStepNumIterations.value, __QuickStepNumIterations.set, None, None)

    
    # Element ContactMaxCorrectingVel uses Python identifier ContactMaxCorrectingVel
    __ContactMaxCorrectingVel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ContactMaxCorrectingVel'), 'ContactMaxCorrectingVel', '__AbsentNamespace0_World__ContactMaxCorrectingVel', False)

    
    ContactMaxCorrectingVel = property(__ContactMaxCorrectingVel.value, __ContactMaxCorrectingVel.set, None, None)

    
    # Element ContactSurfaceLayer uses Python identifier ContactSurfaceLayer
    __ContactSurfaceLayer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ContactSurfaceLayer'), 'ContactSurfaceLayer', '__AbsentNamespace0_World__ContactSurfaceLayer', False)

    
    ContactSurfaceLayer = property(__ContactSurfaceLayer.value, __ContactSurfaceLayer.set, None, None)

    
    # Element Name (Name) inherited from RSObject
    
    # Element ERP uses Python identifier ERP
    __ERP = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ERP'), 'ERP', '__AbsentNamespace0_World__ERP', False)

    
    ERP = property(__ERP.value, __ERP.set, None, None)

    
    # Element CFM uses Python identifier CFM
    __CFM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'CFM'), 'CFM', '__AbsentNamespace0_World__CFM', False)

    
    CFM = property(__CFM.value, __CFM.set, None, None)

    
    # Element AutoDisableAngularThreshold uses Python identifier AutoDisableAngularThreshold
    __AutoDisableAngularThreshold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'AutoDisableAngularThreshold'), 'AutoDisableAngularThreshold', '__AbsentNamespace0_World__AutoDisableAngularThreshold', False)

    
    AutoDisableAngularThreshold = property(__AutoDisableAngularThreshold.value, __AutoDisableAngularThreshold.set, None, None)

    
    # Element Gravity uses Python identifier Gravity
    __Gravity = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Gravity'), 'Gravity', '__AbsentNamespace0_World__Gravity', False)

    
    Gravity = property(__Gravity.value, __Gravity.set, None, None)

    
    # Element AutoDisableFlag uses Python identifier AutoDisableFlag
    __AutoDisableFlag = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'AutoDisableFlag'), 'AutoDisableFlag', '__AbsentNamespace0_World__AutoDisableFlag', False)

    
    AutoDisableFlag = property(__AutoDisableFlag.value, __AutoDisableFlag.set, None, None)

    
    # Element AutoDisableSteps uses Python identifier AutoDisableSteps
    __AutoDisableSteps = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'AutoDisableSteps'), 'AutoDisableSteps', '__AbsentNamespace0_World__AutoDisableSteps', False)

    
    AutoDisableSteps = property(__AutoDisableSteps.value, __AutoDisableSteps.set, None, None)

    
    # Element Body uses Python identifier Body
    __Body = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Body'), 'Body', '__AbsentNamespace0_World__Body', True)

    
    Body = property(__Body.value, __Body.set, None, None)

    
    # Element AutoDisableTime uses Python identifier AutoDisableTime
    __AutoDisableTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'AutoDisableTime'), 'AutoDisableTime', '__AbsentNamespace0_World__AutoDisableTime', False)

    
    AutoDisableTime = property(__AutoDisableTime.value, __AutoDisableTime.set, None, None)


    _ElementMap = RSObject._ElementMap.copy()
    _ElementMap.update({
        __QuickStepNumIterations.name() : __QuickStepNumIterations,
        __ContactMaxCorrectingVel.name() : __ContactMaxCorrectingVel,
        __ContactSurfaceLayer.name() : __ContactSurfaceLayer,
        __ERP.name() : __ERP,
        __CFM.name() : __CFM,
        __AutoDisableAngularThreshold.name() : __AutoDisableAngularThreshold,
        __Gravity.name() : __Gravity,
        __AutoDisableFlag.name() : __AutoDisableFlag,
        __AutoDisableSteps.name() : __AutoDisableSteps,
        __Body.name() : __Body,
        __AutoDisableTime.name() : __AutoDisableTime
    })
    _AttributeMap = RSObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'World', World_)


# Complex type paramFMax with content type ELEMENT_ONLY
class paramFMax (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'paramFMax')
    # Base type is Param
    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_paramFMax_Value', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'paramFMax', paramFMax)


# Complex type ParamSuspensionERP3 with content type EMPTY
class ParamSuspensionERP3 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamSuspensionERP3')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamSuspensionERP3_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamSuspensionERP3', ParamSuspensionERP3)


# Complex type GeomPlane_ with content type ELEMENT_ONLY
class GeomPlane_ (GeomObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GeomPlane')
    # Base type is GeomObject
    
    # Element Body uses Python identifier Body
    __Body = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Body'), 'Body', '__AbsentNamespace0_GeomPlane__Body', False)

    
    Body = property(__Body.value, __Body.set, None, None)

    
    # Element Space uses Python identifier Space
    __Space = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Space'), 'Space', '__AbsentNamespace0_GeomPlane__Space', False)

    
    Space = property(__Space.value, __Space.set, None, None)

    
    # Element Enable (Enable) inherited from GeomObject
    
    # Element CategoryBits (CategoryBits) inherited from GeomObject
    
    # Element Name (Name) inherited from RSObject
    
    # Element CollideBits (CollideBits) inherited from GeomObject
    
    # Element Position (Position) inherited from GeomObject
    
    # Element Quaternion (Quaternion) inherited from GeomObject
    
    # Element Rotation (Rotation) inherited from GeomObject
    
    # Element Enabled uses Python identifier Enabled
    __Enabled = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Enabled'), 'Enabled', '__AbsentNamespace0_GeomPlane__Enabled', False)

    
    Enabled = property(__Enabled.value, __Enabled.set, None, None)


    _ElementMap = GeomObject._ElementMap.copy()
    _ElementMap.update({
        __Body.name() : __Body,
        __Space.name() : __Space,
        __Enabled.name() : __Enabled
    })
    _AttributeMap = GeomObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'GeomPlane', GeomPlane_)


# Complex type ParamBounce2 with content type EMPTY
class ParamBounce2 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamBounce2')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamBounce2_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamBounce2', ParamBounce2)


# Complex type paramStopERP with content type ELEMENT_ONLY
class paramStopERP (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'paramStopERP')
    # Base type is Param
    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_paramStopERP_Value', False)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'paramStopERP', paramStopERP)


# Complex type ParamFMax2 with content type EMPTY
class ParamFMax2 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamFMax2')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamFMax2_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamFMax2', ParamFMax2)


# Complex type HingeJoint_ with content type ELEMENT_ONLY
class HingeJoint_ (Joint):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HingeJoint')
    # Base type is Joint
    
    # Element Body2 (Body2) inherited from Joint
    
    # Element Torque uses Python identifier Torque
    __Torque = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Torque'), 'Torque', '__AbsentNamespace0_HingeJoint__Torque', False)

    
    Torque = property(__Torque.value, __Torque.set, None, None)

    
    # Element Body1 (Body1) inherited from Joint
    
    # Element Axis uses Python identifier Axis
    __Axis = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Axis'), 'Axis', '__AbsentNamespace0_HingeJoint__Axis', False)

    
    Axis = property(__Axis.value, __Axis.set, None, None)

    
    # Element Param (Param) inherited from Joint
    
    # Element Name (Name) inherited from RSObject
    
    # Element Feedback (Feedback) inherited from Joint
    
    # Element Anchor uses Python identifier Anchor
    __Anchor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Anchor'), 'Anchor', '__AbsentNamespace0_HingeJoint__Anchor', False)

    
    Anchor = property(__Anchor.value, __Anchor.set, None, None)


    _ElementMap = Joint._ElementMap.copy()
    _ElementMap.update({
        __Torque.name() : __Torque,
        __Axis.name() : __Axis,
        __Anchor.name() : __Anchor
    })
    _AttributeMap = Joint._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'HingeJoint', HingeJoint_)


# Complex type GeomSphere_ with content type ELEMENT_ONLY
class GeomSphere_ (GeomObject):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GeomSphere')
    # Base type is GeomObject
    
    # Element Quaternion (Quaternion) inherited from GeomObject
    
    # Element Enable (Enable) inherited from GeomObject
    
    # Element Name (Name) inherited from RSObject
    
    # Element CollideBits (CollideBits) inherited from GeomObject
    
    # Element CategoryBits (CategoryBits) inherited from GeomObject
    
    # Element Position (Position) inherited from GeomObject
    
    # Element Radius uses Python identifier Radius
    __Radius = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Radius'), 'Radius', '__AbsentNamespace0_GeomSphere__Radius', False)

    
    Radius = property(__Radius.value, __Radius.set, None, None)

    
    # Element Rotation (Rotation) inherited from GeomObject

    _ElementMap = GeomObject._ElementMap.copy()
    _ElementMap.update({
        __Radius.name() : __Radius
    })
    _AttributeMap = GeomObject._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'GeomSphere', GeomSphere_)


# Complex type ParamHiStop3 with content type EMPTY
class ParamHiStop3 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamHiStop3')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamHiStop3_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamHiStop3', ParamHiStop3)


# Complex type ParamStopERP2 with content type EMPTY
class ParamStopERP2 (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamStopERP2')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamStopERP2_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamStopERP2', ParamStopERP2)


# Complex type ParamGroup with content type EMPTY
class ParamGroup (Param):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamGroup')
    # Base type is Param
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_ParamGroup_Value', pyxb.binding.datatypes.float)
    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = Param._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Param._AttributeMap.copy()
    _AttributeMap.update({
        __Value.name() : __Value
    })
Namespace.addCategoryObject('typeBinding', u'ParamGroup', ParamGroup)


Sim = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Sim'), Sim_)
Namespace.addCategoryObject('elementBinding', Sim.name().localName(), Sim)

Vector = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Vector'), Vector_)
Namespace.addCategoryObject('elementBinding', Vector.name().localName(), Vector)

Rotation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Rotation'), Rotation_)
Namespace.addCategoryObject('elementBinding', Rotation.name().localName(), Rotation)

GeomCylinder = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GeomCylinder'), GeomCylinder_)
Namespace.addCategoryObject('elementBinding', GeomCylinder.name().localName(), GeomCylinder)

SimpleSpace = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimpleSpace'), SimpleSpace_)
Namespace.addCategoryObject('elementBinding', SimpleSpace.name().localName(), SimpleSpace)

Body = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Body'), Body_)
Namespace.addCategoryObject('elementBinding', Body.name().localName(), Body)

HingeJoint2 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HingeJoint2'), HingeJoint2_)
Namespace.addCategoryObject('elementBinding', HingeJoint2.name().localName(), HingeJoint2)

GeomCapsule = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GeomCapsule'), GeomCapsule_)
Namespace.addCategoryObject('elementBinding', GeomCapsule.name().localName(), GeomCapsule)

World = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'World'), World_)
Namespace.addCategoryObject('elementBinding', World.name().localName(), World)

GeomPlane = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GeomPlane'), GeomPlane_)
Namespace.addCategoryObject('elementBinding', GeomPlane.name().localName(), GeomPlane)

HingeJoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HingeJoint'), HingeJoint_)
Namespace.addCategoryObject('elementBinding', HingeJoint.name().localName(), HingeJoint)

GeomSphere = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GeomSphere'), GeomSphere_)
Namespace.addCategoryObject('elementBinding', GeomSphere.name().localName(), GeomSphere)

Quaternion = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Quaternion'), Quaternion_)
Namespace.addCategoryObject('elementBinding', Quaternion.name().localName(), Quaternion)



RSObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=RSObject))
RSObject._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(RSObject._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
RSObject._ContentModel = pyxb.binding.content.ParticleModel(RSObject._GroupModel, min_occurs=1, max_occurs=1)


Foo._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Foo._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
Foo._ContentModel = pyxb.binding.content.ParticleModel(Foo._GroupModel, min_occurs=1, max_occurs=1)



GeomObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CategoryBits'), pyxb.binding.datatypes.nonNegativeInteger, scope=GeomObject))

GeomObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CollideBits'), pyxb.binding.datatypes.nonNegativeInteger, scope=GeomObject))

GeomObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Enable'), pyxb.binding.datatypes.boolean, scope=GeomObject))

GeomObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Position'), Vector_, scope=GeomObject))

GeomObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Quaternion'), Quaternion_, scope=GeomObject))

GeomObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Rotation'), Rotation_, scope=GeomObject))
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



Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Position'), Vector_, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'FiniteRotationAxis'), Vector_, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'GravityMode'), pyxb.binding.datatypes.boolean, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Quaternion'), Quaternion_, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Rotation'), Rotation_, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Mass'), Mass, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Force'), Vector_, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AngularVel'), Vector_, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Space'), pyxb.binding.datatypes.string, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'LinearVel'), Vector_, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'World'), pyxb.binding.datatypes.string, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'FiniteRotationMode'), pyxb.binding.datatypes.nonNegativeInteger, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Enabled'), pyxb.binding.datatypes.boolean, scope=Body_))

Body_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Torque'), Vector_, scope=Body_))
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


Mass._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Mass._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
Mass._ContentModel = pyxb.binding.content.ParticleModel(Mass._GroupModel, min_occurs=1, max_occurs=1)


BoxTotalMass._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(BoxTotalMass._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
BoxTotalMass._ContentModel = pyxb.binding.content.ParticleModel(BoxTotalMass._GroupModel, min_occurs=1, max_occurs=1)



paramSuspensionERP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), Vector_, scope=paramSuspensionERP))
paramSuspensionERP._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(paramSuspensionERP._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), min_occurs=1, max_occurs=1)
    )
paramSuspensionERP._ContentModel = pyxb.binding.content.ParticleModel(paramSuspensionERP._GroupModel, min_occurs=1, max_occurs=1)



paramVel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), Vector_, scope=paramVel))
paramVel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(paramVel._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), min_occurs=1, max_occurs=1)
    )
paramVel._ContentModel = pyxb.binding.content.ParticleModel(paramVel._GroupModel, min_occurs=1, max_occurs=1)



Sim_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Geom'), GeomObject, scope=Sim_))

Sim_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'World'), World_, scope=Sim_))

Sim_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Body'), Body_, scope=Sim_))

Sim_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Space'), SpaceBase, scope=Sim_))
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



paramStopCFM._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), Vector_, scope=paramStopCFM))
paramStopCFM._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(paramStopCFM._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), min_occurs=1, max_occurs=1)
    )
paramStopCFM._ContentModel = pyxb.binding.content.ParticleModel(paramStopCFM._GroupModel, min_occurs=1, max_occurs=1)



paramBounce._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), Vector_, scope=paramBounce))
paramBounce._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(paramBounce._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), min_occurs=1, max_occurs=1)
    )
paramBounce._ContentModel = pyxb.binding.content.ParticleModel(paramBounce._GroupModel, min_occurs=1, max_occurs=1)



paramFudgeFactor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), Vector_, scope=paramFudgeFactor))
paramFudgeFactor._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(paramFudgeFactor._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), min_occurs=1, max_occurs=1)
    )
paramFudgeFactor._ContentModel = pyxb.binding.content.ParticleModel(paramFudgeFactor._GroupModel, min_occurs=1, max_occurs=1)



Rotation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Column3'), Vector_, scope=Rotation_))

Rotation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Column1'), Vector_, scope=Rotation_))

Rotation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Column2'), Vector_, scope=Rotation_))
Rotation_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Rotation_._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
Rotation_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Rotation_._UseForTag(pyxb.namespace.ExpandedName(None, u'Column1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Rotation_._UseForTag(pyxb.namespace.ExpandedName(None, u'Column2')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Rotation_._UseForTag(pyxb.namespace.ExpandedName(None, u'Column3')), min_occurs=1, max_occurs=1)
    )
Rotation_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Rotation_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Rotation_._GroupModel_2, min_occurs=1, max_occurs=1)
    )
Rotation_._ContentModel = pyxb.binding.content.ParticleModel(Rotation_._GroupModel, min_occurs=1, max_occurs=1)



GeomCylinder_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Length'), pyxb.binding.datatypes.float, scope=GeomCylinder_))

GeomCylinder_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Radius'), pyxb.binding.datatypes.float, scope=GeomCylinder_))
GeomCylinder_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCylinder_._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
GeomCylinder_._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCylinder_._UseForTag(pyxb.namespace.ExpandedName(None, u'Enable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCylinder_._UseForTag(pyxb.namespace.ExpandedName(None, u'CategoryBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCylinder_._UseForTag(pyxb.namespace.ExpandedName(None, u'CollideBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCylinder_._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCylinder_._UseForTag(pyxb.namespace.ExpandedName(None, u'Quaternion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCylinder_._UseForTag(pyxb.namespace.ExpandedName(None, u'Rotation')), min_occurs=0L, max_occurs=1)
    )
GeomCylinder_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCylinder_._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCylinder_._GroupModel_3, min_occurs=1, max_occurs=1)
    )
GeomCylinder_._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCylinder_._UseForTag(pyxb.namespace.ExpandedName(None, u'Length')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCylinder_._UseForTag(pyxb.namespace.ExpandedName(None, u'Radius')), min_occurs=0L, max_occurs=1)
    )
GeomCylinder_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCylinder_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCylinder_._GroupModel_4, min_occurs=1, max_occurs=1)
    )
GeomCylinder_._ContentModel = pyxb.binding.content.ParticleModel(GeomCylinder_._GroupModel, min_occurs=1, max_occurs=1)



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


SimpleSpace_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SimpleSpace_._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
SimpleSpace_._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SimpleSpace_._UseForTag(pyxb.namespace.ExpandedName(None, u'Enable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SimpleSpace_._UseForTag(pyxb.namespace.ExpandedName(None, u'CategoryBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SimpleSpace_._UseForTag(pyxb.namespace.ExpandedName(None, u'CollideBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SimpleSpace_._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SimpleSpace_._UseForTag(pyxb.namespace.ExpandedName(None, u'Quaternion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SimpleSpace_._UseForTag(pyxb.namespace.ExpandedName(None, u'Rotation')), min_occurs=0L, max_occurs=1)
    )
SimpleSpace_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SimpleSpace_._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SimpleSpace_._GroupModel_3, min_occurs=1, max_occurs=1)
    )
SimpleSpace_._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SimpleSpace_._UseForTag(pyxb.namespace.ExpandedName(None, u'Geom')), min_occurs=0L, max_occurs=None)
    )
SimpleSpace_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SimpleSpace_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SimpleSpace_._GroupModel_4, min_occurs=1, max_occurs=1)
    )
SimpleSpace_._ContentModel = pyxb.binding.content.ParticleModel(SimpleSpace_._GroupModel, min_occurs=1, max_occurs=1)



paramSuspensionCFM._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), Vector_, scope=paramSuspensionCFM))
paramSuspensionCFM._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(paramSuspensionCFM._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), min_occurs=1, max_occurs=1)
    )
paramSuspensionCFM._ContentModel = pyxb.binding.content.ParticleModel(paramSuspensionCFM._GroupModel, min_occurs=1, max_occurs=1)



paramHiStop._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), Vector_, scope=paramHiStop))
paramHiStop._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(paramHiStop._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), min_occurs=1, max_occurs=1)
    )
paramHiStop._ContentModel = pyxb.binding.content.ParticleModel(paramHiStop._GroupModel, min_occurs=1, max_occurs=1)



GeomBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Lengths'), Vector_, scope=GeomBox))
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



Joint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Param'), Param, scope=Joint))

Joint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Feedback'), pyxb.binding.datatypes.boolean, scope=Joint))

Joint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Body1'), pyxb.binding.datatypes.string, scope=Joint))

Joint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Body2'), pyxb.binding.datatypes.string, scope=Joint))
Joint._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Joint._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
Joint._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Joint._UseForTag(pyxb.namespace.ExpandedName(None, u'Feedback')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Joint._UseForTag(pyxb.namespace.ExpandedName(None, u'Body1')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Joint._UseForTag(pyxb.namespace.ExpandedName(None, u'Body2')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Joint._UseForTag(pyxb.namespace.ExpandedName(None, u'Param')), min_occurs=0L, max_occurs=None)
    )
Joint._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Joint._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Joint._GroupModel_2, min_occurs=1, max_occurs=1)
    )
Joint._ContentModel = pyxb.binding.content.ParticleModel(Joint._GroupModel, min_occurs=1, max_occurs=1)



HingeJoint2_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Torque'), pyxb.binding.datatypes.float, scope=HingeJoint2_))

HingeJoint2_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Anchor'), Vector_, scope=HingeJoint2_))

HingeJoint2_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Axis2'), Vector_, scope=HingeJoint2_))

HingeJoint2_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Axis1'), Vector_, scope=HingeJoint2_))
HingeJoint2_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(HingeJoint2_._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
HingeJoint2_._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(HingeJoint2_._UseForTag(pyxb.namespace.ExpandedName(None, u'Feedback')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint2_._UseForTag(pyxb.namespace.ExpandedName(None, u'Body1')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint2_._UseForTag(pyxb.namespace.ExpandedName(None, u'Body2')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint2_._UseForTag(pyxb.namespace.ExpandedName(None, u'Param')), min_occurs=0L, max_occurs=None)
    )
HingeJoint2_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(HingeJoint2_._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint2_._GroupModel_3, min_occurs=1, max_occurs=1)
    )
HingeJoint2_._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(HingeJoint2_._UseForTag(pyxb.namespace.ExpandedName(None, u'Anchor')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint2_._UseForTag(pyxb.namespace.ExpandedName(None, u'Axis1')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint2_._UseForTag(pyxb.namespace.ExpandedName(None, u'Axis2')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint2_._UseForTag(pyxb.namespace.ExpandedName(None, u'Torque')), min_occurs=0L, max_occurs=1)
    )
HingeJoint2_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(HingeJoint2_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint2_._GroupModel_4, min_occurs=1, max_occurs=1)
    )
HingeJoint2_._ContentModel = pyxb.binding.content.ParticleModel(HingeJoint2_._GroupModel, min_occurs=1, max_occurs=1)



paramCFM._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), Vector_, scope=paramCFM))
paramCFM._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(paramCFM._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), min_occurs=1, max_occurs=1)
    )
paramCFM._ContentModel = pyxb.binding.content.ParticleModel(paramCFM._GroupModel, min_occurs=1, max_occurs=1)



paramLoStop._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), Vector_, scope=paramLoStop))
paramLoStop._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(paramLoStop._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), min_occurs=1, max_occurs=1)
    )
paramLoStop._ContentModel = pyxb.binding.content.ParticleModel(paramLoStop._GroupModel, min_occurs=1, max_occurs=1)



GeomCapsule_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Length'), pyxb.binding.datatypes.float, scope=GeomCapsule_))

GeomCapsule_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Radius'), pyxb.binding.datatypes.float, scope=GeomCapsule_))
GeomCapsule_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCapsule_._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
GeomCapsule_._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCapsule_._UseForTag(pyxb.namespace.ExpandedName(None, u'Enable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCapsule_._UseForTag(pyxb.namespace.ExpandedName(None, u'CategoryBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCapsule_._UseForTag(pyxb.namespace.ExpandedName(None, u'CollideBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCapsule_._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCapsule_._UseForTag(pyxb.namespace.ExpandedName(None, u'Quaternion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCapsule_._UseForTag(pyxb.namespace.ExpandedName(None, u'Rotation')), min_occurs=0L, max_occurs=1)
    )
GeomCapsule_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCapsule_._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCapsule_._GroupModel_3, min_occurs=1, max_occurs=1)
    )
GeomCapsule_._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCapsule_._UseForTag(pyxb.namespace.ExpandedName(None, u'Length')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCapsule_._UseForTag(pyxb.namespace.ExpandedName(None, u'Radius')), min_occurs=0L, max_occurs=1)
    )
GeomCapsule_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomCapsule_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomCapsule_._GroupModel_4, min_occurs=1, max_occurs=1)
    )
GeomCapsule_._ContentModel = pyxb.binding.content.ParticleModel(GeomCapsule_._GroupModel, min_occurs=1, max_occurs=1)



World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'QuickStepNumIterations'), pyxb.binding.datatypes.nonNegativeInteger, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ContactMaxCorrectingVel'), pyxb.binding.datatypes.float, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ContactSurfaceLayer'), pyxb.binding.datatypes.float, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ERP'), pyxb.binding.datatypes.float, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CFM'), pyxb.binding.datatypes.float, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AutoDisableAngularThreshold'), pyxb.binding.datatypes.float, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Gravity'), Vector_, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AutoDisableFlag'), pyxb.binding.datatypes.boolean, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AutoDisableSteps'), pyxb.binding.datatypes.boolean, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Body'), pyxb.binding.datatypes.string, scope=World_))

World_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AutoDisableTime'), pyxb.binding.datatypes.boolean, scope=World_))
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



paramFMax._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), Vector_, scope=paramFMax))
paramFMax._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(paramFMax._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), min_occurs=1, max_occurs=1)
    )
paramFMax._ContentModel = pyxb.binding.content.ParticleModel(paramFMax._GroupModel, min_occurs=1, max_occurs=1)



GeomPlane_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Body'), pyxb.binding.datatypes.string, scope=GeomPlane_))

GeomPlane_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Space'), pyxb.binding.datatypes.string, scope=GeomPlane_))

GeomPlane_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Enabled'), pyxb.binding.datatypes.boolean, scope=GeomPlane_))
GeomPlane_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomPlane_._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
GeomPlane_._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomPlane_._UseForTag(pyxb.namespace.ExpandedName(None, u'Enable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane_._UseForTag(pyxb.namespace.ExpandedName(None, u'CategoryBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane_._UseForTag(pyxb.namespace.ExpandedName(None, u'CollideBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane_._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane_._UseForTag(pyxb.namespace.ExpandedName(None, u'Quaternion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane_._UseForTag(pyxb.namespace.ExpandedName(None, u'Rotation')), min_occurs=0L, max_occurs=1)
    )
GeomPlane_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomPlane_._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane_._GroupModel_3, min_occurs=1, max_occurs=1)
    )
GeomPlane_._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomPlane_._UseForTag(pyxb.namespace.ExpandedName(None, u'Space')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane_._UseForTag(pyxb.namespace.ExpandedName(None, u'Body')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane_._UseForTag(pyxb.namespace.ExpandedName(None, u'Enabled')), min_occurs=0L, max_occurs=1)
    )
GeomPlane_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomPlane_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomPlane_._GroupModel_4, min_occurs=1, max_occurs=1)
    )
GeomPlane_._ContentModel = pyxb.binding.content.ParticleModel(GeomPlane_._GroupModel, min_occurs=1, max_occurs=1)



paramStopERP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Value'), Vector_, scope=paramStopERP))
paramStopERP._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(paramStopERP._UseForTag(pyxb.namespace.ExpandedName(None, u'Value')), min_occurs=1, max_occurs=1)
    )
paramStopERP._ContentModel = pyxb.binding.content.ParticleModel(paramStopERP._GroupModel, min_occurs=1, max_occurs=1)



HingeJoint_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Torque'), pyxb.binding.datatypes.float, scope=HingeJoint_))

HingeJoint_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Axis'), Vector_, scope=HingeJoint_))

HingeJoint_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Anchor'), Vector_, scope=HingeJoint_))
HingeJoint_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(HingeJoint_._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
HingeJoint_._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(HingeJoint_._UseForTag(pyxb.namespace.ExpandedName(None, u'Feedback')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint_._UseForTag(pyxb.namespace.ExpandedName(None, u'Body1')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint_._UseForTag(pyxb.namespace.ExpandedName(None, u'Body2')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint_._UseForTag(pyxb.namespace.ExpandedName(None, u'Param')), min_occurs=0L, max_occurs=None)
    )
HingeJoint_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(HingeJoint_._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint_._GroupModel_3, min_occurs=1, max_occurs=1)
    )
HingeJoint_._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(HingeJoint_._UseForTag(pyxb.namespace.ExpandedName(None, u'Anchor')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint_._UseForTag(pyxb.namespace.ExpandedName(None, u'Axis')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint_._UseForTag(pyxb.namespace.ExpandedName(None, u'Torque')), min_occurs=0L, max_occurs=1)
    )
HingeJoint_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(HingeJoint_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(HingeJoint_._GroupModel_4, min_occurs=1, max_occurs=1)
    )
HingeJoint_._ContentModel = pyxb.binding.content.ParticleModel(HingeJoint_._GroupModel, min_occurs=1, max_occurs=1)



GeomSphere_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Radius'), pyxb.binding.datatypes.float, scope=GeomSphere_))
GeomSphere_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomSphere_._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), min_occurs=0L, max_occurs=1)
    )
GeomSphere_._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomSphere_._UseForTag(pyxb.namespace.ExpandedName(None, u'Enable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomSphere_._UseForTag(pyxb.namespace.ExpandedName(None, u'CategoryBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomSphere_._UseForTag(pyxb.namespace.ExpandedName(None, u'CollideBits')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomSphere_._UseForTag(pyxb.namespace.ExpandedName(None, u'Position')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomSphere_._UseForTag(pyxb.namespace.ExpandedName(None, u'Quaternion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomSphere_._UseForTag(pyxb.namespace.ExpandedName(None, u'Rotation')), min_occurs=0L, max_occurs=1)
    )
GeomSphere_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomSphere_._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomSphere_._GroupModel_3, min_occurs=1, max_occurs=1)
    )
GeomSphere_._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomSphere_._UseForTag(pyxb.namespace.ExpandedName(None, u'Radius')), min_occurs=0L, max_occurs=1)
    )
GeomSphere_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GeomSphere_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GeomSphere_._GroupModel_4, min_occurs=1, max_occurs=1)
    )
GeomSphere_._ContentModel = pyxb.binding.content.ParticleModel(GeomSphere_._GroupModel, min_occurs=1, max_occurs=1)
