import Utils.dataTypes

class EncodePong():
    def __init__(self,ping_received):
        self.command_name = "pong"

        self.nonce = ping_received

    def forge(self):
        return self.nonce


class DecodedPong():
    def __init__(self,ping_received):
        self.command_name = "pong"
        self.nonce = ping_received.read(8)

    def get_decoded_info(self):
        return "\npong   :\t\t %s" %Utils.dataTypes.read_uint64(self.nonce)
