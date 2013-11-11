# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import factory
from .. import models


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.AccountUser

    username = factory.Sequence(lambda n: 'user_{0}'.format(n))
    email = factory.Sequence(lambda n: 'user_{0}@email.test.com'.format(n))





