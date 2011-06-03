# -*- coding: utf-8 -*-
#
#  This file is part of django-taggit-autocomplete-modified.
#
#  DESCRIPTION_DESCRIPTION_DESCRIPTION
#
#  Development Web Site:
#    - http://www.codetrax.org/projects/django-taggit-autocomplete-modified
#  Public Source Code Repository:
#    - https://source.codetrax.org/hgroot/django-taggit-autocomplete-modified
#
#  Copyright 2011 George Notaras <gnot [at] g-loaded.eu>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from django.db.models.loading import cache
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError


def list_tags(request):
    Tag = cache.get_model('tagging', 'Tag')
    try:
        tags = Tag.objects.filter(name__istartswith=request.GET['q']).values_list('name', flat=True)
    except MultiValueDictKeyError:
        pass
    return HttpResponse('\n'.join(tags), mimetype='text/plain')


