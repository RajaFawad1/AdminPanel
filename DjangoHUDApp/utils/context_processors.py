from django.urls import resolve

def mark_active_link(menu, current_path_name):
    for item in menu:
        item['is_active'] = item.get('name', '') == current_path_name

        if 'children' in item:
            item['children'] = mark_active_link(item['children'], current_path_name)

            if any(child.get('is_active', False) for child in item['children']):
                item['is_active'] = True

    return menu

def sidebar_menu(request):
    sidebar_menu = [{
        'url': '/',
        'icon': 'bi bi-cpu',
        'text': 'Dashboard',
        'name': 'index'
    }, {
        'icon': 'bi bi-gear',
        'text': 'Settings',
        'url': '/settings',
        'name': 'settings'
    },  {
        'icon': 'bi bi-gear',
        'text': 'Product',
        'url': '/product',
        'name': 'product'
    },{
        'icon': 'bi bi-gear',
        'text': 'Finance',
        'url': '/finance',
        'name': 'finance'
    },{
        'url': '/analytics',
        'icon': 'bi bi-bar-chart',
        'text': 'Analytics',
        'name': 'analytics'
    }, {
    'url': '/usermanagement',
    'icon': 'bi bi-people',
    'text': 'User Management',
    'name': 'userManagement',
    'children': [
        {
            'url': '/usermanagement/administrator',
            'text': 'Administrator',
            'name': 'administrator',
            'children': [
                {
                    'url': '/usermanagement/administrator/moderator',
                    'text': 'Moderator',
                    'name': 'moderator'
                },
                {
                    'url': '/usermanagement/administrator/staff',
                    'text': 'Staff',
                    'name': 'staff'
                }
            ]
        },
        {
            'url': '/usermanagement/subscribers',
            'text': 'Subscribers',
            'name': 'subscribers'
        },
        {
            'url': '/usermanagement/businesses',
            'text': 'Businesses',
            'name': 'businesses'
        }
    ]
}, {
    "icon": "bi bi-envelope",
    "text": "Correspondence",
    "children": [
        {
            "url": "/email",
            "text": "Email",
            "name": "email",
            "children": [
                {
                    "url": "/email/style",
                    "text": "Email Style",
                    "name": "emailStyle"
                },
                {
                    "url": "/email/user-fields",
                    "text": "User Fields",
                    "name": "emailUserFields"
                }
            ]
        },
        {
            "url": "/user-fields/block",
            "text": "Block",
            "name": "userFieldsBlock"
        },
        {
            "url": "/user-fields/censor",
            "text": "Censor",
            "name": "userFieldsCensor"
        },
        {
            "url": "/user-fields/require-approval",
            "text": "Require Approval",
            "name": "userFieldsRequireApproval"
        },
        {
            "url": "/user-fields/flag",
            "text": "Flag",
            "name": "userFieldsFlag"
        },
        {
            "url": "/user-fields/replace",
            "text": "Replace",
            "name": "userFieldsReplace"
        },
        {
            "url": "/user-fields/auto-tag",
            "text": "Auto-tag",
            "name": "userFieldsAutoTag"
        }
    ]
},  {
            'icon': 'bi bi-palette',
            'text': 'Design',
            'children': [{
                'url': '/design/customize',
                'text': 'Customize',
                'name': 'designCustomize',
                'children': [
                    {
                        'url': '/design/customize/plugins',
                        'text': 'Plugins',
                        'name': 'designCustomizePlugins'
                    },
                    {
                        'url': '/design/customize/apis',
                        'text': 'APIs',
                        'name': 'designCustomizeAPIs'
                    }
                ]
            }, {
                'url': '/design/thememodes',
                'text': 'Theme Modes',
                'name': 'themeModes'
            }, 
            {
                'url': '/design/text',
                'text': 'Text Input fields',
                'name': 'designText'
            }, {
            'url': '/design/emoji',
            'text': 'Emoji',
            'name': 'designEmoji'
        }, {
            'url': '/design/permalinks',
            'text': 'Permalinks',
            'name': 'designPermalinks'
        }, {
            'url': '/design/embedding',
            'text': 'Embedding',
            'name': 'designEmbedding'
        }, {
            'url': '/design/watched-words',
            'text': 'Watched Words',
            'name': 'designWatchedWords'
        }]
    }, {
        'icon': 'bi bi-shield-lock',
        'text': 'Security',
        "url": "/security",
       
    }, {
    "icon": "bi bi-tools",
    "text": "Maintenance",
    "name": "maintenance",
    "url": "/maintenance",
    "children": [
        {
            "text": "Logs",
            "name": "maintenanceLogs",
            "url": "/maintenance/logs"
        },
        {
            "text": "Backup",
            "name": "backup",
            "url": "/maintenance/backup"
        }
    ]
}, {
        'icon': 'bi bi-headset',
        'text': 'Customer Support',
        'name': 'customerSupport',
        'url': '/support'
    }, {
        'icon': 'bi bi-collection',
        'text': 'Miscellaneous',
        'url': '/miscellaneous'
        
    }]
    
    resolved_path = resolve(request.path_info)
    current_path_name = resolved_path.url_name
    sidebar_menu = mark_active_link(sidebar_menu, current_path_name)

    return {'sidebar_menu': sidebar_menu}