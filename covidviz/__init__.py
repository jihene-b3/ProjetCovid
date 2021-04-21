__version__ = '0.0.1'

from .io.load_db import Load_db
from .covidmap.plot_map import Map_covid
from .preprocess.format_granu import format_granularity
from .preprocess.clean_df import choose_columns, choose_granularity
from .icu.link_dep_reg import link_dep_reg
from .screening.plot_map import map_dep, map_screening
from .screening.graphs import daily_test, daily_test_age, daily_test_dep
