
# Air Alert - AQI Retrieval and Push notification

Air Alert AQI Checker is a Python script that retrieves air quality data for a specified location using the AirVisual API and logs the data to a CSV file. The script also sends notifications through Pushbullet if the AQI exceeds certain thresholds.

## Installation

1. Fork this repository to your own GitHub account.
2. Create an account with [IQair](https://www.iqair.com/us/commercial-air-quality-monitors/api) and [Pushbullet](https://www.pushbullet.com/) to get your API keys.
3. Set the environment variables `AIRVISUAL_API_KEY` and `PUSHBULLET_API_KEY` with your respective API keys under Settings in your forked repository.
4. Check if the actions are being executed.
   - To check if your Pushbullet API key works you can change the first threshold number to something low such as 1 to guarantee a push notification is sent.
   
## Usage

With the `.github/workflows` folder and the `main.yml` in it, the script should be executed by GitHub Actions every hour. The script will retrieve air quality data and some weather data for the specified location and log it to a CSV file named `data.csv`. If the AQI exceeds certain thresholds, a notification will be sent through Pushbullet.

You can modify the notification alerts by adjusting the text in the script file and adjusting it to the location you are interested in. Keep in mind that the community API key has limitations. 

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you would like to contribute to this project.

## License

This project is licensed under the MIT License.

## Sidenote
Please be aware of your GitHub Actions quota. Runnings this script for a month will take about 731 hours in total for a full 30-day cycle. 

