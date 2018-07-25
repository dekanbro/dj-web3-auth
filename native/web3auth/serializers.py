import string
from rest_framework import serializers


class Web3TokenSerializer(serializers.Serializer):

    signature = serializers.CharField(required=True, allow_blank=False)
    username = serializers.CharField(max_length=42, required=True, allow_blank=False)


    def validate_signature(self, sig):
        if len(sig) != 132 or (sig[130:] != '1b' and  sig[130:] != '1c') or not all(c in string.hexdigits for c in sig[2:]):
            raise serializers.ValidationError('Invalid signature')

        # self.user = authenticate(token=self.token, signature=sig)
        return sig


class SignupSerializer(serializers.Serializer):

    signature = serializers.CharField(required=True, allow_blank=False)
    username = serializers.CharField(max_length=42, required=True, allow_blank=False)
    email = serializers.EmailField(required=False, allow_blank=True)


    def validate_signature(self, sig):
        if len(sig) != 132 or (sig[130:] != '1b' and  sig[130:] != '1c') or not all(c in string.hexdigits for c in sig[2:]):
            raise serializers.ValidationError('Invalid signature')

        # self.user = authenticate(token=self.token, signature=sig)
        return sig