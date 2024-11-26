# Weather API Application

This is a Python project that interacts with a weather API to provide:
- **Today's Weather**: Displays current weather conditions for a given city.
- **5-Day Forecast**: Provides weather predictions for the next 5 days.

---

## **Features**
1. **Get Today's Weather**:
   - Retrieves weather data for the current day.
   - Outputs:
     - Weather description (e.g., clear sky, rain).
     - Temperature (in °C).
     - Feels-like temperature.
     - Wind speed (in m/s).

2. **Get Weekly Weather**:
   - Provides a 5-day forecast starting from the next day.
   - Outputs the same details as "Today's Weather" for each day.

3. **Error Handling**:
   - Displays appropriate error messages when API calls fail.

---

## **Requirements**
- Python 3.7 or later.
- Installed libraries:
  - `requests`
  - `datetime`

Install dependencies using pip:
```bash
pip install requests
