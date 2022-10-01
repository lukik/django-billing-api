import uuid
import json


def get_uuid():
    """Generate UUID"""
    return uuid.uuid4()


def jsonify(data):
    """Returns JSON formatted data"""
    return json.dumps(data)


def json_dump(data):
    """Serialize ``obj`` to a JSON formatted ``str``"""
    return json.dumps(data)


def json_load(data):
    """Deserialize ``s`` (a ``str``, ``bytes`` or ``bytearray`` instance
    containing a JSON document) to a Python object"""
    return json.loads(data)

