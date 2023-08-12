import uuid

def is_valid_uuid(uuid_str):
    try:
        uuid_obj = uuid.UUID(str(uuid_str))
        return str(uuid_obj) == uuid_str  # Check if the string representation of the UUID matches the input
    except ValueError:
        return False
    
def generate_uuid():
    return str(uuid.uuid4())