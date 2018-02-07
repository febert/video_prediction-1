from .base_dataset import BaseVideoDataset
from.base_dataset import VideoDataset, SequenceExampleVideoDataset
from .google_robot_dataset import GoogleRobotVideoDataset
from .sv2_dataset import SV2PVideoDataset
from .softmotion_dataset import SoftmotionVideoDataset
from .kth_dataset import KTHVideoDataset


def get_dataset_class(dataset):
    dataset_mappings = {
        'google_robot': 'GoogleRobotVideoDataset',
        'sv2p': 'SV2PVideoDataset',
        'softmotion': 'SoftmotionVideoDataset',
        'kth': 'KTHVideoDataset',
    }
    dataset_class = dataset_mappings.get(dataset, dataset)
    dataset_class = globals().get(dataset_class)
    if dataset_class is None or not issubclass(dataset_class, BaseVideoDataset):
        raise ValueError('Invalid dataset %s' % dataset)
    return dataset_class