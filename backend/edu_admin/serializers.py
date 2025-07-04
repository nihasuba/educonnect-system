from rest_framework import serializers

class ZoomWebinarSerializer(serializers.Serializer):
    account_key = serializers.CharField()
    topic = serializers.CharField()
    start_time = serializers.CharField()
    duration = serializers.IntegerField()
    agenda = serializers.CharField(allow_blank=True, required=False)

    repeat_type = serializers.ChoiceField(
        choices=['daily', 'weekly', 'monthly'],
        default= "none",
        required=False
    )
    repeat_interval = serializers.IntegerField(default=1, required=False)
    end_date_time = serializers.CharField(required=False, allow_blank=True)

class ZoomWebinarListSerializer(serializers.Serializer):
    account_key = serializers.CharField(required=True)

    # def validate_account_key(self, value):
    #     if not value:
    #         raise serializers.ValidationError("Account key is required")
    #     return value
