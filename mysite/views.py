import re
from django.views import View
from django.shortcuts import render

class Home(View):
  def get(self, request):
    return render(request, 'home.html')
  
  def post(self, request):
    try:
      name = request.POST['fullname']
    except Exception as e:
      message = "Invalid Name (cannot be %s)" % str(name)
      return render(request, 'error.html', {'message': message, 'error': e})
    try:
      weight = request.POST['weight']
      if weight.isnumeric():
        weight = int(weight)
      else:
        raise AssertionError
      assert weight > 0 # Test if weight is positive
    except AssertionError:
      message = 'Enter a number greater than 0 for weight  (cannot be "%s")' % str(weight)
      return render(request, 'error.html', {'message': message})
    try:
      heightPattern = re.compile(r"""(\d+)' *(\d+)(?:"|'')?""")
      height = request.POST['height']
      match = re.match(heightPattern, height)
      if not match:
        message = ValueError('Invalid Height: Enter your height in feet and inches i.e. 5\'10')
        return render(request, 'error.html', {'message': message})
      feet, inches = map(int, match.groups())
      inches += feet*12 # Convert height to inches
      assert inches > 0
    except AssertionError:
      message = "Height must be a postive number (cannot be %s)" % str(inches)
      return render(request, 'error.html', {'message': message})
    # Calculating BMI based on [weight (lb) / height (in) / height (in)] x 703
    bmi = round(weight/inches/inches*703, 1)
    return render(request, 'success.html', {'name': name, 'bmi': bmi})