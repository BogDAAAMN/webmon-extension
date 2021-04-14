from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from django.views.decorators.csrf import csrf_exempt


# Import generic logout view
from django.contrib.auth.views import LogoutView


from .views import (
    RegisterUser, ListUsers,
     UserView,DeployContract,
    RegisterCause, createDonation,
    UserSearch,getDonation,
    InfluencerSearch, DonorSearch,
    CauseSearch, DonationSearchByCause,
    DonationSearchByDonor, DonationSearchByCauseID,
    DonationSearchByDonorID
    )

# Import settings to access environment variables 
from django.conf import settings

# Import view functions here
from search.views import search_view

from API.views import login

from lucehome.views import (
    
    dev_view,
    # register_view,

    LoginView,
    LoginView_PostReg,
    )

from datastore.views import (
	upload_view,
	browse_view,
    my_data_view,
    detail_view,
    update_view,
    # UpdateView,
    delete_view,
    publish_view,
    request_access_view,
    my_access_view,
    upload_success_view,
    publish_success_view,
    update_success_view
	)


urlpatterns = [
    path('user/register/', RegisterUser.as_view()),
    path('user/influencer/', InfluencerSearch.as_view()),
    path('user/donor/', DonorSearch.as_view()),
    path('user/all/', UserSearch.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('donation/create/', createDonation.as_view()), 
    path('donation/get/', getDonation.as_view()),
    path('donation/cause/', DonationSearchByCause.as_view()),
    path('donation/cause/id/', DonationSearchByCauseID.as_view()),
    path('donation/donor/',DonationSearchByDonor.as_view()),
    path('donation/donor/id/', DonationSearchByDonorID.as_view()),
    path('user/', UserView.as_view()),
    path('cause/register/', RegisterCause.as_view()),
    path('cause/', CauseSearch.as_view()),
    path('deploy/', DeployContract.as_view()),
    path('luce_admin/', admin.site.urls),
    path('login-uphold/', login),
    path('upload/', upload_view),
    path('browse/', browse_view),
    path('my_data/', my_data_view),
    path('my_access/', my_access_view),
    path('dev/', dev_view),
    path('search/', search_view),

    # path('register/', register_view),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path('search/', search_view),

    # Post Registration/Upload Views
    path('register_login/', LoginView_PostReg.as_view()),
    # path('upload_success/', ),

    

    path('data/<int:dataset_id>/', detail_view),
    path('data/<int:dataset_id>/edit', update_view),
    path('data/<int:dataset_id>/delete', delete_view),
    path('data/<int:dataset_id>/publish', publish_view),
    path('data/<int:dataset_id>/request', request_access_view),
    path('data/<int:dataset_id>/upload_success', upload_success_view),
    path('data/<int:dataset_id>/publish_success', publish_success_view),
    path('data/<int:dataset_id>/update_success', update_success_view)
    # re_path(r'^data/(?P<slug>\w+)/$', detail_view)

    ]
urlpatterns = format_suffix_patterns(urlpatterns)


if settings.DEBUG:
    # Use local simulated CDN
    # Add the following to urlpatterns
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)