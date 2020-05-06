from django.urls import path, include, re_path
import rest_auth.registration.views
import user.views

urlpatterns = [
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/verify-email',
            user.views.VerifyEmailView.as_view(), name='rest_verify_email'),
    path('rest-auth/registration/',
         rest_auth.registration.views.RegisterView.as_view(), name='rest_register'),
    path('password-reset/confirm/<str:uidb64>)/<str:token>/',
         user.views.django_rest_auth_null, name='password_reset_confirm'),
    re_path(r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$',
            user.views.VerifyEmailView.as_view(), name='account_confirm_email'),
]
# re_path(r'^rest-auth/registration/',
#         include('rest_auth.registration.urls')),
