# -*- coding: utf-8 -*-

# The parametrize function is generated, so this doesn't work:
#
#     from pytest.mark import parametrize
#
import pytest
parametrize = pytest.mark.parametrize

from duckomatic.utils.resource import (Resource)


class TestResource(object):

    @parametrize('value, min_value, max_value, expected', [
        (0, 0, 10, 0),
        (3, 0, 10, 3),
        (5, 0, 10, 5),
        (10, 0, 10, 10),
        (-1, 0, 10, 0),
        (11, 0, 10, 10)
    ])
    def test_validate_value(self, value, min_value, max_value, expected):
        assert Resource.validate_value(
            'Label', value, min_value, max_value) == expected

    @parametrize('value, min_source_value, max_source_value, target_min, \
        target_max, expected', [
        (0, 0, 10, 100, 1000, 100),
        (3, 0, 10, 100, 1000, 370),
        (5, 0, 10, 100, 1000, 550),
        (10, 0, 10, 100, 1000, 1000),
        (-5, -5, 5, 245, 492, 245),
        (0, -5, 5, 245, 492, 368),
        (5, -5, 5, 245, 492, 492),
    ])
    def test_scale_value(self, value, min_source_value, max_source_value,
                         target_min, target_max, expected):
        assert Resource.scale_value(
            value, min_source_value, max_source_value, target_min,
            target_max) == expected
