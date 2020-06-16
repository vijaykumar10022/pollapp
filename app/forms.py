from django.forms import ModelForm
from app.models import Spoll

class Myform(ModelForm):
	class Meta:
		model=Spoll
		fields='__all__'