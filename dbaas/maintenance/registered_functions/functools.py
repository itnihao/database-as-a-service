import sys, inspect
import logging
LOG = logging.getLogger(__name__)

def _is_mod_function(mod, func):
    return inspect.isfunction(func) and inspect.getmodule(func) == mod

def _get_key(item):
    return item[1]

def _get_registered_functions():
    current_module = sys.modules[__name__]
    function_list = ((func.__name__, func.__doc__) for func in current_module.__dict__.itervalues()
            if _is_mod_function(current_module,
                func) and not func.__name__.startswith('_'))

    return sorted(function_list, key=_get_key)


def _get_function(func_name):
    current_module = sys.modules[__name__]
    func_list =  list((func for func in current_module.__dict__.itervalues()
            if _is_mod_function(current_module,func) and func.__name__ ==func_name))

    try:
        func_list = func_list[0]
    except IndexError, e:
        LOG.info("Function not found! {}".format(e))
        return None

    return func_list


def get_hostmane(host_id):
    """Return HOST_NAME"""
    from physical.models import Host
    host = Host.objects.get(id=host_id)
    return host.hostname

def get_infra_name(host_id):
    """Return DATABASE_INFRA_NAME"""
    from physical.models import Host
    host = Host.objects.filter(id=host_id,
        ).select_related('instance').select_related('databaseinfra')

    try:
        host = host[0]
    except IndexError, e:
        LOG.warn("Host id does not exists: {}. {}".format(host_id, e))
        return None


    return host.instance_set.all()[0].databaseinfra.name

def get_database_name(host_id):
    """Return DATABASE_NAME"""
    from physical.models import Host
    host = Host.objects.filter(id=host_id,
        ).select_related('instance',
        ).select_related('databaseinfra',
        ).select_related('database',)

    try:
        host = host[0]
    except IndexError, e:
        LOG.warn("Host id does not exists: {}. {}".format(host_id, e))
        return None

    try:
        database = host.instance_set.all()[0].databaseinfra.databases.all()[0]
    except IndexError, e:
        LOG.warn("There is not a database on this host: {}. {}".format(host_id, e))
        return None

    return database.name


def get_infra_user(host_id):
    """Return DATABASE_INFRA_USER"""
    from physical.models import Host
    host = Host.objects.filter(id=host_id,
        ).select_related('instance').select_related('databaseinfra')

    try:
        host = host[0]
    except IndexError, e:
        LOG.warn("Host id does not exists: {}. {}".format(host_id, e))
        return None


    return host.instance_set.all()[0].databaseinfra.user


def get_infra_password(host_id):
    """Return DATABASE_INFRA_PASSWORD"""
    from physical.models import Host
    host = Host.objects.filter(id=host_id,
        ).select_related('instance').select_related('databaseinfra')

    try:
        host = host[0]
    except IndexError, e:
        LOG.warn("Host id does not exists: {}. {}".format(host_id, e))
        return None


    return host.instance_set.all()[0].databaseinfra.password


def get_host_user(host_id):
    """Return HOST_USER"""
    from physical.models import Host
    host = Host.objects.filter(id=host_id).select_related('cs_host_attributes')

    try:
        host = host[0]
    except IndexError, e:
        LOG.warn("Host id does not exists: {}. {}".format(host_id, e))
        return None

    try:
        host_attr = host.cs_host_attributes.all()[0]
    except IndexError, e:
        LOG.warn("Host id does not own a cs_host_attr: {}. {}".format(host_id, e))
        return None


    return host_attr.vm_user

def get_host_password(host_id):
    """Return HOST_PASSWORD"""
    from physical.models import Host
    host = Host.objects.filter(id=host_id).select_related('cs_host_attributes')

    try:
        host = host[0]
    except IndexError, e:
        LOG.warn("Host id does not exists: {}. {}".format(host_id, e))
        return None

    try:
        host_attr = host.cs_host_attributes.all()[0]
    except IndexError, e:
        LOG.warn("Host id does not own a cs_host_attr: {}. {}".format(host_id, e))
        return None


    return host_attr.vm_password


def get_engine_type_name(host_id):
    """Return ENGINE_TYPE"""
    from physical.models import Host
    host = Host.objects.filter(id=host_id,
        ).select_related('instance',
        ).select_related('databaseinfra',
        )

    try:
        host = host[0]
    except IndexError, e:
        LOG.warn("Host id does not exists: {}. {}".format(host_id, e))
        return None


    return host.instance_set.all()[0].databaseinfra.engine.name
