from datetime import date
from django.http import Http404
from django.shortcuts import render

posts_data = [
    {
        "slug": "the-world-keeps-turning",
        "image": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=900&q=80",
        "author": "Aman",
        "date": date(2024, 7, 2),
        "title": "The World Keeps Turning",
        "excerpt": "Even through our hardest days, the world keeps moving and gives us another chance to begin.",
        "content": """
            The world does not pause when we are tired or grieving. Morning still arrives,
            rivers keep finding their way to the sea, and strangers carry on with stories
            of their own. At first that can feel cruel. In time, it can also be a quiet
            promise: pain is real, but it is not the whole world. We can take one small
            step and let the day meet us there.
        """,
    },
    {
        "slug": "meaning-in-small-things",
        "image": "https://images.unsplash.com/photo-1490730141103-6cac27aaab94?auto=format&fit=crop&w=900&q=80",
        "author": "Aman",
        "date": date(2024, 7, 5),
        "title": "Meaning in Small Things",
        "excerpt": "A life does not need grand answers to be meaningful; sometimes care is enough.",
        "content": """
            We often look for meaning as if it were a distant place we must reach.
            But it can live in ordinary acts: listening without rushing, tending a
            plant, sharing food, or showing up for someone who feels alone. These
            moments may not solve every problem, yet they remind us that our presence
            matters. Meaning is sometimes something we make together, one small kindness
            at a time.
        """,
    },
    {
        "slug": "when-life-feels-heavy",
        "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=900&q=80",
        "author": "Aman",
        "date": date(2024, 7, 8),
        "title": "When Life Feels Heavy",
        "excerpt": "Some seasons ask us to move slowly, and that is still a way of moving forward.",
        "content": """
            There are days when even simple tasks seem to carry the weight of the
            world. On those days, strength may look less like pushing onward and more
            like resting, asking for help, or doing only what is possible. Hard seasons
            can narrow our view until tomorrow feels unreachable. We do not have to
            understand the whole road today; finding the next safe step is enough.
        """,
    },
    {
        "slug": "the-kindness-of-being-human",
        "image": "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?auto=format&fit=crop&w=900&q=80",
        "author": "Aman",
        "date": date(2024, 7, 11),
        "title": "The Kindness of Being Human",
        "excerpt": "We all carry unseen struggles, and a little patience can make the world gentler.",
        "content": """
            Every person we pass is living through a life we cannot fully see. Some
            carry regret, some worry about what comes next, and some are simply trying
            to get through today. Remembering this does not excuse harm, but it can
            soften our first judgment. Patience gives people room to be imperfect,
            including ourselves. In a difficult world, compassion is not weakness;
            it is a way of making room for one another.
        """,
    },
    {
        "slug": "learning-to-live-with-loss",
        "image": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=900&q=80",
        "author": "Aman",
        "date": date(2024, 7, 14),
        "title": "Learning to Live with Loss",
        "excerpt": "Loss changes the shape of life, but love can remain part of the story.",
        "content": """
            Grief rarely follows a straight line. It can return in familiar songs,
            quiet rooms, and ordinary dates on the calendar. We may wish to leave it
            behind, but sometimes healing means learning how to carry it without letting
            it carry everything. The people and moments we miss helped shape who we
            are. Remembering them can hurt, and it can also be a way of keeping love
            present in a changed life.
        """,
    },
    {
        "slug": "hope-without-certainty",
        "image": "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=900&q=80",
        "author": "Aman",
        "date": date(2024, 7, 17),
        "title": "Hope Without Certainty",
        "excerpt": "Hope is not a promise that everything will be easy; it is room for possibility.",
        "content": """
            Hope does not require us to pretend that the world is fair or that every
            sorrow has a simple answer. It can be quieter than that: the willingness
            to imagine that something may change, to plant a seed without knowing
            the weather, or to let someone help. We can hold uncertainty and still
            choose care. Sometimes that choice is enough to keep a small light alive
            until the next morning.
        """,
    }
]


def home(request):
    latest_posts = sorted(posts_data, key=lambda post: post["date"], reverse=True)[:3]
    return render(request, "blogs/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blogs/posts.html", {"posts": posts_data})


def post_details(request, slug):
    post = next((post for post in posts_data if post["slug"] == slug), None)
    if post is None:
        raise Http404("Post not found")

    return render(request, "blogs/post_details.html", {"post": post})


def page_not_found(request, exception):
    return render(request, "404.html", status=404)