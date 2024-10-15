
# Django Template Language (DTL) DateTime Format Parameters

In Django templates, you can format dates, times, and datetime objects using the `date` and `time` filters. Below is a comprehensive list of all the format characters available, and what they represent.

## 1. Date Format Characters

- **`d`**: Day of the month, 2 digits with leading zeros.
  ```html
  {{ date_value|date:"d" }}
  ```
  Example: If `date_value = datetime(2023, 10, 15)`, output will be `"15"`.

- **`D`**: Day of the week, abbreviated (e.g., Sun, Mon).
  ```html
  {{ date_value|date:"D" }}
  ```
  Example: If `date_value = datetime(2023, 10, 15)`, output will be `"Sun"`.

- **`j`**: Day of the month without leading zeros.
  ```html
  {{ date_value|date:"j" }}
  ```
  Example: If `date_value = datetime(2023, 10, 5)`, output will be `"5"`.

- **`l`**: Day of the week, full name (e.g., Sunday, Monday).
  ```html
  {{ date_value|date:"l" }}
  ```
  Example: If `date_value = datetime(2023, 10, 15)`, output will be `"Sunday"`.

- **`F`**: Month, full name (e.g., January, February).
  ```html
  {{ date_value|date:"F" }}
  ```
  Example: If `date_value = datetime(2023, 10, 15)`, output will be `"October"`.

- **`m`**: Month, 2 digits with leading zeros (01 to 12).
  ```html
  {{ date_value|date:"m" }}
  ```
  Example: If `date_value = datetime(2023, 10, 15)`, output will be `"10"`.

- **`M`**: Month, abbreviated (e.g., Jan, Feb).
  ```html
  {{ date_value|date:"M" }}
  ```
  Example: If `date_value = datetime(2023, 10, 15)`, output will be `"Oct"`.

- **`n`**: Month without leading zeros.
  ```html
  {{ date_value|date:"n" }}
  ```
  Example: If `date_value = datetime(2023, 10, 5)`, output will be `"10"`.

- **`Y`**: Year, 4 digits.
  ```html
  {{ date_value|date:"Y" }}
  ```
  Example: If `date_value = datetime(2023, 10, 15)`, output will be `"2023"`.

- **`y`**: Year, 2 digits.
  ```html
  {{ date_value|date:"y" }}
  ```
  Example: If `date_value = datetime(2023, 10, 15)`, output will be `"23"`.

## 2. Time Format Characters

- **`H`**: Hour (24-hour format) with leading zeros.
  ```html
  {{ time_value|time:"H" }}
  ```
  Example: If `time_value = time(14, 30)`, output will be `"14"`.

- **`h`**: Hour (12-hour format) with leading zeros.
  ```html
  {{ time_value|time:"h" }}
  ```
  Example: If `time_value = time(14, 30)`, output will be `"02"`.

- **`i`**: Minutes with leading zeros.
  ```html
  {{ time_value|time:"i" }}
  ```
  Example: If `time_value = time(14, 5)`, output will be `"05"`.

- **`s`**: Seconds with leading zeros.
  ```html
  {{ time_value|time:"s" }}
  ```
  Example: If `time_value = time(14, 30, 5)`, output will be `"05"`.

- **`A`**: Uppercase AM or PM.
  ```html
  {{ time_value|time:"A" }}
  ```
  Example: If `time_value = time(14, 30)`, output will be `"PM"`.

- **`P`**: Lowercase am or pm.
  ```html
  {{ time_value|time:"P" }}
  ```
  Example: If `time_value = time(14, 30)`, output will be `"pm"`.

## 3. Datetime Format Characters

You can combine date and time format characters for a complete `datetime` format.

Example:
```html
{{ datetime_value|date:"Y-m-d H:i:s" }}
```
If `datetime_value = datetime(2023, 10, 15, 14, 30, 45)`, output will be `"2023-10-15 14:30:45"`.

### Common Examples:

1. **Full Date and Time (24-hour format)**:
    ```html
    {{ datetime_value|date:"Y-m-d H:i:s" }}
    ```
    Example Output: `"2023-10-15 14:30:45"`.

2. **12-hour Time with AM/PM**:
    ```html
    {{ datetime_value|date:"h:i A" }}
    ```
    Example Output: `"02:30 PM"`.

3. **Day, Month (Abbreviated), Year**:
    ```html
    {{ datetime_value|date:"d M Y" }}
    ```
    Example Output: `"15 Oct 2023"`.

4. **Full Day of Week, Month, and Day**:
    ```html
    {{ datetime_value|date:"l, F d" }}
    ```
    Example Output: `"Sunday, October 15"`.

---

This guide covers the most important date and time format characters in Django Template Language.
