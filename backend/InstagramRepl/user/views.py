from rest_framework.exceptions import NotFound
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.views.generic import TemplateView
from rest_auth.registration.serializers import VerifyEmailSerializer
from django.http import HttpResponseRedirect


@api_view
def django_rest_auth_null():
    return Response(status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(APIView):
    """
    Verify Email View that would provide success detail once email 
    has been verified.
    """
    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get_serializer(self, *args, **kwargs):
        return VerifyEmailSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        try:
            confirmation = self.get_object()
            confirmation.confirm(self.request)
            return Response({'detail': _("Successfully confirmed email.")}, status=status.HTTP_200_OK)
        except:
            return Response({'detail': _("Error. Incorrect key.")}, status=status.HTTP_404_NOT_FOUND)


class ConfirmEmailView(APIView):
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)
        # A React Router Route will handle the successful scenario
        return HttpResponseRedirect('/login/success/')

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        email_confirmation = EmailConfirmationHMAC.from_key(key)
        if not email_confirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                email_confirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                # A React Router Route will handle the failure scenario
                return HttpResponseRedirect('/login/failure/')
        return email_confirmation

    def get_queryset(self):
        qs = EmailConfirmation.objects.all_valid()
        qs = qs.select_related("email_address__user")
        return qs
