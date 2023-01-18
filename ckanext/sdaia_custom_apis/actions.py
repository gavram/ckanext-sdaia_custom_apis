import ckan.plugins.toolkit as toolkit

@toolkit.side_effect_free
def recently_updated_datasets(context, data_dict):
    """Return the 5 most recently updated datasets."""
    
    # Perform a search for packages, sorted by the metadata_modified field in descending order
    # and return the first 5 results.
    search_results = toolkit.get_action("package_search")(context, {"sort": "metadata_modified desc", "rows": 5})
    return search_results["results"]


@toolkit.side_effect_free
def get_organization_datasets(context, data_dict):
    """Return all datasets that belongs to organization."""
    
    org_dict = toolkit.get_action("organization_show")(context, data_dict)
    
    if org_dict["name"] == data_dict["id"]:
        id = org_dict["id"]
    else:
        id = data_dict["id"]
    
    search_dict = {}
    search_dict["fq"] = "owner_org:" + id
    search_results = toolkit.get_action("package_search")(context, search_dict)
    return search_results["results"]

@toolkit.side_effect_free
def get_groups_datasets(context, data_dict):
    """Return all datasets that belongs to group."""
    
    group_dict = toolkit.get_action("group_show")(context, data_dict)
    if group_dict["name"] == data_dict["id"]:
        id = group_dict["id"]
    else:
        id = data_dict["id"]
    
    search_dict = {}
    search_dict["fq"] = "groups:" + id
    search_results = toolkit.get_action("package_search")(context, search_dict)
    return search_results["results"]

@toolkit.side_effect_free
def organizations_user_list(context, data_dict):
    """Returns all organization user's display names and capacity"""

    org_dict = toolkit.get_action("organization_show")(context, data_dict)
    user_list = org_dict["users"]
    new_list = []

    # We want to return only display names and capacity
    for user in user_list:
        new_list.append({
            "name": user["display_name"],
            "capacity": user["capacity"]
        })
    
    return new_list