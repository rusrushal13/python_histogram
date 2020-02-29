from collections import OrderedDict
from constants import INTEGER_ONE
from utilities import (fetch_inputs,
                       fetch_min_max_bucket_sizes,
                       count_in_between,
                       show_histogram)


def print_histogram():
    """
    Print the histogram.

    ARGS:
    """
    comma_seperated_inputs, bucket_size = fetch_inputs()
    min_bucket_size, max_bucket_size = fetch_min_max_bucket_sizes(
        comma_seperated_inputs, bucket_size)
    print(min_bucket_size, max_bucket_size)
    result_histogram = []

    for element in range(min_bucket_size, max_bucket_size * bucket_size,
                         bucket_size):
        key = '{} to {}'.format(
            element,
            bucket_size + element - INTEGER_ONE)
        value = count_in_between(
            comma_seperated_inputs, element,
            element + bucket_size)

        result_histogram.append([key, value])

    show_histogram(result_histogram)


if __name__ == '__main__':
    print_histogram()
