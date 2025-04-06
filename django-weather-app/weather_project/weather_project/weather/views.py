from django.shortcuts import render # type: ignore
import requests # type: ignore

def index(request):
    data = None
    if request.method == "POST":
        city = request.POST.get('city')
        api_key = "YOUR_API_KEY"  # Replace with your key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={5779be2437fdd64a9e8df76bd124ee90}&units=metric"
        
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            data = {
                "city": city,
                "temperature": json_data["main"]["temp"],
                "description": json_data["weather"][0]["description"].title(),
                "humidity": json_data["main"]["humidity"],
                "wind_speed": json_data["wind"]["speed"],
            }
        else:
            data = {"city": city, "temperature": "Not Found"}

    return render(request, "index.html", {"data": data})

##some changes