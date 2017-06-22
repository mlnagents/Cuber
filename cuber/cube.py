import abc
import cPickle as pickle
import os.path
import logging

logger = logging.getLogger(__name__)

class Cube(object):
    __metaclass__  = abc.ABCMeta

    @abc.abstractmethod
    def name(self):
        return

    def get(self):
        pickle_name = 'checkpoints/{}.pkl'.format(self.name())
        logger.info('Pickle name: {}'.format(pickle_name))
        if not os.path.isfile(pickle_name):
            logger.info('Cache is not ok. Evaluating...')
            data = self.eval()
            logger.info('Writing cache')
            with open(pickle_name, 'wb') as f:
                pickle.dump(data, f)
        else:
            logger.info('Cache is ok')
        logger.info('Loading from cache')
        with open(pickle_name, 'rb') as f:
            data = pickle.load(f)
        logger.info('Loaded')
        return data

    @abc.abstractmethod
    def eval(self):
        return