from spaceone.core.error import *


class ERROR_SAME_RESPONDER_ALREADY_EXISTS(ERROR_INVALID_ARGUMENT):
    _message = 'The same responder already exists. (resource_type = {resource_type}, resource_id = {resource_id})'


class ERROR_RESPONDER_NOT_EXIST(ERROR_INVALID_ARGUMENT):
    _message = 'Responder does not exist. (resource_type = {resource_type}, resource_id = {resource_id})'


class ERROR_SAME_PROJECT_DEPENDENCY_ALREADY_EXISTS(ERROR_INVALID_ARGUMENT):
    _message = 'The same project already exists. (project_id = {project_id})'


class ERROR_PROJECT_DEPENDENCY_NOT_EXIST(ERROR_INVALID_ARGUMENT):
    _message = 'Project does not exist. (project_id = {project_id})'

