from django.urls import path
from .views import productlistview, supplierlistview, addsupplier, addproduct, \
    deleteproduct, confirmdeleteproduct, deletesupplier, confirmdeletesupplier, edit_product_get, edit_product_post, \
    edit_supplier_get, edit_supplier_post, searchsuppliers, products_filtered, loginview, login_action, logout_action

urlpatterns = [
    # LANDING PAGE AFTER LOGIN
    #path('landing/', landingview),

    # Login and authentication
    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),

    # Products
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
    path('products-by-supplier/<int:id>/', products_filtered),

    # Suppliers
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('edit-supplier-get/<int:id>/', edit_supplier_get),
    path('edit-supplier-post/<int:id>/', edit_supplier_post),
    path('search-suppliers/', searchsuppliers),
]
