# what are nodes and why use them?
# they become useful when the allocation of memory can not sture data in a continuous block of memory
# pointers are a data structure allow current data element to link to the next element

# how to create nodes?

class Topics:
    def __init__(self, topicval=None):
        self.topicval = topicval
        self.nextval = None


topic1 = Topics("psychology")
topic2 = Topics("biology")
topic3 = Topics("economics")
topic4 = Topics("computer science")

topic1.nextval = topic3
topic3.nextval = topic2
topic2.nextval = topic4

# how to traverse node elements?
# first create a variable to store the first element for traverse
# then use a while loop to print all the other elements

this_topic = topic1

while this_topic:
    print(this_topic.topicval)
    this_topic = this_topic.nextval


