import hashlib
import zlib
import os

object_dir = ".ivcs/objects"

def create_blob_object(data, type="blob"):
    """
    Takes file contents, hashes them using sha1 and stores in objects directory
    """
    header = f"blob {len(data)}\0".encode()
    store = header + data
    hash_object = hashlib.sha1(store).hexdigest()

    hash_path = os.path.join(object_dir, hash_object[:2], hash_object[2:])
    os.makedirs(os.path.dirname(hash_path), exist_ok=True)

    compressed = zlib.compress(data)

    with open(hash_path, 'wb') as f:
        f.write(compressed)
    
    return hash_object
