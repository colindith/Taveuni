from rest_framework import serializers
from map.models import Cell


class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = '__all__'

    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        print(f'ret: {ret}')
        # if data.get('level'):
        #     ret['level'] = \
        #         [int(level) for level in data.get('level').split(',')]
        # if data.get('bank'):
        #     ret['bank'] = data.get('bank')

        return ret