# Copyright (C) 2018 Intel Corporation
#
# SPDX-License-Identifier: MIT

from cvat.settings.base import JS_3RDPARTY

JS_3RDPARTY['engine'] = JS_3RDPARTY.get('engine', []) + ['someapp/js/enginePlugin.js']
