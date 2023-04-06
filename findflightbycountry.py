import requests

url = "https://skyscanner44.p.rapidapi.com/fly-to-country"

querystring = {"destination":"SI","origin":"MUC","departureDate":"2023-07-01","returnDate":"2023-07-21","currency":"EUR","locale":"en-GB","country":"UK"}

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "skyscanner44.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)