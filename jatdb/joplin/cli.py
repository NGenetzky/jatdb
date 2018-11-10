""" CLI for Joplin subpackage
"""

import argparse
import logging
import os
import sys

# This is currently a special frontmatter package that has 'joplin-support'
import frontmatter

logging.basicConfig(filename='jatdb.log', level=logging.INFO)
log = logging.getLogger(__name__)


def frontmatter_load(filename):
    with open(filename) as fd:
        return frontmatter.load(fd=fd)


def frontmatter_dump(post, filename):
    post.handler = frontmatter.YAMLHandler()
    with open(filename, 'w') as fd:
        return frontmatter.dump(post, fd)


def note_handler(post, outdir):
    notedir = os.path.join(outdir, post['parent_id'], post['id'])
    if not os.path.isdir(notedir):
        os.makedirs(notedir)
    # log.info('{0}/{1}'.format(post['parent_id'], post['id']))
    frontmatter_dump(post, os.path.join(notedir, 'index.md'))


def content_handler(filename, outdir):
    log.debug(filename)
    post = frontmatter_load(filename)
    if post['type_'] is 1:
        note_handler(post, outdir)
    else:
        log.info('pass {0} -> {1}'.format(filename, post['id']))
        pass


def find_files_in_sync(syncdir, outdir):
    if not os.path.exists(syncdir + '.resource'):
        raise ValueError("Directory({0}) does not appear to be sync dir")

    for root, dirs, files in os.walk(syncdir):
        print(root)
        if root == syncdir:
            for f in files:
                content_handler(root + f, outdir)
        elif root == syncdir + '.resource':
            pass
        else:
            pass


def parse_args(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sync', type=str, help='Joplin sync directory')
    parser.add_argument('--out', type=str, help='Output directory')
    return parser.parse_args()


def main(argv=None):
    args = parse_args(argv)

    if (args.sync is not None and args.out is not None):
        find_files_in_sync(args.sync, args.out)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
