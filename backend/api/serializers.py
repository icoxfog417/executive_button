from django.contrib.auth.models import User, Group
from api.models import Remuneration
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class RemunerationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Remuneration
        fields = [
            'edinet_code', 'sec_code', 'filer_name',
            'doc_description', 'doc_id', 'period_start', 'period_end',
            'amount', 'number']
