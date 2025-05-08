from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='user-create'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('profile/', ProfileView.as_view(), name='user-profile'),
    path('mentee/', Fieldofinterest.as_view(), name='become-a-mentee'),
    path('mentor/', ExpertField.as_view(), name='update-expertise'),
    path('profile/edit/', ProfileUpdate.as_view(), name='profile-update'),
    path('mentors/', MentorList.as_view(), name='list-mentors'),
    path('metrics/', Metrics.as_view(), name='metrics'),
]