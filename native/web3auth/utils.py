# https://github.com/atereshkin/django-web3-auth/blob/master/web3auth/utils.py
import sha3
import ethereum

def sig_to_vrs(sig):
    # sig_bytes = bytes.fromhex(sig[2:])
    r = int(sig[2:66], 16)
    s = int(sig[66:130], 16)
    v = int(sig[130:], 16)
    return v,r,s


def hash_personal_message(msg):
    padded = "\x19Ethereum Signed Message:\n" + str(len(str(msg))) + str(msg)
    return sha3.keccak_256(bytes(padded, 'utf8')).digest()


def recover_to_addr(msg, sig):
    msghash = hash_personal_message(msg)
    vrs = sig_to_vrs(sig)
    return '0x' + sha3.keccak_256(ethereum.utils.ecrecover_to_pub(msghash, *vrs)).hexdigest()[24:]