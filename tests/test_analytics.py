# [IA] ChatGPT/Codex - testes dos cálculos, histogramas e seleção de categorias.
import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.analytics import correlation_matrix, calculate_metrics, category_counts, select_categories, category_coverage, rating_summary
from src.charts import category_bar, heatmap, histogram, coverage_bar, rating_boxplot
from src.data_loader import load_data


class AnalyticsTest(unittest.TestCase):
    def test_rating_summary_preserves_missing_and_empty_groups(self):
        df = pd.DataFrame({'tipo_conteudo': ['Filme', 'Filme', 'Filme', 'Série'],
                           'imdb_rating': [6.0, 8.0, np.nan, np.nan]})
        summary = rating_summary(df).set_index('tipo_conteudo')
        self.assertEqual(summary.loc['Filme', 'mediana'], 7.0)
        self.assertEqual(summary.loc['Filme', 'total'], 3)
        self.assertAlmostEqual(summary.loc['Filme', 'cobertura'], 2 / 3)
        self.assertTrue(pd.isna(summary.loc['Série', 'mediana']))
        self.assertEqual(summary.loc['Série', 'cobertura'], 0)
        self.assertTrue(rating_summary(df.iloc[:0]).empty)
        spec = rating_boxplot(df).to_dict(validate=True)
        self.assertEqual(spec['mark']['type'], 'boxplot')
        self.assertEqual(spec['encoding']['y']['scale']['domain'], [0, 10])

    def test_category_coverage_keeps_unrated_titles_and_unknown_categories(self):
        df = pd.DataFrame({'primary_genre': ['A', 'A', 'B', None],
                           'imdb_rating': [6.0, np.nan, np.nan, 8.0]})
        result = category_coverage(df, 'primary_genre').set_index('categoria')
        self.assertEqual(result.loc['A', 'total'], 2)
        self.assertEqual(result.loc['A', 'avaliados'], 1)
        self.assertEqual(result.loc['A', 'cobertura'], 0.5)
        self.assertEqual(result.loc['B', 'cobertura'], 0)
        self.assertEqual(result.loc['Não informado', 'cobertura'], 1)
        self.assertTrue(category_coverage(df.iloc[:0], 'primary_genre').empty)
        self.assertEqual(category_coverage(df, 'primary_genre', limit=1).categoria.tolist(), ['A'])
        coverage_bar(result.reset_index()).to_dict(validate=True)

    def test_boxplot_keeps_all_available_ratings(self):
        df = load_data()
        spec = rating_boxplot(df).to_dict(validate=True)
        values = spec['datasets'][spec['data']['name']] if 'name' in spec['data'] else spec['data']['values']
        self.assertEqual(len(values), 5460)
        self.assertEqual(sorted(row['imdb_rating'] for row in values), sorted(df.imdb_rating.dropna()))
        self.assertEqual(spec['mark']['extent'], 1.5)
        self.assertFalse(plt.get_fignums())

    def test_pairwise_correlation_and_constant_values(self):
        df = pd.DataFrame({'release_year': [1, 2, 3, np.nan], 'imdb_rating': [3, 2, 1, 9], 'imdb_votes': [1, 1, 1, 1]})
        result = correlation_matrix(df, ['release_year', 'imdb_rating', 'imdb_votes'])
        self.assertEqual(result.loc['release_year', 'imdb_rating'], -1)
        self.assertTrue(result['imdb_votes'].isna().all())
        fig = heatmap(result)
        fig.canvas.draw()
        plt.close(fig)

    def test_histograms_share_edges_and_preserve_counts(self):
        df = load_data()
        for log in [False, True]:
            fig = histogram(df, 'imdb_votes', 25, False, log)
            self.assertEqual(sum(bar.get_height() for bar in fig.axes[0].patches), 5460)
            plt.close(fig)
            fig = histogram(df, 'imdb_votes', 25, True, log)
            groups = fig.axes[0].containers
            self.assertEqual(len(groups), 2)
            for bars in groups:
                self.assertAlmostEqual(sum(bar.get_height() for bar in bars), 100)
            self.assertEqual([bar.get_x() for bar in groups[0]], [bar.get_x() for bar in groups[1]])
            plt.close(fig)

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
        coverage = category_coverage(selected, 'primary_genre')
        self.assertEqual(coverage.total.sum(), len(selected))
        self.assertEqual(coverage.avaliados.sum(), selected.imdb_rating.notna().sum())
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
