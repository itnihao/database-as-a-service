# -*- coding: utf-8 -*-
import logging
from . import start_vm
from . import stop_vm
from ...util.base import BaseStep

LOG = logging.getLogger(__name__)

class StartVM(BaseStep):
    def __unicode__(self):
        return "Starting VMs..."

    def do(self, workflow_dict):
        return start_vm(workflow_dict)

    def undo(self, workflow_dict):
        return stop_vm(workflow_dict)
