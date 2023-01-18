import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.sdaia_custom_apis.actions import get_organization_datasets, recently_updated_datasets, get_groups_datasets, organizations_user_list
# from ckanext.sdaia_custom_apis.actions import get_organization_datasets

class SdaiaCustomApisPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IActions)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'sdaia_custom_apis')

    # IActions
    def get_actions(self):
        # Register the custom action
        return  {
                    "recently_updated_datasets": recently_updated_datasets,
                    "get_organization_datasets": get_organization_datasets,
                    "get_groups_datasets": get_groups_datasets,
                    "organizations_user_list": organizations_user_list
                }

