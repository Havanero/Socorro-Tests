#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.home_page import CrashStatsHomePage
from unittestzero import Assert


class TestLayout:

    @pytest.mark.nondestructive
    def test_that_products_are_sorted_correctly(self, mozwebqa):

        csp = CrashStatsHomePage(mozwebqa)

        product_list = ['Firefox',
                        'Thunderbird',
                        'Fennec',
                        'FennecAndroid',
                        'SeaMonkey',
                        'WebappRuntime',
                        'B2G',
                        'WebappRuntimeMobile',
                        'MetroFirefox']
        products = csp.header.product_list
        Assert.equal(product_list, products)

    @pytest.mark.xfail(reason='Bug 934910 - [stage][prod] Current versions are not listed in the right order')
    @pytest.mark.nondestructive
    def test_that_product_versions_are_ordered_correctly(self, mozwebqa):
        csp = CrashStatsHomePage(mozwebqa)

        Assert.is_sorted_descending(csp.header.current_versions)
        Assert.is_sorted_descending(csp.header.other_versions)
