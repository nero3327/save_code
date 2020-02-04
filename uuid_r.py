import uuid
print(uuid.uuid5(uuid.NAMESPACE_DNS, str(uuid.uuid4())))
