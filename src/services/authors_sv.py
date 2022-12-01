from init_app import db
from src.const import *
from src.models.authors_md import Authors
from src.models.subscription_md import Subscription
from src.utils import is_similar


def search_by_name(query):
    all_authors = Authors.query.all()
    result = []
    for author in all_authors:
        if is_similar(author.author_name, query):
            result.append(author.get_json())
    if len(result) == 0:
        return None, NOT_FOUND
    return result, OK_STATUS


def get_follower_list(author_id):
    subs = Subscription.query.filter_by(author_id=author_id)
    followers = []
    for sub in subs:
        followers.append(sub.username)


def get_info(author_id):
    author = Authors.query.get(author_id)
    if author is None:
        return None, NOT_FOUND

    result = author.get_json()
    result["followers"] = get_follower_list(author_id)
    return result, OK_STATUS


def add_author(author_info):
    new_author = Authors()

    if new_author.update_author_name(author_info["author_name"]):
        new_author.update_bio(author_info["bio"])
        new_author.update_profile_pic(author_info[PROFILE_PIC])
        new_author.update_social_account(author_info["social_account"])
        new_author.update_website(author_info["website"])

        db.session.add(new_author)
        db.session.commit()

        return new_author.get_json(), OK_STATUS

    return None, BAD_REQUEST
