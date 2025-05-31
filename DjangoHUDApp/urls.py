from django.urls import path
from . import views

app_name = 'DjangoHUDApp'
urlpatterns = [
    # Main pages
    path('', views.index, name='index'),
    path('404/', views.error404, name='error404'),
    path('analytics/', views.analytics, name='analytics'),
    path('settings/', views.settings, name='settings'),
    path('product/', views.product, name='product'),
    path('finance/', views.finance, name='finance'),
    
    # Email related URLs
    path('email/inbox/', views.emailInbox, name='emailInbox'),
    path('email/detail/', views.emailDetail, name='emailDetail'),
    path('email/compose/', views.emailCompose, name='emailCompose'),
    path('email/', views.email, name='email'),
    path('email/style/', views.email_style, name='emailStyle'),
    path('email/user-fields/', views.email_user_fields, name='emailUserFields'),
    
    # User Management URLs
    path('usermanagement/', views.user_management, name='userManagement'),
    path('usermanagement/administrator/', views.administrator, name='administrator'),
    path('usermanagement/administrator/moderator/', views.moderator, name='moderator'),
    path('usermanagement/administrator/staff/', views.staff, name='staff'),
    path('usermanagement/subscribers/', views.subscribers, name='subscribers'),
    path('usermanagement/businesses/', views.businesses, name='businesses'),
    
    # User Fields URLs
    path('user-fields/block/', views.user_fields_block, name='userFieldsBlock'),
    path('user-fields/censor/', views.user_fields_censor, name='userFieldsCensor'),
    path('user-fields/require-approval/', views.user_fields_require_approval, name='userFieldsRequireApproval'),
    path('user-fields/flag/', views.user_fields_flag, name='userFieldsFlag'),
    path('user-fields/replace/', views.user_fields_replace, name='userFieldsReplace'),
    path('user-fields/auto-tag/', views.user_fields_auto_tag, name='userFieldsAutoTag'),
    
    # Design URLs
    path('design/customize/', views.design_customize, name='designCustomize'),
    path('design/thememodes/', views.design_theme_modes, name='themeModes'),
    path('design/customize/plugins/', views.design_customize_plugins, name='designCustomizePlugins'),
    path('design/customize/apis/', views.design_customize_apis, name='designCustomizeAPIs'),
    path('design/text/', views.design_text, name='designText'),
    path('design/emoji/', views.design_emoji, name='designEmoji'),
    path('design/permalinks/', views.design_permalinks, name='designPermalinks'),
    path('design/embedding/', views.design_embedding, name='designEmbedding'),
    path('design/watched-words/', views.design_watched_words, name='designWatchedWords'),
    
    # Security URL
    path('security/', views.security, name='security'),
    
    # Maintenance URLs
    path('maintenance/', views.maintenance, name='maintenance'),
    path('maintenance/logs/', views.maintenance_logs, name='maintenanceLogs'),
    path('maintenance/backup/', views.backup, name='backup'),
    
    # Customer Support URL
    path('support/', views.customer_support, name='customerSupport'),
    
    # Miscellaneous URL
    path('miscellaneous/', views.miscellaneous, name='miscellaneous'),
    
    # UI Components
    path('widgets/', views.widgets, name='widgets'),
    path('ui/bootstrap/', views.uiBootstrap, name='uiBootstrap'),
    path('ui/buttons/', views.uiButtons, name='uiButtons'),
    path('ui/card/', views.uiCard, name='uiCard'),
    path('ui/icons/', views.uiIcons, name='uiIcons'),
    path('ui/modal-notifications/', views.uiModalNotifications, name='uiModalNotifications'),
    path('ui/typography/', views.uiTypography, name='uiTypography'),
    path('ui/tabs-accordions/', views.uiTabsAccordions, name='uiTabsAccordions'),
    
    # Form Components
    path('form/elements/', views.formElements, name='formElements'),
    path('form/plugins/', views.formPlugins, name='formPlugins'),
    path('form/wizards/', views.formWizards, name='formWizards'),
    
    # Table Components
    path('table/elements/', views.tableElements, name='tableElements'),
    path('table/plugins/', views.tablePlugins, name='tablePlugins'),
    
    # Chart Components
    path('chart/js/', views.chartJs, name='chartJs'),
    path('chart/apex/', views.chartApex, name='chartApex'),
    
    # Other pages
    path('map/', views.map, name='map'),
    path('calendar/', views.calendar, name='calendar'),
    path('profile/', views.profile, name='profile'),
    path('helper/', views.helper, name='helper'),
    path('landing/', views.landing, name='landing'),
    
    # Layout Options
    path('layout/starter/', views.layoutStarter, name='layoutStarter'),
    path('layout/fixed-footer/', views.layoutFixedFooter, name='layoutFixedFooter'),
    path('layout/full-height/', views.layoutFullHeight, name='layoutFullHeight'),
    path('layout/full-width/', views.layoutFullWidth, name='layoutFullWidth'),
    path('layout/boxed-layout/', views.layoutBoxedLayout, name='layoutBoxedLayout'),
    path('layout/collapsed-sidebar/', views.layoutCollapsedSidebar, name='layoutCollapsedSidebar'),
    path('layout/top-nav/', views.layoutTopNav, name='layoutTopNav'),
    path('layout/mixed-nav/', views.layoutMixedNav, name='layoutMixedNav'),
    path('layout/mixed-nav-boxed-layout/', views.layoutMixedNavBoxedLayout, name='layoutMixedNavBoxedLayout'),
    
    # Additional Pages
    path('page/scrum-board/', views.pageScrumBoard, name='pageScrumBoard'),
    path('page/product/', views.pageProduct, name='pageProduct'),
    path('page/product-details/', views.pageProductDetails, name='pageProductDetails'),
    path('page/order/', views.pageOrder, name='pageOrder'),
    path('page/order-details/', views.pageOrderDetails, name='pageOrderDetails'),
    path('page/gallery/', views.pageGallery, name='pageGallery'),
    path('page/search-results/', views.pageSearchResults, name='pageSearchResults'),
    path('page/coming-soon/', views.pageComingSoon, name='pageComingSoon'),
    path('page/error/', views.pageError, name='pageError'),
    path('page/login/', views.pageLogin, name='pageLogin'),
    path('page/register/', views.pageRegister, name='pageRegister'),
    path('page/messenger/', views.pageMessenger, name='pageMessenger'),
    path('page/data-management/', views.pageDataManagement, name='pageDataManagement'),
    path('page/file-manager/', views.pageFileManager, name='pageFileManager'),
    path('page/pricing/', views.pagePricing, name='pagePricing'),
    
    # AI Pages
    path('ai/chat/', views.aiChat, name='aiChat'),
    path('ai/image-generator/', views.aiImageGenerator, name='aiImageGenerator'),
    
    # POS Pages
    path('pos/customer-order/', views.posCustomerOrder, name='posCustomerOrder'),
    path('pos/kitchen-order/', views.posKitchenOrder, name='posKitchenOrder'),
    path('pos/counter-checkout/', views.posCounterCheckout, name='posCounterCheckout'),
    path('pos/table-booking/', views.posTableBooking, name='posTableBooking'),
    path('pos/menu-stock/', views.posMenuStock, name='posMenuStock'),
]