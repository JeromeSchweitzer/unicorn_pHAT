# unicorn_pHAT
Expanding on a binary clock project for the Raspberry Pi Unicorn pHAT.

Inspired by Frederick Vandenbosch's project: https://www.instructables.com/Pi-Zero-Binary-Clock/.

This project differs from Vandenbosch's in that the column colors indicate the days of the week that have a chance of rain. This is done by calling OpenWeatherMap's (OWM) forecasting in `forecasting.py`. Pixels colors are also changed upon incoming ssh connections to the pi. Finally, I have implemented functions in `message.py` that roll messages in 3x4 pixeled characters across the pHAT. `message.py` is useful for greetings and error messages across the hat, especially when working without a monitor.

### Notes:
Run the entire binary clock program with: `sudo -E python3 bc.py` - `unicornhat` requires root permissions and `geocoder` needs persisted environment variables (hence the `sudo` and `-E`, respectively).

The OWM API requires a key, here I have stored this in an environment variable, `owm_key`.

If running `bc.py` from a cron job, you may need to export the OWM API key here as well, something like:
```
@reboot export owm_key='12345asdf' && sudo -E /home/pi/bc.py
```

