from django.shortcuts import render

posts = [
    {
        "author": "Jatin Singhal",
        "title": "Post 1",
        "content": "Post 1 Body Content",
        "date_posted": "Feb 5, 2022"
    },
    {
        "author": "Corey Schafer",
        "title": "Post 2",
        "content": "Post 2 Body Content",
        "date_posted": "Feb 6, 2022"
    }
]


def home(request):
    context = {
        "posts": posts
    }

    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
