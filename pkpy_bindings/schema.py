from dataclasses import dataclass
from typing import Any, List, Union, Optional, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


@dataclass
class Alias:
    type: str
    name: str
    description: str

    @staticmethod
    def from_dict(obj: Any) -> 'Alias':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        return Alias(type, name, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        return result


@dataclass
class Param:
    type: str
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Param':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        name = from_str(obj.get("name"))
        return Param(type, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["name"] = from_str(self.name)
        return result


@dataclass
class Callback:
    name: str
    description: str
    return_type: str
    params: List[Param]

    @staticmethod
    def from_dict(obj: Any) -> 'Callback':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        return_type = from_str(obj.get("returnType"))
        params = from_list(Param.from_dict, obj.get("params"))
        return Callback(name, description, return_type, params)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["returnType"] = from_str(self.return_type)
        result["params"] = from_list(lambda x: to_class(Param, x), self.params)
        return result


@dataclass
class Define:
    name: str
    type: str
    value: Union[float, str]
    description: str

    @staticmethod
    def from_dict(obj: Any) -> 'Define':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        type = from_str(obj.get("type"))
        value = from_union([from_float, from_str], obj.get("value"))
        description = from_str(obj.get("description"))
        return Define(name, type, value, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["type"] = from_str(self.type)
        result["value"] = from_union([to_float, from_str], self.value)
        result["description"] = from_str(self.description)
        return result


@dataclass
class ValueElement:
    name: str
    value: int
    description: str

    @staticmethod
    def from_dict(obj: Any) -> 'ValueElement':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        value = from_int(obj.get("value"))
        description = from_str(obj.get("description"))
        return ValueElement(name, value, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["value"] = from_int(self.value)
        result["description"] = from_str(self.description)
        return result


@dataclass
class EnumElement:
    name: str
    description: str
    values: List[ValueElement]

    @staticmethod
    def from_dict(obj: Any) -> 'EnumElement':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        values = from_list(ValueElement.from_dict, obj.get("values"))
        return EnumElement(name, description, values)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["values"] = from_list(lambda x: to_class(ValueElement, x), self.values)
        return result


@dataclass
class Function:
    name: str
    description: str
    return_type: str
    params: Optional[List[Param]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Function':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        return_type = from_str(obj.get("returnType"))
        params = from_union([lambda x: from_list(Param.from_dict, x), from_none], obj.get("params"))
        return Function(name, description, return_type, params)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["returnType"] = from_str(self.return_type)
        if self.params is not None:
            result["params"] = from_union([lambda x: from_list(lambda x: to_class(Param, x), x), from_none], self.params)
        return result


@dataclass
class Struct:
    name: str
    description: str
    fields: List[Alias]

    @staticmethod
    def from_dict(obj: Any) -> 'Struct':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        fields = from_list(Alias.from_dict, obj.get("fields"))
        return Struct(name, description, fields)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["fields"] = from_list(lambda x: to_class(Alias, x), self.fields)
        return result


@dataclass
class Header:
    defines: List[Define]
    structs: List[Struct]
    aliases: List[Alias]
    enums: List[EnumElement]
    callbacks: List[Callback]
    functions: List[Function]

    @staticmethod
    def from_dict(obj: Any) -> 'Header':
        assert isinstance(obj, dict)
        defines = from_list(Define.from_dict, obj.get("defines"))
        structs = from_list(Struct.from_dict, obj.get("structs"))
        aliases = from_list(Alias.from_dict, obj.get("aliases"))
        enums = from_list(EnumElement.from_dict, obj.get("enums"))
        callbacks = from_list(Callback.from_dict, obj.get("callbacks"))
        functions = from_list(Function.from_dict, obj.get("functions"))
        return Header(defines, structs, aliases, enums, callbacks, functions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["defines"] = from_list(lambda x: to_class(Define, x), self.defines)
        result["structs"] = from_list(lambda x: to_class(Struct, x), self.structs)
        result["aliases"] = from_list(lambda x: to_class(Alias, x), self.aliases)
        result["enums"] = from_list(lambda x: to_class(EnumElement, x), self.enums)
        result["callbacks"] = from_list(lambda x: to_class(Callback, x), self.callbacks)
        result["functions"] = from_list(lambda x: to_class(Function, x), self.functions)
        return result


def header_from_dict(s: Any) -> Header:
    return Header.from_dict(s)


def header_to_dict(x: Header) -> Any:
    return to_class(Header, x)
