from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Dealer, Review

def home(request):
    dealers = Dealer.objects.all()
    return render(request, "index.html", {"dealers": dealers})

def dealer_detail(request, dealer_id):
    dealer = get_object_or_404(Dealer, id=dealer_id)
    reviews = dealer.reviews.all()
    return render(request, "dealer_detail.html", {
        "dealer": dealer,
        "reviews": reviews
    })

@login_required
def post_review(request, dealer_id):
    dealer = get_object_or_404(Dealer, id=dealer_id)

    if request.method == "POST":
        review_text = request.POST.get("review")
        rating = request.POST.get("rating")
        Review.objects.create(
            dealer=dealer,
            user=request.user,
            review=review_text,
            rating=rating
        )
        return redirect("dealer_detail", dealer_id=dealer.id)

    return render(request, "dealer_review.html", {"dealer": dealer})