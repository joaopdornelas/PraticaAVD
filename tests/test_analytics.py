import unittest
import numpy as np
import pandas as pd
from src.analytics import correlation_data, histogram_data, calculate_metrics, category_counts, select_categories, decade_counts
from src.charts import category_bar, heatmap, histogram
from src.data_loader import load_data


class AnalyticsTest(unittest.TestCase):
    def test_pairwise_correlation_and_constant_values(self):
        df = pd.DataFrame({'release_year': [1, 2, 3, np.nan], 'imdb_rating': [3, 2, 1, 9], 'imdb_votes': [1, 1, 1, 1]})
        result = correlation_data(df, ['release_year', 'imdb_rating', 'imdb_votes'])
        pair = result[(result.x == 'Ano de lançamento') & (result.y == 'Nota IMDb')].iloc[0]
        self.assertEqual(pair['n'], 3)
        self.assertEqual(pair.rho, -1)
        self.assertTrue(result.loc[result.x.eq('Votos IMDb'), 'rho'].isna().all())
        heatmap(result, ['release_year', 'imdb_rating', 'imdb_votes']).to_dict(validate=True)

    def test_histograms_share_edges_and_preserve_counts(self):
        df = load_data()
        for log in [False, True]:
            data = histogram_data(df, 'imdb_votes', 25, True, log)
            self.assertEqual(data.quantidade.sum(), 5460)
            self.assertTrue(np.allclose(data.groupby('grupo').percentual.sum(), 100))
            parts = [p for _, p in data.groupby('grupo')]
            self.assertEqual(parts[0].inicio.tolist(), parts[1].inicio.tolist())
            histogram(data, 'imdb_votes', True, log).to_dict(validate=True)
        self.assertTrue(histogram_data(df.iloc[:0], 'imdb_votes').empty)

    def test_metrics_and_cross_filter(self):
        df = load_data()
        metrics = calculate_metrics(df)
        self.assertEqual(metrics['total'], 7786)
        self.assertEqual(metrics['avaliados'], 5460)
        self.assertEqual(metrics['series'], 2410)
        self.assertEqual(metrics['mediana'], 6.5)
        self.assertAlmostEqual(metrics['cobertura'], 5460/7786)
        self.assertAlmostEqual(metrics['proporcao_series'], 2410/7786)
        selected = select_categories(df, 'primary_genre', [{'categoria': 'Dramas'}, {'categoria': 'Comedies'}])
        self.assertEqual(len(selected), df.primary_genre.isin(['Dramas', 'Comedies']).sum())
        self.assertEqual(decade_counts(selected).titulos.sum(), len(selected))
        self.assertEqual(len(select_categories(df, 'primary_genre', [])), len(df))
        empty = calculate_metrics(df.iloc[:0])
        self.assertEqual(empty['total'], 0)
        self.assertIsNone(empty['cobertura'])
        self.assertIsNone(empty['proporcao_series'])
        missing = calculate_metrics(df[df.imdb_rating.isna()])
        self.assertEqual(missing['cobertura'], 0)
        self.assertIsNone(missing['mediana'])
        spec = category_bar(category_counts(df, 'primary_genre')).to_dict(validate=True)
        self.assertEqual(spec['params'][0]['name'], 'categorias')


if __name__ == '__main__':
    unittest.main()
