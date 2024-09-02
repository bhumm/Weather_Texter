# Weather_Texter
Weather forecast texts to your phone using Sinch. This is a simple script that relys on the NOAA SDK (https://github.com/paulokuong/noaa). It is recommended to run this script daily using a cronjob or on a VM. 

The script sends forecast information, temperature, wind speed, and precipitation for 7am, 12pm, and 5pm for your timezone.

You need to input your own values for:
- your zipcode
- your country
- Sinch service plan ID
- Sinch API token
- The sending number
- The receiving number
- Sinch API link
