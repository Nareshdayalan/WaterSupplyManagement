from django.urls import path
from . import views

urlpatterns = [
    # path('welcome/',views.welcome,name = 'welcome'),
    #path('waterManagement/',views.get_water_management_details,name = 'waterManagement'),
    # path('getSupplier',views.GetSuppliers.as_view(),name = 'getSupplier'),
    #path('getCustomer',views.GetCustomers.as_view(),name = 'getCustomer'),
    #path('addSupplier',views.AddSupplier.as_view(),name = 'addSupplier'),
    #path('addCustomer',views.AddCustomer.as_view(),name = 'addCustomer')
    path('getWatercans',views.GetWatercans.as_view(),name = 'getWatercan'),
    path('addWatercan',views.AddWatercan.as_view(),name = 'addWatercan'),
    path('getWatercanDetails',views.GetWatercanDetails.as_view(),name = 'getWatercanDetails'),
    path('getUserInfos',views.GetUserInfos.as_view(),name = 'getUserInfos'),
    path('addUserInfo',views.AddUserInfo.as_view(),name='addUserInfo'),
    path('getUserDetails',views.GetUserDetails.as_view(),name = 'getUserDetails' ),
   

 ]
