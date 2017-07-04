import csv
import numpy as np


def convert_to_one_hot(raw_target):
    n_uniques = len(np.unique(raw_target))
    one_hot_target = np.zeros((raw_target.shape[0], n_uniques))
    one_hot_target[np.arange(raw_target.shape[0]), raw_target.astype(np.int)] = 1
    return one_hot_target

def load_fer(dataset = 0, one_hot = True, flat = True):
    '''
    Loads the FER Dataset from memory and returns the dataset.
    The fer2013.csv file needs to be extracted and placed under data/fer2013.csv. The labels can be converted
    to one-hot encoding.

    :param dataset: selects which dataset to load - 0 = Train, 1 = Validation, 2 = Test
    :param one_hot: True returns the labels as one hot encoding
    :return: A dict with `data` and `target` keys.
    '''

    dest_file = 'utils/data/fer2013.csv'
    delimiter = ','
    firstline = True
    i = 0
    training_labels = []
    training_images = []
    validation_labels = []
    validation_images = []
    test_labels = []
    test_images = []
    with open(dest_file, 'r') as dest_f:
        data_iter = csv.reader(dest_f,
                            delimiter = delimiter,
                            quotechar = '"')
        for data in data_iter:
            i += 1
            if firstline:
                firstline = False
                continue
            elif i < 28710:
                training_labels.append(float(data[0]))
                if flat:
                    training_images.append(np.fromstring(data[1], dtype=int, sep=' '))
                else:
                    training_images.append(np.reshape(np.fromstring(data[1], dtype=int, sep=' '),[48,48]))
            elif i < 32299:
                validation_labels.append(float(data[0]))
                if flat:
                    validation_images.append(np.fromstring(data[1], dtype=int, sep=' '))
                else:
                    validation_images.append(np.reshape(np.fromstring(data[1], dtype=int, sep=' '), [48, 48]))
            else:
                test_labels.append(float(data[0]))
                if flat:
                    test_images.append(np.fromstring(data[1], dtype=int, sep=' '))
                else:
                    test_images.append(np.reshape(np.fromstring(data[1], dtype=int, sep=' '), [48, 48]))


    if dataset == 0:
        training_images = np.asarray(training_images)
        training_labels = np.asarray(training_labels)
        if one_hot:
            training_labels = convert_to_one_hot(training_labels)
        fer = {'data': training_images, 'target': training_labels}
    elif dataset == 1:
        validation_images = np.asarray(validation_images)
        validation_labels = np.asarray(validation_labels)
        if one_hot:
            validation_labels = convert_to_one_hot(validation_labels)
        fer = {'data': validation_images, 'target': validation_labels}
    else:
        test_images = np.asarray(test_images)
        test_labels = np.asarray(test_labels)
        if one_hot:
            test_labels = convert_to_one_hot(test_labels)
        fer = {'data': test_images, 'target': test_labels}

    return fer