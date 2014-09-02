from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import pandas as pd

from .position import position
from .collide import collide, pos_dodge
from ..utils import check_required_aesthetics


class position_dodge(position):

    def adjust(self, data):
        if len(data) == 0:
            return pd.DataFrame()

        check_required_aesthetics(
            ['x'], data.columns, "position_dodge")

        width = data['width'] if 'width' in data else None
        return collide(data, width=width,
                       name='position_dodge',
                       strategy=pos_dodge)