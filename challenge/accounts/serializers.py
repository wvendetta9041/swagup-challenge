from rest_framework import serializers

from . import models


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = '__all__'

class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ('phone', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_zip', 'shipping_country')
