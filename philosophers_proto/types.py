"""
Data types management for .proto files compilation
"""

import enum
from sqlalchemy.sql.sqltypes import *


# todo: finish datatype mappings
class DataType(enum.Enum):
    int = 'int'
    float = 'float'
    rpc = 'rpc'
    message = 'message'
    double = 'double'
    int16 = 'int16'
    int32 = 'int32'
    int64 = 'int64'
    long = 'long'
    repeated = 'repeated'
    string = 'string'


# todo: add the missing types
TYPES_MAP_SQLALCHEMY_TO_DATATYPE = {
    Integer: DataType.int,
    String: DataType.string
}


class TypeResolver:
    @staticmethod
    def from_sqlalchemy(dtype):
        return TYPES_MAP_SQLALCHEMY_TO_DATATYPE[dtype]
