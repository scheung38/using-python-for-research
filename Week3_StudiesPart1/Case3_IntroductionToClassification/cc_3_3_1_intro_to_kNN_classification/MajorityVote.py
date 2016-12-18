import random
import scipy.stats as ss


def majority_vote(votes):
    """
    :param votes: input string
    :return: the frequency count of each word
    """
    vote_counts = {}

    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1

    winners = []
    max_count = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)

    return random.choice(winners)


def majority_vote_short(votes):
    """
    :param votes:
    :return: the most common element in votes
    """
    mode, count = ss.mstats.mode(votes)
    return mode


votes = [1, 2, 3, 1, 2, 3, 1, 2, 3, 3, 3, 3, 2, 2, 2]

vote_counts = majority_vote(votes)

if __name__ == '__main__':
    vote_counts = majority_vote_short(votes)
    print(vote_counts)

    print(vote_counts)
    # {1: 3, 2: 3, 3: 6}
    # the number 3 occurred 4 time

    print(max(vote_counts))
    # 3

    # same as
    print(max(vote_counts.keys()))
    # 3

    print(max(vote_counts.values()))
    # 6







    # 3.3.3 Majority Vote
    # What does the items method for dictionaries return?
    # A dict_items object with elements consisting of tuples of key, value pairs


    # What will random.choice() return for a list containing only one object? (Assume that the random module has already been imported.)
    # This code returns the single element every time.


    # 3.3.4
    # For an np.array of dimension 2, what does the shape method return?
    # A tuple containing the number of rows and columns

    # What does np.argsort do?
    # It sorts an array according to a single argument and returns the sorted indices

    # 3.3.5: Generating Synthetic Data

    # What does np.concatenate do?
    # Takes in a tuple of np.arrays and joins them lengthwise along the specified axis


    # Do you expect the k-Nearest Neighbors to categorize new values in the synthetic data perfectly?
    # No, because the data contain some observations with a majority of neighbors in another category.

    # 3.3.6
    # What does np.arange do?
    # Creates regularly spaced values between the first and second argument, with spacing given in the third argument

    # What does enumerate do?
    # Takes an iterable and returns a new iterable with tuples as elements, where the first index of each tuple is the index of the tuple in the iterable

    # 3.3.8: Applying the kNN Method
    # What are the four variables in the iris dataset described in Video 3.3.8?
    # Sepal length, sepal width, petal length, petal width

    # How many different species are contained in the iris dataset described in Video 3.3.8?
    # 3

    # How often do the predictions from the homemade and scikit-learn kNN classifiers accurately predict the class of the data in the iris dataset described in Video 3.3.8?
    # Approximately 85% of the time correct
