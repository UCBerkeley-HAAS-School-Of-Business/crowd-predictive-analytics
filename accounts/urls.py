from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm, PwdResetForm, PwdChangeForm, PwdResetForm, PwdResetConfirmForm
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="accounts/password_change_form.html",
                                                                   form_class=PwdChangeForm), name='pwdforgot'),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html",
                                                authentication_form=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/logged_out.html") , name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html",
                                                                 form_class=PwdResetForm), name='pwdreset'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html', form_class=PwdResetConfirmForm), name="pwdresetconfirm"),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit, name='edit'),
    path('profile/delete/', views.delete_user, name='deleteuser'),
    path('register/', views.accounts_register, name='register')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
