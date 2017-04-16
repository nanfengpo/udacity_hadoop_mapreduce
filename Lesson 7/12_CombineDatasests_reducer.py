#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

def reducer():
    users = dict()
    posts = dict()
    for line in sys.stdin:
        data = line.strip().split("\t")

        if data[1] == "A":
            user_id, type, reputation, gold, silver, bronze = data
            users[user_id] = [reputation, gold, silver, bronze]
        elif data[1] == "B":
            author_id, type, id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score = data
            posts[id] = [id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score]

    for post_id in posts:
        id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score = posts[post_id]
        reputation, gold, silver, bronze = users[author_id]
        print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score, reputation, gold, silver, bronze)

def main():
    reducer()

if __name__ == '__main__':
    main()
