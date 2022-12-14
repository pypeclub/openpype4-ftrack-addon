# Name of attribute on server where ftrack related info is stored
FTRACK_ID_ATTRIB = "ftrackId"
FTRACK_PATH_ATTRIB = "ftrackPath"
REMOVED_ID_VALUE = "removed"

# Custom attribute where server id is stored
CUST_ATTR_KEY_SERVER_ID = "ayon_id"
CUST_ATTR_KEY_SERVER_PATH = "ayon_path"
CUST_ATTR_KEY_SYNC_FAIL = "ayon_sync_failed"

# Group which marks custom attribute to synchronize
CUST_ATTR_GROUP = "ayon"

# Project custom attribute which define if project should be auto-synced
CUST_ATTR_AUTO_SYNC = "auto_sync_enabled"
CUST_ATTR_AUTO_SYNC = "avalon_auto_sync" # TODO remove this line


FPS_KEYS = {
    "fps",
    "fps_string"
}

# TODO these are applications addon specific
# - maybe should be handled by applications?
# Applications custom attribute name
CUST_ATTR_APPLICATIONS = "applications"
# Environment tools custom attribute
CUST_ATTR_TOOLS = "tools_env"
