from django.urls import path
from . import views

urlpatterns = [
    # الصفحات الرئيسية
    path('', views.home_view, name='home'),
    path('granite/', views.granite_view, name='granite_page'),
    path('porcelain/', views.porcelain_view, name='porcelain_page'),
    path('stainless/', views.stainless_view, name='stainless_page'),
    path('contact/', views.contact_view, name='contact_page'),
    path('my-admin/edit/<int:product_id>/', views.admin_edit_product, name='admin_edit'),
    
    # صفحة تسجيل دخول الأدمن
    # تأكد أن الاسم هنا 'admin_login' ليطابق الـ login_url في الـ views
    path('panel-login/', views.admin_login_view, name='admin_login'),
    
    # مسارات لوحة التحكم المخصصة
    path('my-admin/', views.custom_admin_dashboard, name='admin_dashboard'),
    path('my-admin/add/', views.admin_add_product, name='admin_add'),
    
    # مسار الحذف (شلت الـ /not-found/ عشان يكون المسار أنظف وأسهل)
    path('my-admin/delete/<int:product_id>/', views.admin_delete_product, name='admin_delete'),
]