from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = "db8b36227cmsh36904c604d3a623p128502jsn3760ceaa8a89"
url = "https://coinranking1.p.rapidapi.com/stats?referenceCurrencyUuid=yhjMzLPhuIDl"

headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symbol = request.form['symbol'].upper()
        response = requests.get(url, headers=headers)
        data = response.json()
        
        coins = data['data']['bestCoins'] + data['data']['newestCoins']
        coin = next((coin for coin in coins if coin['symbol'] == symbol), None)
        
        if coin:
            return render_template('index.html', coin=coin)
        else:
            error = f"No coin found with symbol: {symbol}"
            return render_template('index.html', error=error)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()