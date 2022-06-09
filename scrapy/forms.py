from . import parser, models
from django import forms

class ParserForm(forms.Form):
    MEDIA_CHOICE = (
        ("Movies", "Movies"),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        fields = [
            "media_type",
        ]

    def parser_data(self):
        if self.data['media_type'] == "Movies":
            movies_parser = parser.parser_fuct()
            for data in movies_parser:
                models.Movies.objects.create(**data)
