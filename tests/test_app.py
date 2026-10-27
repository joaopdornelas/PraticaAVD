"""Execute: python -m unittest discover -s tests -v"""
import unittest
from pathlib import Path
from streamlit.testing.v1 import AppTest
from src.data_loader import load_data
from src.filters import filter_data


class FiltersTest(unittest.TestCase):
    def test_two_dashboards_and_shared_filter(self):
        at = AppTest.from_file(str(Path(__file__).resolve().parents[1] / 'app.py'), default_timeout=60).run()
        self.assertEqual(len(at.exception), 0)
        self.assertEqual(len(at.tabs), 2)
        self.assertEqual(at.metric[0].value, '7.786')
        self.assertEqual(at.metric[1].value, '70,1%')
        self.assertEqual(at.metric[2].value, '6,5')
        at.multiselect(key='tipos').set_value(['Série']).run()
        self.assertEqual(at.metric[0].value, '2.410')
        self.assertEqual(at.metric[3].value, '100,0%')
        at.multiselect(key='variaveis').set_value(['imdb_rating', 'imdb_votes']).run()
        at.toggle(key='separar_por_tipo').set_value(True).run()
        at.selectbox(key='distribuicao').set_value('imdb_votes').run()
        at.checkbox(key='hist_log').check().run()
        at.selectbox(key='kpi_group').set_value('primary_country').run()
        at.button(key='clear_categories').click().run()
        self.assertEqual(len(at.exception), 0)

    def test_defaults_preserve_all_titles_and_missing_ratings(self):
        df = load_data()
        result = filter_data(df, ["Filme", "Série"], "release_year", (int(df.release_year.min()), int(df.release_year.max())))
        self.assertEqual(len(result), 7786)
        self.assertEqual(result['imdb_rating'].isna().sum(), 2326)

    def test_missing_values_are_an_explicit_choice(self):
        df = load_data()
        result = filter_data(df, ["Filme", "Série"], "imdb_rating", (8.0, 10.0), False)
        self.assertTrue(result['imdb_rating'].between(8, 10).all())
        included = filter_data(df, ["Filme", "Série"], "imdb_rating", (8.0, 10.0), True)
        self.assertEqual(len(included) - len(result), 2326)
        self.assertEqual(len(df), 7786)

    def test_ui_empty_and_single_variable(self):
        at = AppTest.from_file(str(Path(__file__).resolve().parents[1] / 'app.py'), default_timeout=60).run()
        self.assertEqual(len(at.exception), 0)
        at.multiselect(key='variaveis').set_value([]).run()
        self.assertEqual(len(at.exception), 0)
        self.assertGreaterEqual(len(at.warning), 2)
        at.multiselect(key='variaveis').set_value(['imdb_rating']).run()
        at.selectbox(key='filtro').set_value('imdb_rating').run()
        at.slider(key='intervalo_imdb_rating').set_value((8.0, 9.0)).run()
        at.checkbox(key='manter_ausentes').uncheck().run()
        self.assertEqual(len(at.exception), 0)
        at.multiselect(key='tipos').set_value([]).run()
        self.assertEqual(len(at.exception), 0)
        self.assertTrue(any('Nenhum título' in w.value for w in at.warning))


if __name__ == '__main__':
    unittest.main()
