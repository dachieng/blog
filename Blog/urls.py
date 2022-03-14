
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("blogapp.urls")),
    path('authentication/',include("accounts.urls")),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name="accounts/password-reset.html"),name="password-reset"),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password-reset-done.html"),name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password-reset-confirm.html"),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password-reset-complete.html"),name="password_reset_complete")

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)