from base64 import b64decode
import pickle

code = b'KGRwMApTJ3NlcnVtJwpwMQpjY29weV9yZWcKX3JlY29uc3RydWN0b3IKcDIKKGNfX21haW5fXwphbnRpX3BpY2tsZV9zZXJ1bQpwMwpjX19idWlsdGluX18Kb2JqZWN0CnA0Ck50cDUKUnA2CnMu'
# anti_pickle_serum = 'test'

class anti_pickle_serum(object):
    def __init__(self):
        pass

serum = pickle.loads(b64decode(code))
print(serum)



