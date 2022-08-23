CHANGE_ME = '[CHANGE_ME]'
DEFAULT_DATAKITCHEN_URL = 'https://cloud.datakitchen.io'
KITCHEN = 'kitchen'
KITCHEN_STAFF = 'kitchen-staff'
RECIPE = 'recipe'
VARIATION = 'variation'
PARAMETERS = 'parameters'
ORDER_ID = 'order_id'
ORDER_RUN_ID = 'order_run_id'
ORDER_RUN_STATUS = 'order_run_status'
RECIPE_OVERRIDES = 'recipeoverrides'
PARENT_KITCHEN = 'parent-kitchen'

# API HTTP Request Methods
API_DELETE = 'delete'
API_GET = 'get'
API_POST = 'post'
API_PUT = 'put'

# Order status options
ACTIVE_ORDER = 'ACTIVE_ORDER'
COMPLETED_ORDER = 'COMPLETED_ORDER'
STOPPED_ORDER = 'STOPPED_ORDER'
ORDER_ERROR = 'ORDER_ERROR'
PAUSED_ORDER = 'PAUSED_ORDER'
INACTIVE_ORDER_STATUS_TYPES = [COMPLETED_ORDER, STOPPED_ORDER, ORDER_ERROR]

# Order run status options
PLANNED_SERVING = 'PLANNED_SERVING'
ACTIVE_SERVING = 'ACTIVE_SERVING'
COMPLETED_SERVING = 'COMPLETED_SERVING'
STOPPED_SERVING = 'STOPPED_SERVING'
SERVING_ERROR = 'SERVING_ERROR'
SERVING_RERAN = 'SERVING_RERAN'
STOPPED_STATUS_TYPES = [COMPLETED_SERVING, STOPPED_SERVING, SERVING_ERROR, SERVING_RERAN]

# DataKitchen Tests
VALID_TEST_DIRECTORIES = ['actions', 'data_sources', 'data_sinks']

# Vault
DEFAULT_VAULT_URL = 'https://vault2.datakitchen.io:8200'
GLOBAL = '**__GLOBAL__**'

# GMail API
GMAIL_APPROVAL_STRING = "Approved"
GMAIL_SLEEP_SECONDS = 10
GMAIL_MAX_WAIT_SECONDS = 30
