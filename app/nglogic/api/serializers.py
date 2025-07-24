from rest_framework import serializers


class NglogicApiSerializer(serializers.Serializer):
    idx = serializers.IntegerField(required=False)
    value = serializers.IntegerField()
    message = serializers.CharField(required=False)

    def validate(self, data):
        if not isinstance(data["value"], int):
            raise serializers.ValidationError("Value must be an integer")

        if data["idx"] is not None and not isinstance(data["idx"], int):
            raise serializers.ValidationError("Value must be an integer")

        return data
