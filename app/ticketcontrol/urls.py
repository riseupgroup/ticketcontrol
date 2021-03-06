"""ticketcontrol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .initial_data import load_initial_data
from .views import *

app_name = "ticketcontrol"
urlpatterns = [
    # path('admin/', admin_view),
    # Ticket
    path('ticket/my', mytickets_view, name='my_tickets'),
    path('ticket/manage', ticket_manage_view, name='manage_tickets'),
    path('ticket/new', ticket_new_view, name='create_ticket'),
    path('ticket/<int:id>', ticket_view, name="ticket_view"),
    path('ticket/<int:id>/close', ticket_close, name="close_ticket"),
    path('ticket/<int:id>/hide', ticket_hide, name="hide_ticket"),
    path('ticket/<int:id>/unhide', ticket_unhide, name="unhide_ticket"),
    path('ticket/<int:id>/delete', ticket_delete, name="delete_ticket"),
    path('ticket/<int:id>/comment/add', ticket_comment_add, name="add_comment_to_ticket"),
    path('ticket/<int:id>/participants/add/<str:username>', ticket_participant_add, name="ticket_add_participant"),
    path('ticket/<int:id>/participants/add/', ticket_participant_add, name="ticket_add_participant"),
    path('ticket/<int:id>/participants/remove/<str:username>', ticket_participant_remove, name="ticket_remove_participant"),
    path('ticket/<int:id>/moderators/add/<str:username>', ticket_moderator_add, name="ticket_add_moderator"),
    path('ticket/<int:id>/moderators/remove/<str:username>', ticket_moderator_remove, name="ticket_remove_moderator"),
    path('ticket/<int:id>/moderators/add/', ticket_moderator_add, name="ticket_add_moderator"),
    path('ticket/<int:id>/info/update/', ticket_info_update, name="update_ticket_info"),
    path('ticket/<int:id>/status/update', ticket_status_update, name="update_status_ticket"),
    path('ticket/<int:id>/edit', ticket_edit, name="edit_ticket"),
    path('comment/<int:id>/edit', comment_edit, name='edit_comment'),
    path('attachment/<int:id>', attachment_access_control, name='attachment'),
    path('attachment/<int:id>/name/<str:name>', attachment_access_control, name='attachment'),
    path('attachment/<int:id>/delete', attachment_edit, name="delete_attachment"),
    path('attachment/upload', attachment_upload, name="upload_attachment"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('register/activate', user_activate_view, name='activate_user'),
    path('user/create', user_create_view, name='create_user'),
    path('user/<int:id>', user_details_view, name='user_details'),
    path('user/<int:id>/edit', user_edit_view, name='edit_user'),
    path('user/<int:id>/delete', user_delete_view, name='delete_user'),
    path('user/passwordreset', user_passwordreset_view, name='reset_password'),
    path('user/passwordreset/request', user_passwordreset_request_view, name='reset_password_request'),
    path('user/profile', profile_view, name='profile'),
    path('user/manage', user_manage_view, name='manage_users'),
    path('user/live_search/<str:typed_username>', username_live_search, name='user_live_search'),
    path('user/live_search/', username_live_search, name='user_live_search'),
    path('user/check_username/<str:username>', username_check_view, name='check_username'),
    path('group/manage', group_manage_view, name='manage_groups'),
    path('group/create', group_create_view, name='create_group'),
    path('group/<int:id>/delete', group_delete_view, name='delete_group'),
    path('group/<int:id>', group_edit_view, name='edit_group'),
    path('settings', settings_view, name='settings'),
    path('category/manage', category_manage_view, name="manage_categories"),
    path('category/<int:id>', category_edit_view, name="edit_category"),
    path('category/<int:id>/delete', category_delete_view, name="delete_category"),
    path('category/create', category_create_view, name="create_category"),
    path('', dashboard_view, name='dashboard'),
    path('imprint', imprint_view, name='imprint'),
    path('privacy', privacy_view, name='privacy')
]

handler404 = "ticketcontrol.views.handler404"

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += path('djangoadmin/', admin.site.urls),

load_initial_data()
