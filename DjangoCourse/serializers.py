from django.utils.timezone import now
from rest_framework import serializers
from DjangoCourse.models import Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        # fields = '__all__'
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created')

    def get_days_since_created(self, obj):
        return (now() - obj.created).days
