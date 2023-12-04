from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response

from utils.verification import send_verification_code
from .models import Category, Document, Form, Company
from .serializers import CategorySerializer, DocumentSerializer, FormSerializer, CompanySerializer, \
    SendVerificationCodeSerializer
from utils.bot import bot


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class DocumentCustomFilterView(generics.ListAPIView):
    serializer_class = DocumentSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('document_type', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        document_type = self.request.query_params.get('document_type', None)

        if document_type:
            queryset = Document.objects.filter(type=document_type)
            if not queryset.exists():
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'types': [Document.DocumentTypes.DOCUMENT, Document.DocumentTypes.CERTIFICATE,
                                       Document.DocumentTypes.PROJECT]})

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FormCreateView(generics.CreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        bot.send_message(f"Full name: {serializer.validated_data.get('full_name')}\n"
                         f"Organization: {serializer.validated_data.get('organization')}\n"
                         f"Phone number: {serializer.validated_data.get('phone_number')}\n"
                         f"Email: {serializer.validated_data.get('email')}\n"
                         f"Description: {serializer.validated_data.get('desc')}")
        return super().post(request, *args, **kwargs)


class CompanyRetrieveView(generics.RetrieveAPIView):
    serializer_class = CompanySerializer

    def get_object(self):
        return Company.objects.first()


class SendVerificationCodeView(generics.CreateAPIView):
    serializer_class = SendVerificationCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data.get("phone_number")
        code = send_verification_code(phone_number)

        return Response({phone_number: code}, status=status.HTTP_201_CREATED)
