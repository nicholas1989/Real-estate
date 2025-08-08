from django.forms import ModelForm
from .models import Listing


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            "title",
            "address",
            "price",
            "square_footage",
            "num_rooms",
            "image"
        ]