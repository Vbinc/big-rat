import time
from transaction_values import transaction_value
import zlib
import base64
import jsons
import json

class transaction:
    source = ""
    values = []

    def __init__(self, source):
        self.source = source

    def add_value(self, value: transaction_value):
        self.values.append(value)

    def add_values(self, values: list):
        for value in values:
            self.values.append(value)

    def write(self, file_name=source + str(int(time.time())) + ".indicator", use_compression=True, use_base64=True):
        """
        Write the indicator to a file, with compression via zlib and encoding with base64.
        """
        # make indicator into a serialable object
        object_dict = { transaction: self }
        # convert to JSON string
        json_object = json.dumps(object_dict, skipkeys=True)
        # conver to bytes
        json_bytes = json_object.encode('utf-8')

        ret_object = json_bytes
        # compress JSON string via zlib
        if (use_compression & use_base64): 
            # compress JSON string via zlib
            ret_object = zlib.compress(json_bytes)
            # encode compressed JSON string via base64
            ret_object = base64.b64encode(ret_object).decode('utf-8')
            # append the string to the file
            with open(file_name, "a") as file:
                file.write(ret_object)
                file.write('\n')

        elif (use_compression):
            # compress JSON string via zlib
            ret_object = zlib.compress(json_bytes)
            # append compressed JSON string to file
            with open(file_name, 'wb') as file:
                file.write(ret_object)
                file.write(b'\n')

        elif (use_base64):
            # encode JSON string with base64
            ret_object = base64.b64encode(json_bytes).decode('utf-8')
            # append encoded JSON string to file
            with open(file_name, 'w') as file:
                file.write(ret_object)
                file.write('\n')
