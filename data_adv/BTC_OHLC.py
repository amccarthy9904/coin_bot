"""BTC_OHLC dataset."""

import tensorflow_datasets as tfds

# TODO(BTC_OHLC): Markdown description  that will appear on the catalog page.
_DESCRIPTION = """
Description is **formatted** as markdown.

It should also contain any processing which has been applied (if any),
(e.g. corrupted example skipped, images cropped,...):
"""

# TODO(BTC_OHLC): BibTeX citation
_CITATION = """
"""


class BtcOhlc(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for BTC_OHLC dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # Date,Open,High,Low,Close,Adj Close,Volume
            'open': tfds.features.Text(),
            'high': tfds.features.Text(),
            'low': tfds.features.Text(),
            'close': tfds.features.Text(),
            'volume': tfds.features.Text(),
            'up_down_label': tfds.features.ClassLabel(names=['up', 'down'])
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=('image', 'label'),  # Set to `None` to disable
        disable_shuffling=False,
        homepage='https://dataset-homepage/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # TODO(BTC_OHLC): Downloads the data and defines the splits
    path = dl_manager.download_and_extract('https://todo-data-url')

    # TODO(BTC_OHLC): Returns the Dict[split names, Iterator[Key, Example]]
    return {
        'train': self._generate_examples(path / 'train_imgs'),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    # TODO(BTC_OHLC): Yields (key, example) tuples from the dataset
    for f in path.glob('*.jpeg'):
      yield 'key', {
          'image': f,
          'label': 'yes',
      }
