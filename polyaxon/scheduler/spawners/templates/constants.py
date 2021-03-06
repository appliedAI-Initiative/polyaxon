DEFAULT_PORT = 2222
ENV_VAR_TEMPLATE = '{name: "{var_name}", value: "{var_value}"}'
VOLUME_CLAIM_NAME = 'plx-pvc-{vol_name}'
CONFIG_MAP_NAME = 'plx-config-{uuid}'
SECRET_NAME = 'plx-secret-{uuid}'  # noqa, secret
CONFIG_MAP_CLUSTER_KEY_NAME = 'POLYAXON_CLUSTER'
CONFIG_MAP_DECLARATIONS_KEY_NAME = 'POLYAXON_DECLARATIONS'
CONFIG_MAP_EXPERIMENT_INFO_KEY_NAME = 'POLYAXON_EXPERIMENT_INFO'
CONFIG_MAP_JOB_INFO_KEY_NAME = 'POLYAXON_JOB_INFO'
CONFIG_MAP_NOTEBOOK_INFO_KEY_NAME = 'POLYAXON_NOTEBOOK_INFO'
CONFIG_MAP_TENSORBOARD_INFO_KEY_NAME = 'POLYAXON_TENSORBOARD_INFO'
CONFIG_MAP_TASK_INFO_KEY_NAME = 'POLYAXON_TASK_INFO'
CONFIG_MAP_LOG_LEVEL_KEY_NAME = 'POLYAXON_LOG_LEVEL'
CONFIG_MAP_REFS_OUTPUTS_PATHS_KEY_NAME = 'POLYAXON_REFS_OUTPUTS_PATHS'
CONFIG_MAP_RUN_OUTPUTS_PATH_KEY_NAME = 'POLYAXON_RUN_OUTPUTS_PATH'
CONFIG_MAP_RUN_LOGS_PATH_KEY_NAME = 'POLYAXON_LOGS_PATH'
CONFIG_MAP_RUN_DATA_PATHS_KEY_NAME = 'POLYAXON_RUN_DATA_PATHS'
CONFIG_MAP_RUN_STORES_ACCESS_KEYS = 'POLYSTORES_RUN_STORES_ACCESS_KEYS'
CONFIG_MAP_IN_CLUSTER = 'POLYAXON_IN_CLUSTER'
CONFIG_MAP_IS_MANAGED = 'POLYAXON_IS_MANAGED'
CONFIG_MAP_API_VERSION = 'POLYAXON_API_VERSION'
CONFIG_MAP_INTERNAL_HEADER = 'POLYAXON_INTERNAL_HEADER'
CONFIG_MAP_INTERNAL_HEADER_SERVICE = 'POLYAXON_INTERNAL_HEADER_SERVICE'
SECRET_USER_TOKEN = 'POLYAXON_SECRET_USER_TOKEN'  # noqa, secret
SECRET_EPHEMERAL_TOKEN = 'POLYAXON_SECRET_EPHEMERAL_TOKEN'  # noqa, secret

REPOS_VOLUME = 'repos'
DOCKER_VOLUME = 'docker'
DOCKER_MOUNT_PATHS = '/var/run/docker.sock'
BUILD_CONTEXT_VOLUME = 'build-context'
AUTH_CONTEXT_VOLUME = 'auth-context'
SHM_VOLUME = 'shm'
BUILD_CONTEXT = '/plx-build'
AUTH_CONTEXT = '/plx-context'
