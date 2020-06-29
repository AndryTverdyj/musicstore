from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from musicstore.models import MusicWork, MusicWorkFile
from musicstore.serializers import MusicWorkSerializer, MusicWorkFileSerializer


class MusicWorkAPIView(ModelViewSet):
    allowed_methods = [u'get']
    queryset = MusicWork.objects.all()
    serializer_class = MusicWorkSerializer

    def get_queryset(self):
        queryset = MusicWork.objects.all()
        iswc =  self.request.query_params.get('iswc', None)
        if iswc is not None:
            queryset = queryset.filter(iswc=iswc)
        return queryset


class MusikWorkFileUpload(CreateAPIView):
    queryset = MusicWorkFile.objects.all()
    serializer_class = MusicWorkFileSerializer
